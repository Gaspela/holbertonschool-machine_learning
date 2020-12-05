#!/usr/bin/env python3
"""
Bidirectional Output
"""
import numpy as np


class BidirectionalCell:
    """
    represents a bidirectional cell of an RNN:
    """

    def __init__(self, i, h, o):
        """
        i is the dimensionality of the data
        h is the dimensionality of the hidden states
        o is the dimensionality of the outputs
        Creates the public instance attributes Whf, Whb, Wy, bhf, bhb, by that
        represent the weights and biases of the cell
        Whf and bhfare for the hidden states in the forward direction
        Whb and bhbare for the hidden states in the backward direction
        Wy and byare for the outputs
        """
        self.Whf = np.random.randn(h+i, h)
        self.Whb = np.random.randn(h+i, h)
        self.Wy = np.random.randn(h * 2, o)
        self.bhf = np.zeros((1, h))
        self.bhb = np.zeros((1, h))
        self.by = np.zeros((1, o))

    def forward(self, h_prev, x_t):
        """
        x_t is a numpy.ndarray of shape(m, i) that contains the data input
        for the cell
        m is the batch size for the data
        h_prev is a numpy.ndarray of shape(m, h) containing the previous
        hidden state
        Returns: h_next, the next hidden state
        """
        h_next = np.tanh(np.matmul(np.hstack((h_prev, x_t)), self.Whf)
                         + self.bhf)
        return (h_next)

    def backward(self, h_next, x_t):
        """
        x_t is a numpy.ndarray of shape(m, i) that contains the data input
        for the cell
        m is the batch size for the data
        h_next is a numpy.ndarray of shape(m, h) containing the next hidden
        state
        Returns: h_pev, the previous hidden state
        """
        h_prev = np.tanh(np.matmul(np.hstack((h_next, x_t)), self.Whb)
                         + self.bhb)
        return (h_prev)

    def softmax(self, x):
        """
        funtion softmax values
        """
        exp_x = np.exp(x)
        return exp_x / exp_x.sum(axis=1, keepdims=True)

    def output(self, H):
        """
        H is a numpy.ndarray of shape (t, m, 2 * h) that contains the
        concatenated hidden states from both directions, excluding their
        initialized states
        t is the number of time steps
        m is the batch size for the data
        h is the dimensionality of the hidden states
        Returns: Y, the outputs
        """
        t, m, h2 = H.shape
        Y = []
        for t in range(t):
            y = self.softmax(np.matmul(H[t], self.Wy) + self.by)
            Y.append(y)

        return (np.array(Y))
