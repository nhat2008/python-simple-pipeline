class Pipe(object):
    def __init__(self, *args):
        self.functions = args
        self.state = {'error': '', 'result': None}

    def __call__(self, value):
        if not value:
            raise "Not any value for running"
        self.state['result'] = self.data_pipe(value)
        return self.state

    def _bind(self, value, function):
        try:
            if value:
                return function(value)
            else:
                return None
        except Exception as e:
            self.state['error'] = e

    def data_pipe(self, value):
        c_value = value
        for function in self.functions:
            c_value = self._bind(c_value, function)
        return c_value
