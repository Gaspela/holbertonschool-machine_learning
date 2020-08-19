#!/usr/bin/env python3
""" Evaluate """

import tensorflow as tf


def evaluate(X, Y, save_path):
    """
    X is a numpy.ndarray containing the input data to evaluate.
    Y is a numpy.ndarray containing the one-hot labels for X.
    save_path is the location to load the model from.
    You are not allowed to use tf.saved_model.
    """
    with tf.Session() as sess:
        saver = tf.train.import_meta_graph('{}.meta'.format(save_path))
        saver.restore(sess, save_path)
        x = tf.get_collection('x')[0]
        y = tf.get_collection('y')[0]
        y_pred = tf.get_collection('y_pred')[0]
        loss = tf.get_collection('loss')[0]
        accuracy = tf.get_collection('accuracy')[0]

        y_pred_evaluate, loss_evaluate,
        accuracy_evaluate = sess.run((y_pred, loss,
                                      accuracy),
                                     feed_dict={x: X,
                                                y: Y})

    return y_pred_evaluate, accuracy_evaluate, loss_evaluate
