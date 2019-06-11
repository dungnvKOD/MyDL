from .Layer import Layer
import numpy as np


class FCLayer(Layer):  # 2
    def __init__(self, input, input_shape, output_shape):
        '''
        :param input_shape: [1,3]
        :param output_shape:[1,4]
        '''

        self.input_shape = input_shape
        self.output_shape = output_shape
        self.weights = np.random.rand(self.input_shape[1], self.output_shape[1]) - 0.5
        self.biase = np.random.rand(1, output_shape[1]) - 0.5

    def forward_propagation(self, input):
        self.input = input
        self.output = np.dot(input, self.weights) + self.biase
        return self.output

    def backward_propagation(self, output_error, learning_rate):

        dweight = np.dot(self.input.T, output_error)

        self.weights -= dweight * learning_rate
        self.biase -= learning_rate * output_error

        curent_error = np.dot(output_error, self.weights) # tinh loi de tra ve cholop truoc
        return curent_error
