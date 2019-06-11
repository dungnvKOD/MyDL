from .Layer import Layer


class ActivationLayer(Layer):

    def __init__(self, input_shape, output_sahpe, activation, activation_prime):
        '''

        :param input_shape: đầu vào input (1,4)
        :param output_sahpe: mảng
        :param activation: hàm
        :param activation_prime: hàm
        '''

        self.input_shape = input_shape
        self.output_shape = output_sahpe
        self.activation = activation
        self.activation_prime = activation_prime

    def forward_propagation(self, input):
        self.input = input
        self.output = self.activation(input)

        return self.output

    def backward_propagation(self, output_error, learning_rate):
        return self.activation_prime(self.input)*output_error

