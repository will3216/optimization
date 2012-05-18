from base_equation import BaseEquation

class Equation(BaseEquation):
    #################################################################
    ##                         Desciption:                         ##
    #################################################################
    
    #################################################################
    ##                 Initialize class attributes                 ##
    #################################################################
    def __init__(self, parent, id, args):
        BaseEquation.__init__(self, parent, id, args, 'Equation')
        return
    #################################################################
    ##                      Test Class Data:                       ##
    #################################################################
    def __test__(self):
        if not self.processed:
            self.processed = True
            pass
        else:
            pass
    #################################################################
    ##                     Process Class Data:                     ##
    #################################################################
    def __process__(self):
        try:
            pass
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
        pass


##############################################################################
##                               To do list:                                ##
##############################################################################
"""
1. Input Test
2. Data Processing
3. Post process test



"""