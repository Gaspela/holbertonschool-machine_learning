#!/usr/bin/env python3
"""
Pipeline
"""
import tensorflow.compat.v2 as tf
import tensorflow_datasets as tfds


class Dataset():
    """
    pr to en
    """

    def __init__(self, batch_size, max_len):
        """
        data_train, which contains the ted_hrlr_translate/pt_to_en tf.data
        Dataset train split, loaded as_supervided
        data_valid, which contains the ted_hrlr_translate/pt_to_en tf.data
        Dataset validate split, loaded as_supervided
        tokenizer_pt is the Portuguese tokenizer created from the training set
        tokenizer_en is the English tokenizer created from the training set
        """
        examples, data_info = tfds.load('ted_hrlr_translate/pt_to_en',
                                        with_info=True,
                                        as_supervised=True)
        data_info = data_info
        data_train, data_valid = examples['train'], examples['validation']
        self.tokenizer_pt, self.tokenizer_en = self.tokenize_dataset(
            data_train)

        data_train = data_train.map(self.tf_encode)
        data_valid = data_valid.map(self.tf_encode)

        def filter_max_length(x, y, max_length=max_len):
            return tf.logical_and(tf.size(x) <= max_length,
                                  tf.size(y) <= max_length)

        data_train = data_train.filter(filter_max_length)
        data_train = data_train.cache()

        train_dataset_size = data_info.splits['train'].num_examples

        data_train = data_train.shuffle(train_dataset_size)
        padded_shapes = ([None], [None])
        data_train = data_train.padded_batch(batch_size,
                                             padded_shapes=padded_shapes)
        self.data_train = data_train.prefetch(tf.data.experimental.AUTOTUNE)
        data_valid = data_valid.filter(filter_max_length)
        padded_shapes = ([None], [None])
        self.data_valid = data_valid.padded_batch(batch_size,
                                                  padded_shapes=padded_shapes)

    def tokenize_dataset(self, data):
        """
        data is a tf.data.Dataset whose examples are formatted as a tuple(pten)
        pt is the tf.Tensor containing the Portuguese sentence
        en is the tf.Tensor containing the corresponding English sentence
        """
        tokenizer_pt = tfds.features.text.SubwordTextEncoder.build_from_corpus(
            (pt.numpy() for pt, en in data),
            target_vocab_size=2**15)

        tokenizer_en = tfds.features.text.SubwordTextEncoder.build_from_corpus(
            (en.numpy() for pt, en in data),
            target_vocab_size=2**15)

        return (tokenizer_pt, tokenizer_en)

    def encode(self, pt, en):
        """
        pt is the tf.Tensor containing the Portuguese sentence
        en is the tf.Tensor containing the corresponding English sentence
        """
        pt_tokens = [self.tokenizer_pt.vocab_size] +\
            self.tokenizer_pt.encode(pt.numpy()) +\
            [self.tokenizer_pt.vocab_size + 1]

        en_tokens = [self.tokenizer_en.vocab_size] +\
            self.tokenizer_en.encode(en.numpy()) +\
            [self.tokenizer_en.vocab_size + 1]

        return (pt_tokens, en_tokens)

    def tf_encode(self, pt, en):
        """
        Make sure to set the shape of the pt and en return tensors
        """
        result_pt, result_en = tf.py_function(self.encode, [pt, en],
                                              [tf.int64, tf.int64])
        result_pt.set_shape([None])
        result_en.set_shape([None])

        return (result_pt, result_en)
