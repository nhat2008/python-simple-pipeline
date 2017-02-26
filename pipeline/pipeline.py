from pipe import Pipe
from utils import *


class Pipeline(object):
    all_functions = None

    def __init__(self, functions):
        self.all_functions = functions

    def _load_functions(self, name_functions):
        return loading(self.all_functions, name_functions)

    def __call__(self, name_functions, input_data):
        if not isinstance(name_functions, list):
            name_functions = [name_functions]
        pipe = Pipe(*self._load_functions(name_functions))
        return pipe(input_data)



