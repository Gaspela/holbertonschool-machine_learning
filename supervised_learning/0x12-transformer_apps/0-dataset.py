#!/usr/bin/env python3
"""
Dataset
"""

import tensorflow.compat.v2 as tf
import tensorflow_datasets as tfds


class Dataset:
    """
    pt to en
    """

    def __init__(self):
        """
        data_train, which contains the ted_hrlr_translate/pt_to_en tf.data
        Dataset train split, loaded as_supervided
        data_valid, which contains the ted_hrlr_translate/pt_to_en tf.data
        Dataset validate split, loaded as_supervided
        tokenizer_pt is the Portuguese tokenizer created from the training set
        tokenizer_en is the English tokenizer created from the training set
        """
        self.data_train = tfds.load('ted_hrlr_translate/pt_to_en',
                                    split='train', as_supervised=True)
        self.data_valid = tfds.load('ted_hrlr_translate/pt_to_en',
                                    split='validation', as_supervised=True)

        tokenizer_pt, tokenizer_en = self.tokenize_dataset(self.data_train)
        self.tokenizer_pt = tokenizer_pt
        self.tokenizer_en = tokenizer_en

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
