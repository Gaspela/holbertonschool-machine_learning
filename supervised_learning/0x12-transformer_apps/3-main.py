#!/usr/bin/env python3

import tensorflow as tf
Dataset = __import__('3-dataset').Dataset

tf.compat.v1.enable_eager_execution()
tf.compat.v1.set_random_seed(0)
data = Dataset(32, 40)
for pt, en in data.data_train.take(1):
    print(pt, en)
for pt, en in data.data_valid.take(1):
    print(pt, en)
