class Network:

    def __init__(self):
        self.layers = []
        self.loss = None
        self.loss_prime = None
        pass

    def add(self, layer):
        self.layers.append(layer)

    def setup_loss(self, loss, loss_prime):
        '''

        :param loss:
        :param loss_prime: hàm đọa hàm của loss funcition
        :return:
        '''
        self.loss = loss
        self.loss_prime = loss_prime

        pass

    def predict(self, input):
        '''

        :param input:  [[1,3]]->1
        :return: ket qua du doan
        '''
        n = len(input)
        result = []
        for i in range(n):
            output = input[i]
            for layer in self.layers:
                layer.forward_propagation(output)
            result.append(output)

        return result

    def fit(self, x_train, y_train, learning_rate, epochs):

        n = len(x_train)
        for j in range(epochs):
            for j in range(n):
                pass




