from model_base import ModelBase
from numpy import zeros

class Variable(ModelBase):
    #################################################################
    ##                         Desciption:                         ##
    #################################################################

    VariableKeys = ('Free', 'Positive', 'Negative', 'Binary', 
                    'Integer')
    #################################################################
    ##                 Initialize class attributes                 ##
    #################################################################
    def __init__(self, parent, id, arg_list, dtype='float'):
        ModelBase.__init__(self, parent, id, arg_list[1], 'Variable')
        self.domain = arg_list.pop(0)
        arg_list.pop(0)
        self.variable_type = arg_list.pop()
        self.upper_bound = 10**30
        self.lower_bound = -10**30
        self.dtype = dtype
        return
    #################################################################
    ##                      Test Class Data:                       ##
    #################################################################
    def __test__(self):
        if not self.processed == True:
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

            # Check that the variable type is specified correctly
            try:
                if not self.variable_type in VariableKeys:
                    self.error_code = self.error_code + '1'
                else:
                    self.error_code = self.error_code + '0'
            except:
                self.error_code = self.error_code + '2'
        else:

            try:
                if type(self.data) == type(2) or type(self.data) == type(2.0):
                    self.error_code = self.error_code + '0'
                else:
                    self.error_code = self.error_code + '1'
                
            except:
                self.error_code = self.error_code + '2'
                    
        return 
    #################################################################
    ##                     Process Class Data:                     ##
    #################################################################
    def __process__(self):
        try:
            if self.dtype == 'float':
                shape_holder = []
                for set in self.domain:
                    temp = len(self.parent.set_values[set])
                    shape_holder.append(temp)
                self.shape = tuple(shape_holder)
                self.data = zeros(self.shape, dtype=self.dtype)
            else:
                self.data = 0
            self.processed = True
        except:
            self.error_code = '99'
            raise
        self.error_status = True
        return 
    #################################################################
    ##                   Print to Python Script:                   ##
    #################################################################
    def __repr__(self):
        _id = self.id + ' = Array(['
        _shape = 'shape=' + str(self.shape) + ', '
        _type = "dtype='" + self.dtype + "', "
        _io = "iotype='in', "
        _de = "desc='" + self.descr + "'])\n"
        prnt_stmt = _id + _shape + _type + _io + _de
        return prnt_stmt
        


##############################################################################
##                               To do list:                                ##
##############################################################################
"""
1. Input Test            [x]
2. Data Processing       [x]
3. Post process test     [x]
4. String Representation [x]



"""

