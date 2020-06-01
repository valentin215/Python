# Functions

def global_scope():

    test_variable_outside_scope = 'global scope'
    print(test_variable_outside_scope)

    def test_function():
        test_variable_outside_scope = 'inside function'
        print(test_variable_outside_scope)
        return test_variable_outside_scope

    def test_function_non_local():
        nonlocal test_variable_outside_scope
        test_variable_outside_scope = 'non local'
        print(test_variable_outside_scope)
        return test_variable_outside_scope

    def test_function_global():
        global test_variable_outside_scope
        test_variable_outside_scope = 'think global'
        print(test_variable_outside_scope)
        return test_variable_outside_scope

    test_function()
    test_function_non_local()
    test_function_global()
    print(test_variable_outside_scope)
    
global_scope()


def power_of(number, power=2):
    return number ** power

def function_test_arguments(params, *args):
    print(params)
    print(args)

function_test_arguments('one', 'test', 'second_test')