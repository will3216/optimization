from model_base import ModelBase
from numpy import zeros, array
from module1 import convert_string_to_number as safe_convert

class Table(ModelBase):
    #################################################################
    ##                         Desciption:                         ##
    #################################################################
    
    #################################################################
    ##                 Initialize class attributes                 ##
    #################################################################
    def __init__(self, parent, id, arg_list, dtype='float'):
        ModelBase.__init__(self, parent, id, arg_list[1], 'Table')
        self.domain = arg_list.pop(0)
        arg_list.pop(0)
        self.dtype = dtype
        arg_list.pop(0)
        self.raw_table = arg_list.pop()
        self.data = array([])
        return
    
    #################################################################
    ##                      Test Class Data:                       ##
    #################################################################
    def __test__(self):
        self.error_code = ''
        if not self.processed:
            # The first item in the raw_table list should be index labels from
            # the first domain in list form.
            rows = self.raw_table[0]
            cols = self.raw_table[1]
            table = self.raw_table[2]
            # Check that rows is a list
            if not type(rows) == type([]):
                self.error_code = self.error_code + '1'
            else:
                # Check that all of the row labels correspond to values in the 
                # domain of the row dimension
                temp_char = '0'
                for label in rows:
                    if label not in self.parent.set_values[self.domain[0]]:
                        temp_char = '2'
                        break
                self.error_code = self.error_code + temp_char

            # Check that cols is a list
            if not type(cols) == type([]):
                self.error_code = self.error_code + '1'
            else:
                # Check that all of the col labels correspond to values in the
                # domain of the col dimension
                temp_char = '0'
                for label in cols:
                    if label not in self.parent.set_values[self.domain[1]]:
                        temp_char = '2'
                        break
                self.error_code = self.error_code + temp_char

            # Check that raw_table is a list
            if not type(cols) == type([]):
                self.error_code = self.error_code + '1'
            else:
                # Check that every value in the table safely converts to a
                # to a numeric type.
                
                temp_char = '0'
                for i in table:
                    # Check that each row is a list
                    if not type(i) == type([]):
                        temp_char = '2'
                    for j in i:
                        try:
                            safe_convert(j)
                        except:
                            temp_char = '3'
                            print j
                            break
                        if temp_char == '3':
                            break
                self.error_code = self.error_code + temp_char
        else:
            # Check if the processed data is a numpy array
            try:
                if not type(self.data) == type(array([1, 1])):
                    self.error_code = self.error_code + '1'
                else:
                    self.error_code = self.error_code + '0'
                    if not self.data.dtype == array([], dtype=self.dtype).dtype:
                        self.error_code = self.error_code + '1'
                    else:
                        self.error_code = self.error_code + '0'
            except:
                self.error_code = self.error_code + '2'

            return
    #################################################################
    ##                     Process Class Data:                     ##
    #################################################################
    def __process__(self):
        # Create a new array filled with zeros with the shape of the domain
        try:
            rows = self.raw_table[0]
            cols = self.raw_table[1]
            table = self.raw_table[2]
            i_size = len(self.parent.set_values[self.domain[0]])
            j_size = len(self.parent.set_values[self.domain[1]])
            new_array = zeros((i_size, j_size), dtype=self.dtype)
            for first in range(len(table)):
                i_index = self.parent.set_values[self.domain[0]][rows[first]]
                for second in range(len(table[first])):
                    j_index = self.parent.set_values[self.domain[1]][cols[second]]
                    new_array[i_index, j_index] = table[first][second]
            self.data = new_array
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
        # Is there a description?
        if not self.descr == '':
        # format descr string
            str_descr = '"""' + self.descr + '"""\n'
        else:
            str_descr = ''
        end_str = "], dtype= '" + self.dtype + "')"
        lead_str = self.id + ' = array(['
        table = ''
        for i in range(len(self.data)):
            line = str(self.data[i]).replace(' ','',1).replace('  ',', ')
            table = table + line + ','
        table = table[:-1] + end_str
        #table = table.replace(' ',',')
        table = self.pretty_print(len(lead_str), table)
        
        table = lead_str + table
        return str_descr + table
    
    #################################################################
    ##                       Helper Functions                      ##
    #################################################################
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
4. String representation [x]



"""