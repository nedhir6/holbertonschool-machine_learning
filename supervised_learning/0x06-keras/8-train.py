#!/usr/bin/env python3
"""function that hat trains a model using mini-batch gradient descent"""
import tensorflow.keras as K


def train_model(
        network,
        data,
        labels,
        batch_size,
        epochs,
        validation_data=None,
        early_stopping=False,
        patience=0,
        learning_rate_decay=False,
        alpha=0.1,
        decay_rate=1,
        save_best=False,
        filepath=None,
        verbose=True,
        shuffle=False):
    """network is the model to train
    data: array containing the input data
    labels: is a one-hot containing the labels of data
    batch_size: size of the batch used for mini-batch gradient descent
    epochs: the number of passes through data
    validation_data: data to validate the model with, if not None
    early_stopping: boolean indicates whether early stopping
    should be used
    patience is the patience used for early stopping
    learning_rate_decay: boolean indicates whether learning
    rate decay should be used
    alpha: initial learning rate
    decay_rate: decay rate
    save_best: boolean indicating whether to save
    the model after each epoch if it is the best
    filepath: file path where the model should be saved
    verbose: boolean that determines if output should be
    printed during training
    shuffle: boolean that determines whether to shuffle the
    batches every epoch.
    Returns: History object generated after training the model"""
    def scheduler(epoch):
        return alpha / (1 + (decay_rate * epoch))
    model = network
    callbacks = []
    if early_stopping:
        callbacks.append(K.callbacks.EarlyStopping(
            monitor='val_loss', patience=patience))
    if learning_rate_decay and validation_data:
        callbacks.append(
            K.callbacks.LearningRateScheduler(
                scheduler, verbose=1))
    if save_best:
        callbacks.append(K.callbacks.ModelCheckpoint(
            filepath=filepath, save_best_only=True))
    hist_obj = model.fit(
        x=data,
        y=labels,
        batch_size=batch_size,
        epochs=epochs,
        verbose=verbose,
        callbacks=callbacks,
        validation_data=validation_data,
        shuffle=shuffle,
    )
    return hist_obj
