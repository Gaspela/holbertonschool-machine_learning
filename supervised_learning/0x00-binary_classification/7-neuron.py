#!/usr/bin/env python3
"""
Class Neuron that defines a single neuron performing binary
classification
"""


import numpy as np
""" Single neuron performing binary classification """


class Neuron:
    """Neuron performing binary classification"""

    def __init__(self, nx):
        """
        nx: number of input features
        _W: The weights vector for the neuron. Upon instantiation,
        it should be initialized using a random normal distribution.
        _b: The bias for the neuron. Upon instantiation,
        it should be initialized to 0.
        _A: The activated output of the neuron (prediction).
        Upon instantiation, it should be initialized to 0.
        """
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")

        # Private instance attributes
        self.__W = np.ndarray((1, nx))
        self.__W[0] = np.random.normal(size=nx)
        self.__b = 0
        self.__A = 0

    # getter function
    @property
    def W(self):
        """Return weights vector for the neuron """
        return self.__W

    @property
    def b(self):
        """Return bias for the neuron """
        return self.__b

    @property
    def A(self):
        """Return activated output of the neuron """
        return self.__A

    def forward_prop(self, X):
        """
        Calculate the forward propagation of the neuron
        nx: is the number of input features to the neuron
        m: is the number of examples,
        """
        z = np.dot(self.__W, X) + self.__b
        sigmoid = 1 / (1 + np.exp(-z))
        self.__A = sigmoid

        return self.__A

    def cost(self, Y, A):
        """
        Calculates the cost of the model using logistic regression
        Y: is a numpy.ndarray with shape (1, m),
        that contains the correct labels for the input data.
        A: is a numpy.ndarray with shape (1, m)
        containing the activated output of the neuron for each example
        """
        y1 = 1 - Y
        y2 = 1.0000001 - A
        m = Y.shape[1]
        cost = -1 * (1 / m) * np.sum(Y * np.log(A) + y1 * np.log(y2))

        return cost

    def evaluate(self, X, Y):
        """
        Evaluates the neuron’s predictions
        nx: is the number of input features to the neuron.
        m: is the number of examples.
        Y: is a numpy.ndarray with shape (1, m) that contains
        the correct labels for the input data.
        """
        A = self.forward_prop(X)
        cost = self.cost(Y, A)
        return np.round(A).astype(int), self.cost(Y, A)

    def gradient_descent(self, X, Y, A, alpha=0.05):
        """
        Calculates one pass of gradient descent on the neuron
        X: is a numpy.ndarray with shape (nx, m)
        that contains the input data.
        nx: is the number of input features to the neuron.
        m: is the number of examples.
        Y: is a numpy.ndarray with shape (1, m) that contains
        the correct labels for the input data.
        A: is a numpy.ndarray with shape (1, m) containing the
        activated output of the neuron for each example.
        alpha: is the learning rate.
        """
        self.__W[0] = (self.__W[0] - alpha *
                       np.dot(X, (A - Y).T).T[0] / X.shape[1])
        self.__b -= alpha * (A[0] - Y[0]).mean()

    def train(self, X, Y, step=5000, alpha=0.05, verbose=True,
              graph=True, step=100):
        """
        Trains the neuron.
        X: is a numpy.ndarray with shape (nx, m) that contains the input data.
            nx: is the number of input features to the neuron.
            m: is the number of examples.
        Y: is a numpy.ndarray with shape (1, m) that contains
        the correct labels for the input data.
        step: is the number of step to train over.
        alpha: is the learning rate.
        verbose: is a boolean that defines whether or not to print information
        about the training, If True, print Cost after {iteration} step:
        {cost} every step step.
        graph: is a boolean that defines whether or not to graph information
        about the training once the training has completed.

        """
        if type(step) is not int:
            raise TypeError("step must be an integer")
        if step <= 0:
            raise ValueError("step must be a positive integer")
        if type(alpha) is not float:
            raise TypeError("alpha must be a float")
        if alpha <= 0:
            raise ValueError("alpha must be positive")
        if verbose or graph:
            if type(step) is not int:
                raise TypeError("step must be an integer")
        if step < 1:
            raise ValueError("step must be a positive integer")

        cost_list = []
        accuracy_list = []

        for i in range(step + 1):
            self.forward_prop(X)
            self.gradient_descent(X, Y, self.__A, alpha)
            cost = self.cost(Y, self.__A)

            if verbose:
                if i % step == 0 or step == step:
                    cost_list.append(cost)
                    accuracy_list.append(i)
                    print("Cost after {} step: {}".format(i, cost))

        if graph:
            plt.plot(accuracy_list, cost_list)
            plt.xlabel('iteration')
            plt.ylabel('cost')
            plt.title("Trainig Cost")
            plt.show()

        return self.evaluate(X, Y)
