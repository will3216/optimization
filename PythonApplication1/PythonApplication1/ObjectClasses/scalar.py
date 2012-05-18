from model_base import ModelBase
from module1 import convert_string_to_number as safe_convert
from numpy import array

class Scalar(ModelBase):
    #################################################################
    ##                         Desciption:                         ##
    #################################################################


    #################################################################
    ##                 Initialize class attributes                 ##
    #################################################################
    def __init__(self, parent, id, arg_list, dtype=float):
        ModelBase.__init__(self, parent, id, arg_list[0], type)
        arg_list.pop(0)
        [self.raw_value] = arg_list.pop(0)
        self.dtype = dtype
        self.data = None
        return
    #################################################################
    ##                      Test Class Data:                       ##
    #################################################################
    def __test__(self):
        if not self.processed:
            self.error_code = ''
            # Check that self.raw_value converts to a numeric type
            self.error_code = '0'
            try:
                safe_convert(self.raw_value)
            except:
                self.error_code = '1'
        else:
            self.error_code = ''
            try:
                self.data.dtype
                self.error_code = self.error_code = '0'
            except:
                self.error_code = self.error_code +'1'
        return

    #################################################################
    ##                     Process Class Data:                     ##
    #################################################################
    def __process__(self):
        try:
            self.data = array(safe_convert(self.raw_value), dtype=self.dtype)
            self.processed = True
        except:
            self.error_code = '99'
        self.error_status = True
        return 
    #################################################################
    ##                   Print to Python Script:                   ##
    #################################################################
    def __repr__(self):
        id = str(self.id)
        val_h = '# Scalar parameter ' + id + '\n'
        descr = '# ' + str(self.descr) + '\n'
        mid = ' = array('
        val = str(self.data) + ')'
        pr_stmt = val_h + descr + id + mid + val
        pr_stmt = id + mid + val
        return pr_stmt



##############################################################################
##                               To do list:                                ##
##############################################################################
"""
1.
2.



"""


