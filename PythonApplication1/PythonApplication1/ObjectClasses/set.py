from model_base import ModelBase

class Set(ModelBase):
    #################################################################
    ##                         Desciption:                         ##
    #################################################################
    """description of class"""

    # To create a new object of this type, simply import the class into your
    # script, eg: from object_classes import Set
    # Then define for instance: i = Set("name", ["description", ['label1', 'label2', ...]])
    
    #################################################################
    ##                 Initialize class attributes                 ##
    #################################################################
    def __init__(self, parent, id, arg_list):
        ModelBase.__init__(self, parent, id, arg_list[0], 'Set')
        # The labels of the members of this Set
        self.labels = arg_list[1]
    
    # Use this function to determine if the attributes of this object are of 
    # the correct data type and format.
    #################################################################
    ##                      Test Class Data:                       ##
    #################################################################
    def __test__(self):
        if not self.processed:
            self.error_code = ''
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

            # Test the labels
            # Is the list of labels a list?
            if not type(self.labels) == type([]):
                label_code = '1'
            else:
                label_code = '0'
                for label in self.labels:
                    # Do each of the labels begin with a letter
                    if not label[0].isalpha():
                        label_code = '4'
                        break
                    # Are all of the labels strings?
                    if not type(label) == type(''):
                        label_code = '2'
                        break
                    # Are all of the labels alphanumeric?
                    elif not label.isalnum():
                        if '-' in label or '_' in label:
                            temp = ''.join(''.join(label.split('-')).split('_'))
                            if not temp.isalnum():
                                label_code = '3'
                                break
                        else:
                            label_code = '3'
                            break
            self.error_code = self.error_code + label_code
        else:
            pass
        return

    #################################################################
    ##                     Process Class Data:                     ##
    #################################################################
    def __process__(self):
        self.processed = True
        return
    #################################################################
    ##                   Print to Python Script:                   ##
    #################################################################
    # This function determines what happens when you use a print command on a 
    # Set object.
    def __repr__(self):
        label_str = ''
        label_line = ''
        for item in self.labels:
            if len(label_line) + len(item) >= 80:
                label_str = label_str + '\n' + label_line
                label_line = item
            else:
                if label_line == '':
                    label_line = item
                else:
                    label_line = label_line + ', ' + item
        if label_str == '':
            label_str = label_line
        else:
            label_str = label_str + '\n' + label_line

        return_str = '"""\n<Set Object>\nIdentifier = ' + self.id
        if not self.descr == '':
            return_str = return_str + "\nDescription = " + self.descr 
        return_str = return_str + "\nLabels:\n" + label_str + '\n"""'
        return return_str


##############################################################################
##                               To do list:                                ##
##############################################################################
"""
1.
2.



"""