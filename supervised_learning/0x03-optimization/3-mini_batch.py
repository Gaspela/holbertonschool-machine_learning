#!/usr/bin/env python3
"""Function that trains a loaded neural network
model using mini-batch gradient descent"""

import tensorflow as tf

shuffle_data = __import__('2-shuffle_data').shuffle_data


def train_mini_batch(X_train, Y_train, X_valid, Y_valid,
                     batch_size=32, epochs=5,
                     load_path="/tmp/model.ckpt", save_path="/tmp/model.ckpt"):
    """
    X_train: is a numpy.ndarray of shape (m, 784) containing the training data.
    m: is the number of data points.
    784: is the number of input features.
    Y_train: is a one-hot numpy.ndarray of shape (m, 10) containing the
    training labels.
    10 is the number of classes the model should classify.
    X_valid: is a numpy.ndarray of shape (m, 784) containing the validation
    data.
    Y_valid: is a one-hot numpy.ndarray of shape (m, 10) containing the
    validation labels.
    batch_size is the number of data points in a batch.
    epochs is the number of times the training should pass through the whole
    dataset.
    load_path: is the path from which to load the model.
    save_path: is the path to where the model should be saved after training.
    Returns: the path where the model was saved.
    """
    with tf.Session() as sess:
        saver = tf.train.import_meta_graph(load_path + ".meta")
        saver.restore(sess, load_path)
        x = tf.get_collection("x")[0]
        y = tf.get_collection("y")[0]
        train_op = tf.get_collection("train_op")[0]
        accuracy = tf.get_collection("accuracy")[0]
        loss = tf.get_collection("loss")[0]

        for i in range(epochs + 1):
            accuracy_train, cost_train = sess.run([accuracy, loss], feed_dict={
                x: X_train, y: Y_train})
            accuracy_evaluate, cost_valid = sess.run([accuracy, loss],
                                                     feed_dict={x: X_valid,
                                                                y: Y_valid})
            print("After {} epochs:".format(i))
            print("\tTraining Cost: {}".format(cost_train))
            print("\tTraining Accuracy: {}".format(accuracy_train))
            print("\tValidation Cost: {}".format(cost_valid))
            print("\tValidation Accuracy: {}".format(accuracy_evaluate))
            if i < epochs:
                X_shuffled, Y_shuffled = shuffle_data(X_train, Y_train)
                batch = X_shuffled.shape[0]
                start = 0
                step = 1
                while batch > 0:
                    if batch - batch_size < 0:
                        end = X_shuffled.shape[0]
                    else:
                        end = start + batch_size
                    X = X_shuffled[start:end]
                    Y = Y_shuffled[start:end]
                    sess.run(train_op, feed_dict={x: X, y: Y})
                    if step % 100 == 0:
                        step_cost = sess.run(loss, feed_dict={x: X, y: Y})
                        step_acc = sess.run(accuracy, feed_dict={x: X, y: Y})
                        print("\tStep {}:".format(step))
                        print("\t\tCost: {}".format(step_cost))
                        print("\t\tAccuracy: {}".format(step_acc))
                    step = step + 1
                    batch = batch - batch_size
                    start = start + batch_size

        return saver.save(sess, save_path)
