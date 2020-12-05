#!/usr/bin/env python3
"""
LSTM Cell
"""
import numpy as np


class LSTMCell:
    """
    represents an LSTM unit
    """

    def __init__(self, i, h, o):
        """
        i is the dimensionality of the data
        h is the dimensionality of the hidden state
        o is the dimensionality of the outputs
        Creates the public instance attributes Wf, Wu, Wc, Wo, Wy, bf, bu, bc,
        bo, by that represent the weights and biases of the cell
        Wfand bf are for the forget gate
        Wuand bu are for the update gate
        Wcand bc are for the intermediate cell state
        Woand bo are for the output gate
        Wyand by are for the outputs
        """
        self.Wf = np.random.randn(h+i, h)
        self.Wu = np.random.randn(h+i, h)
        self.Wc = np.random.randn(h+i, h)
        self.Wo = np.random.randn(h+i, h)
        self.Wy = np.random.randn(h, o)

        self.bf = np.zeros((1, h))
        self.bu = np.zeros((1, h))
        self.bc = np.zeros((1, h))
        self.bo = np.zeros((1, h))
        self.by = np.zeros((1, o))

    def softmax(self, x):
        """
        funtion softmax values
        """
        exp_x = np.exp(x)
        return exp_x / exp_x.sum(axis=1, keepdims=True)

    def sigmoid(self, x):
        """
        funtion sigmoid activation
        """
        return 1 / (1 + np.exp(-x))

    def forward(self, h_prev, c_prev, x_t):
        """
        x_t is a numpy.ndarray of shape (m, i) that contains the data input
        for the cell
        m is the batche size for the data
        h_prev is a numpy.ndarray of shape (m, h) containing the previous
        hidden state
        c_prev is a numpy.ndarray of shape (m, h) containing the previous cell
        state
        The output of the cell should use a softmax activation function
        Returns: h_next, c_next, y
        h_next is the next hidden state
        c_next is the next cell state
        y is the output of the cell
        """
        u_c = np.concatenate((h_prev, x_t), axis=1)
        forgetsig = self.sigmoid(np.matmul(u_c, self.Wf) + self.bf)
        middlesig = self.sigmoid(np.matmul(u_c, self.Wu) + self.bu)
        active = np.tanh(np.matmul(u_c, self.Wc) + self.bc)
        c_next = middlesig * active + forgetsig * c_prev
        outsig = self.sigmoid(np.matmul(u_c, self.Wo) + self.bo)
        h_next = outsig * np.tanh(c_next)
        y = self.softmax(np.matmul(h_next, self.Wy) + self.by)

        return (h_next, c_next, y)
