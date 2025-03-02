def build_model(input_shape):

# Define the input placeholder as a tensor with shape input_shape. X_input = Input(input_shape) # shape=(?, 240, 240, 3)
# Zero-Padding: pads the border of X_input with zeroes

X = ZeroPadding2D((2, 2))(X_input) # shape=(?, 244, 244, 3) # CONV -> BN -> RELU Block applied to X
X = Conv2D(32, (7, 7), strides = (1, 1), name = 'conv0')(X) X = BatchNormalization(axis = 3, name = 'bn0')(X)
X = Activation('relu')(X) # shape=(?, 238, 238, 32) # MAXPOOL
X = MaxPooling2D((4, 4), name='max_pool0')(X) # shape=(?, 59, 59, 32) # MAXPOOL
X = MaxPooling2D((4, 4), name='max_pool1')(X) # shape=(?, 14, 14, 32) # FLATTEN X
X = Flatten()(X) # shape=(?, 6272) # FULLYCONNECTED
X = Dense(1, activation='sigmoid', name='fc')(X) # shape=(?, 1) # Create model. This creates your Keras model instanc,.
model = Model(inputs = X_input, outputs = X, name='BrainDetectionModel') return model