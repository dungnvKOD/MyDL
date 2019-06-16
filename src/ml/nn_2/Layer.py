class Layer:
    def __init__(self):
        self.input = None
        self.output = None
        self.input_shape = None
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
    def forward_propagation(self,input):
        '''

        :param input: lan truyen tien nhan vao input cua layer truoc
        :return:

        '''
        raise NotImplementedError

    @abs
    def backward_propagation(self,output_error,learning_rate):
        '''

        :param output_error: loi cua layer sau no
        :param learning_rate:
        :return:
        '''
        raise NotImplementedError
    