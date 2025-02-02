#!/usr/bin/env python3
""" Train """

import tensorflow as tf

calculate_accuracy = __import__('3-calculate_accuracy').calculate_accuracy
calculate_loss = __import__('4-calculate_loss').calculate_loss
create_placeholders = __import__('0-create_placeholders').create_placeholders
create_train_op = __import__('5-create_train_op').create_train_op
forward_prop = __import__('2-forward_prop').forward_prop


def train(X_train, Y_train, X_valid, Y_valid, layer_sizes, activations, alpha,
          iterations, save_path="/tmp/model.ckpt"):
    """
    X_train is a numpy.ndarray containing the training input data
    Y_train is a numpy.ndarray containing the training labels
    X_valid is a numpy.ndarray containing the validation input data
    Y_valid is a numpy.ndarray containing the validation labels
    layer_sizes is a list containing the number of nodes in each layer of
    the network.
    activations is a list containing the activation functions for each layer
    of the network.
    alpha is the learning rate
    iterations is the number of iterations to train over
    save_path designates where to save the model
    """
    trainx = X_train.shape[1]
    layers = layer_sizes[-1]
    x, y = create_placeholders(trainx, layers)

    y_pred = forward_prop(x, layer_sizes, activations)
    loss = calculate_loss(y, y_pred)
    accuracy = calculate_accuracy(y, y_pred)
    train_op = create_train_op(loss, alpha)

    tf.add_to_collection('x', x)
    tf.add_to_collection('y', y)
    tf.add_to_collection('y_pred', y_pred)
    tf.add_to_collection('loss', loss)
    tf.add_to_collection('accuracy', accuracy)
    tf.add_to_collection('train_op', train_op)

    init = tf.global_variables_initializer()
    saver = tf.train.Saver()
    sess = tf.Session()
    sess.run(init)

    for i in range(iterations + 1):
        loss_train, accuracy_train = sess.run((loss, accuracy),
                                              feed_dict={x: X_train,
                                                         y: Y_train})
        loss_valid, accuracy_valid = sess.run((loss, accuracy),
                                              feed_dict={x: X_valid,
                                                         y: Y_valid})
        if not i % 100 or i == iterations:
            print('After {} iterations:'.format(i))
            print('\tTraining Cost: {}'.format(loss_train))
            print('\tTraining Accuracy: {}'.format(accuracy_train))
            print('\tValidation Cost: {}'.format(loss_valid))
            print('\tValidation Accuracy: {}'.format(accuracy_valid))
        if i < iterations:
            sess.run(train_op, feed_dict={x: X_train, y: Y_train})
    save_path = saver.save(sess, save_path)

    return save_path
