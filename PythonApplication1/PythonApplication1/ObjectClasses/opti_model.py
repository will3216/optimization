from model_base import ModelBase

class OptiModel(ModelBase):
    #################################################################
    ##                         Desciption:                         ##
    #################################################################


    #################################################################
    ##                 Initialize class attributes                 ##
    #################################################################
    def __init__(self, object_values_list, name, d_check=True):
        from equation import Equation
        from direct_assign import DirectAssign
        from variable import Variable
        from table import Table
        from set import Set
        from scalar import Scalar
        from parameter_list import ParameterList
        self.id = name
        self.domain_checking = d_check
        self.error_status = True
        self.processed = False
        self.error_code = ''
        self.error_list = []
        
        self.declared_parameters = []
        self.declared_variables = []
        self.declared_equations = []
        self.set_order = []
        self.set_values = {}
        self.objects = {}
        for item in object_values_list:
            if item[1] == 'Set':
                temp = {item[0]: Set(self, item[0], item[2])}
                self.declared_parameters.append(item[0])
                self.set_order.append(item[0])
                self.set_values.update({item[0]: dict(zip(item[2][1], 
                                                     range(len(item[2][1]))))})
            elif item[1] == 'Param List':
                temp = {item[0]: ParameterList(self, item[0], item[2])}
                self.declared_parameters.append(item[0])
            elif item[1] == 'Table':
                temp = {item[0]: Table(self, item[0], item[2])}
                self.declared_parameters.append(item[0])
                print temp[item[0]].__test__()
            elif item[1] == 'Scalar':
                temp = {item[0]: Scalar(self, item[0], item[2])}
                self.declared_parameters.append(item[0])
            elif item[1] == 'Param DA':
                temp = {item[0]: DirectAssign(self, item[0], item[2])}
                self.declared_parameters.append(item[0])
            elif item[1] == 'Variable':
                temp = {item[0]: Variable(self, item[0], item[2])}
                self.declared_variables.append(item[0])
            elif item[1] == 'Equation':
                temp = {item[0]: Equation(self, item[0], item[2])}
                self.declared_equations.append(item[0])
            self.objects.update(temp)
        return
    #################################################################
    ##                      Test Class Data:                       ##
    #################################################################
    def __test__(self):
        if not self.processed:
            # Check that id is a string
            try:
                if not type(self.id) == type(""):
                    self.error_code = self.error_code + '1'
                else:
                    self.error_code = self.error_code + '0'
            except:
                self.error_code = self.error_code + '2'

            # Check that id begins with a letter
            try:
                if not self.id[0].isalpha():
                    self.error_code = self.error_code + '1'
                else:
                    self.error_code = self.error_code + '0'
            except:
                self.error_code = self.error_code + '2'

            # Check that the id is alphanumeric
            try:
                if not self.id.isalnum():
                    self.error_code = self.error_code + '1'
                else:
                    self.error_code = self.error_code + '0'
            except:
                self.error_code = self.error_code + '2'

            # Check that this object has no errors before processing the rest
            if int(self.error_code) == 0:
                # Object type key for error code
                error_code_dict = {
                        'Set'       :'.1',
                        'Param List':'.2',
                        'Table'     :'.3',
                        'Scalar'    :'.4',
                        'Param DA'  :'.5',
                        'Variable'  :'.6',
                        'Equation'  :'.7',
                }
                # Run first round of tests on ModelBase classes
                for item in self.objects:
                    item.__test__()
                    error_msg = item.error_code 
                    error_msg = error_msg + error_code_dict[item.class_type] 
                    self.error_list.append(error_msg)
                # If the error list is empty, all tests were cleared.
                # Change error status to False
                if len(self.error_list) == 0:
                    self.error_code = '0'
                    self.error_status = False
                # Return an error
                else:
                    self.error_code = '1'
                    return self.error_code
            # Return an error.
            else:
                self.error_code = '2'
                return self.error_code
        else:
            pass
        return
    #################################################################
    ##                     Process Class Data:                     ##
    #################################################################

    #################################################################
    ##                   Print to Python Script:                   ##
    #################################################################

##############################################################################
##                               To do list:                                ##
##############################################################################
"""
1. Input Test
2. Data Processing
3. Post process test
4. Load redundant attributes from ModelBase


"""
