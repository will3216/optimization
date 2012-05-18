


import os
from gams_to_python import input as namespace_input
from custom_np_fxns import test
from opti_model import OptiModel
from temp_fxn_builder import test, test_set


object_list, solve_block = namespace_input('Inputfile.txt')
for item in object_list:
    print item 
model = OptiModel(object_list, 'test')
var = 'cost'
print model.objects[var].declared_variables
print model.objects[var].declared_parameters
print model.objects[var].declared_equations
model.objects[var].__test__()
model.objects[var].__process__()
print model.objects[var].error_code
print model.objects[var].error_status
print model.objects[var].processed
#print model.objects[var].data
#print type(model.objects[var].data)
#print model.objects[var]

















def find_dependencies(eq_str):
    dependency_list =[]
    temp_str = ''

    for char in eq_str:
        if char.isalpha():
            temp_str = ''.join([temp_str, char])
        elif not temp_str == '':
            if char.isdigit():
                temp_str = ''.join([temp_str, char])
            else:
                if not temp_str in dependency_list:
                    dependency_list.append(temp_str)
                temp_str = ''

    if not temp_str == '':
        dependency_list.append(temp_str)

    return dependency_list

test_str = 'sum(j, x(i,j)) =l= a(i)'










test(test_set)



#print process_eqn_ls(eqns, input)

