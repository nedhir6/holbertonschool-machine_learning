#!/usr/bin/env python3
""" Class that loads and preps a dataset for machine translation """
import tensorflow.compat.v2 as tf
import tensorflow_datasets as tfds


class Dataset:
    """ Class that loads and preps a dataset for machine translation """

    def __init__(self):
        """initialization"""
        self.data_train, self.data_valid = tfds.load(
            'ted_hrlr_translate/pt_to_en',
            split=['train', 'validation'],
            as_supervised=True)
        self.tokenizer_pt, self.tokenizer_en = self.tokenize_dataset(
            self.data_train)

    def tokenize_dataset(self, data):
        """ Instance method that creates sub-word tokenizers for our dataset
            data: tf.data.Dataset """
        ste = tfds.deprecated.text.SubwordTextEncoder.build_from_corpus
        tokenizer_pt = ste([pt.numpy() for pt, _ in data],
                           target_vocab_size=2 ** 15)
        tokenizer_en = ste([en.numpy() for _, en in data],
                           target_vocab_size=2**15)
        return tokenizer_pt, tokenizer_en
