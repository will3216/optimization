from model_base import ModelBase
from numpy import zeros, array

class ParameterList(ModelBase):
    object_type = 'ParameterList'
    #################################################################
    ##                 Initialize class attributes                 ##
    #################################################################
    def __init__(self, parent, id, arg_list, dtype='float'):
        ModelBase.__init__(self, parent, id, arg_list[1], 'Param List')
        self.domain = arg_list.pop(0)
        self.raw_list = arg_list[-1]
        self.dtype = dtype
        self.shape = []
        self.data = array([])
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

            # Check if the sets specified in the domain exist
            try:
                passed = True
                for i in self.domain:
                    if not i in parent.set_order:
                        passed = False
                if passed:
                    self.error_code = self.error_code + '0'
                else:
                    self.error_code = self.error_code + '1'
            except:
                self.error_code = self.error_code + '2'

            # Check that the raw list is formatted correctly
            try:
                dim_in_dom = len(self.domain)
                passed = True
                for item in self.raw_list:
                    if not len(item) == dim_in_domain + 1:
                        passed = False
                if not passed:
                    self.error_code = self.error_code + '1'
                else:
                    self.error_code = self.error_code + '0'
            except:
                self.error_code = self.error_code + '2'

            # Check that each item in the raw list belongs to its
            # respective domains.
            try:
                passed = True
                for set_index in range(len(self.domain)):
                    for item in self.raw_list:
                        set_indices = parent.set_values[self.domain[set_index]].keys()
                        if not item[set_index] in set_indices:
                            passed = False
                if not passed:
                    self.error_code = self.error_code + '1'
                else:
                    self.error_code = self.error_code + '0'
            except:
                self.error_code = self.error_code + '2'

            # Check that each value in the raw list is a number type
            try:
                passed = True
                for item in self.raw_list:
                    try:
                        float(item)
                    except:
                        passed = False
                if not passed:
                    self.error_code = self.error_code + '1'
                else:
                    self.error_code = self.error_code + '0'
            except:
                self.error_code = self.error_code + '2'
        else:
            # Check that self.data is a numpy array
            try:
                if type(self.data) == type(array([])):
                    self.error_code = self.error_code + '0'
                else:
                    self.error_code = self.error_code + '1'
            except:
                self.error_code = self.error_code + '2'

            # Check that the data type of the array is correct
            try:
                if self.data.dtype == array([], dtype=self.dtype):
                    self.error_code = self.error_code + '0'
                else:
                    self.error_code = self.error_code + '1'
            except:
                self.error_code = self.error_code + '2'

            # Check that the shape of the array is correct
            try:
                if self.data.shape == tuple(self.shape):
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
        #try:
        # Determine the shape of the data array
        for set in self.domain:
            set_indices = self.parent.set_values[set]
            self.shape.append(len(set_indices))
            
        # Build empty data array
        temp = zeros(self.shape, dtype=self.dtype)

        # Add values to empty data array
        self.data = self.process_raw_list(temp)

        # Toggle self.processed to True
        self.processed = True
        #except:
            #self.error_code = '99'
        return

    #################################################################
    ##                   Print to Python Script:                   ##
    #################################################################
    def __repr__(self):
        # Is there a description?
        if not self.descr == '':
        # format descr string
            str_descr = '"""' + self.descr + '"""\n'
        else:
            str_descr = ''
        # Make string that contains the variable name, and calls the numpy 
        # array creator. 
        str_array = self.id + ' = array('
        
        # Make string to hold addition array creator variables
        end_str = ', dtype=' + self.dtype + ')'

        # Convert self.data into a string
        data_str = self.process_data(self.data).replace('\n','').replace(' ',',')
        data_str = data_str + end_str
        
        # Make string not be crazy long
        data_str = self.pretty_print(len(str_array), data_str)
        
        # Add the definition to the declaration and close creator
        str_array = str_array + data_str

        # Return description and declaration/definition
        return str_descr + str_array

    #################################################################
    ##                       Helper Functions                      ##
    #################################################################
    # Convert self.raw_list to array
    def process_raw_list(self, empty_array):
        dom_len = len(self.domain)
        for item in self.raw_list:
            index = []
            for i in range(dom_len):
                key1 = self.domain[i]
                set_indices = self.parent.set_values[key1]
                key2 = item[i]
                set_index = set_indices[key2]
                index.append(set_index)
            if self.dtype == 'float':
                empty_array[index] = float(item[-1])
            elif self.dtype == 'int':
                empty_array[index] = int(item[-1])
            else:
                self.error_code = '98'
            
        return empty_array

    # Convert data to string
    def process_data(self, data):
        data_str = ''
        for i in range(len(data)):
            if len(data[i].shape) > 1:
                data_str = data_str + process_data(self, data[i]) + ',' 
            else:
                data_str = data_str + str(data[i]) + ','
        return '[' + data_str[:-1] + ']'

    # Make string conform to PEP8 (line length <= 79), could look nicer though
    def pretty_print(self, lead_space, input_str):
        pretty_str = ''
        ugly_str = input_str
        white_space = ''
        white_space_length = lead_space
        entry_length = 75 - white_space_length

        for i in range(white_space_length):
            white_space = white_space + ' '
        
        while len(ugly_str) > 0:
            if len(ugly_str) > entry_length:
                if len(pretty_str) == 0:
                    pretty_str = pretty_str + ugly_str[:entry_length]
                else:
                    pretty_str = white_space + pretty_str + ugly_str[:entry_length]
                pretty_str = pretty_str + '\n'
                ugly_str = ugly_str[entry_length:]
            else:
                if len(pretty_str) == 0:
                    pretty_str = pretty_str + ugly_str
                else:
                    pretty_str = pretty_str + white_space + ugly_str
                ugly_str = ''
            
        return pretty_str

##############################################################################
##                               To do list:                                ##
##############################################################################
"""
1. Input Test            [x]
2. Data Processing       [x]
3. Post process test     [x]
4. String Representation [x]



"""