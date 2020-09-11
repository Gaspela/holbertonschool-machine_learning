#!/usr/bin/env python3
"""
Pooling Back Prop
"""

import numpy as np


def pool_backward(dA, A_prev, kernel_shape, stride=(1, 1), mode='max'):
    """
    m is the number of examples
    h_dp is the height of the output
    w_dp is the width of the output
    c_new is the number of channels in the output
    h_prev is the height of the previous layer
    w_prev is the width of the previous layer
    c_prev is the number of channels in the previous layer
    kh is the filter height
    kw is the filter width
    sh is the stride for the height
    sw is the stride for the width
    Returns: the partial derivatives with respect to the previous layer
    (dA_prev).
    """

    m = dA.shape[0]
    h_new = dA.shape[1]
    w_new = dA.shape[2]
    c_new = dA.shape[3]
    m = A_prev.shape[0]
    kh = kernel_shape[0]
    kw = kernel_shape[1]
    sh = stride[0]
    sw = stride[1]

    dA_prev = np.zeros_like(A_prev)
    for i in range(m):
        for j in range(h_new):
            for k in range(w_new):
                for cn in range(c_new):
                    if mode == 'max':
                        A_min = A_prev[i,
                                       j*sh:kh+(j*sh),
                                       k*sw:kw+(k*sw),
                                       cn]
                        pen = (A_min == np.max(A_min))
                        dA_prev[i,
                                j*sh:kh+(j*sh),
                                k*sw:kw+(k*sw),
                                cn] += dA[i, j, k, cn] * pen
                    if mode == 'avg':
                        dA_prev[i,
                                j*sh:kh+(j*sh),
                                k*sw:kw+(k*sw),
                                cn] += (dA[i, j, k, cn])/kh/kw

    return dA_prev
