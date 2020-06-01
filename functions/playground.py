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

