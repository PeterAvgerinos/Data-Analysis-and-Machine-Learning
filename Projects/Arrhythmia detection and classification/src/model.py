import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv1D, MaxPooling1D, Flatten, Dense, Dropout
from tensorflow.keras.layers import LSTM

# CNN Model
def build_train_test_cnn_model(X_train, y_train, X_val, y_val, X_test, y_test, filters=32, kernel_size=3, pool_size=2,
                           dense_units=128, dropout_rate=0.5, epochs=10, batch_size=32):

    physical_devices = tf.config.list_physical_devices('GPU')
    if physical_devices:
        tf.config.experimental.set_memory_growth(physical_devices[0], True)
        print("GPU is available.")
    else:
        print("No GPU detected. Running on CPU.")

    model = Sequential()

    model.add(Conv1D(filters=filters, kernel_size=kernel_size, activation='relu', input_shape=(X_train.shape[1], 1)))
    model.add(MaxPooling1D(pool_size=pool_size))
    model.add(Conv1D(filters=filters*2, kernel_size=kernel_size, activation='relu'))
    model.add(MaxPooling1D(pool_size=pool_size))
    model.add(Flatten())
    model.add(Dense(dense_units, activation='relu'))
    model.add(Dropout(dropout_rate))
    model.add(Dense(1, activation='sigmoid'))

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size, validation_data=(X_val, y_val), verbose=0)

    _, val_accuracy = model.evaluate(X_val, y_val, verbose=0)

    _, test_accuracy = model.evaluate(X_test, y_test, verbose=0)

    return val_accuracy, test_accuracy

# RNN Model
def build_train_test_rnn_model(X_train, y_train, X_val, y_val, X_test, y_test, units=64, dropout_rate=0.5, epochs=10, batch_size=32):

    model = Sequential()

    model.add(LSTM(units=units, input_shape=(X_train.shape[1], 1)))
    model.add(Dropout(dropout_rate))
    model.add(Dense(1, activation='sigmoid'))

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size, validation_data=(X_val, y_val), verbose=0)

    _, val_accuracy = model.evaluate(X_val, y_val, verbose=0)

    _, test_accuracy = model.evaluate(X_test, y_test, verbose=0)

    return val_accuracy, test_accuracy

