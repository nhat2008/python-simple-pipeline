import inspect


def loading(modules, names):
    all_functions = []
    if not isinstance(modules, list):
        modules = [modules]
    if not isinstance(names, list):
        names = [names]
    for module in modules:
        tmp_functions = [function for function in inspect.getmembers(module, inspect.isfunction) if
                         function[0] in names]
        all_functions += tmp_functions
    all_functions_mapping = dict(all_functions)
    functions = [all_functions_mapping[x] for x in names]
    return functions
