class ModelBase(object):
    #################################################################
    ##                         Desciption:                         ##
    #################################################################
    """description of class"""
    #################################################################
    ##                 Initialize class attributes                 ##
    #################################################################
    def __init__(self, parent, identifier, description, type):
        self.parent = parent
        self.id = identifier
        self.descr = description
        self.processed = False
        self.error_status = True
        self.error_code = ''
        self.class_type = type
        return
