class Layer: # 1
    def __init__(self):
        self.input = None
        self.output = None
        self.input_shape = None  # kich thuoc layer
        self.output_shape = None
        raise NotImplementedError

    @abs
    def input(self):
        return self.input

    @abs
    def output(self):
        return self.output

    @abs
    def input_shape(self):
        return self.input_shape

    @abs
    def output_shape(self):
        return self.output_shape

    @abs
    def forward_propagation(self, input):
        '''
        :param input:  lan truyen tien can nhan vao input cuar layer truoc do
        :return:
        '''
        raise NotImplementedError

    @abs
    def backward_propagation(self,output_error,learning_rate):
        '''
        E =E0.W0.R(Za)
        :param output: cua layer sau no
        :param learning_rate:
        :return:
        '''
        raise NotImplementedError

