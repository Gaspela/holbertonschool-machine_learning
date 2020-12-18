#!/usr/bin/env python3
"""
Extract Word2Vec
"""

from gensim.models import Word2Vec


def gensim_to_keras(model):
    """
    model is a trained gensim word2vec models
    Returns: the trainable keras Embedding
    """
    layer = model.wv.get_keras_embedding()
    return (layer)
