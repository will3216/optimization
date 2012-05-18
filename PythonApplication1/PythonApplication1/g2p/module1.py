"###############################################################"#############
"####_     ######     _######## ______ #######_   ___ ##########"#####    ####
"#####   _  ####  _   #######  _######_  ######   ###__ ########"####__   ####
"#####   #_  ##  _#   ######  _########_  #####   #####_  ######"######   ####
"#####   ##_    _##   #####_  ##########  _####   ######   #####"######   ####
"#####   ###_  _###   ######_  ########  _#####   ######  _#####"######   ####
"#####   ####__####   #######__  ####   _######   #### ___######"######   ####
"####_____########_____########________#######_________#########"###________##
"###############################################################"#############
###                                                                        ###
###                                                                        ###
###           MODULE 1:                                                    ###
###                Everything you need to convert GAMS data as text        ###
###            into a python data or your money back!                      ###
###                                                                        ###
###                                                                        ###
##############################################################################
##############################################################################
##                             William Bryant                               ##
##                      Tabu Search Software Project                        ##
##                         Camarda Research Group                           ##
##                          University of Kansas                            ##
##############################################################################
## DESCRIPTION:                                                             ##
##                                                                          ##
##      This  module was created in order to provide conversion  functions  ##
##  for converting GAMS submission information into python code. Currently  ##
##  this  code is only  useful for constructing  python data from the text  ##
##  input,  however,  soon   additional  functions  will  be  created  for  ##
##  transcription of these python structures into python code, or  perhaps  ##
##  the  python data will  just be passed into the solve portion, I am not  ##
##  sure yet.                                                               ##
##                                                                          ##
##############################################################################














"############################################################################"
">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
"                                  FUNCTIONS                                 "
">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
"############################################################################"


"""
##############################################################################
" NAME: TEMPLATE"
#=============================================================================
# DESCRIPTION: description of function
# STATUS: Working, In Progress, Broken, etc.
#=============================================================================
# EXAMPLE INPUT AND OUTPUT:
# Given: <sample input>
# Returns: <sample output>
#=============================================================================
# CODE:
# def function(args*):...
##############################################################################
"""



##############################################################################
" NAME: convert_string_to_number(string)"
#=============================================================================
# DESCRIPTION: Converts string which contains a number and decides
# which string conversion function to use to convert it, returning
# the number.
# STATUS: Working
#=============================================================================
# EXAMPLE INPUT AND OUTPUT:
# Given: "3.145"
# Returns: 3.145
# Given: "19"
# Returns: 19
#=============================================================================
# CODE:
def convert_string_to_number(string):
 	#Convert string to either int or float.
 	try:
 		ret = int(string)
 	except ValueError:
 		#Try float.
 		ret = float(string)
 	return ret
##############################################################################



##############################################################################
" NAME: minimize_white_space(string, comma = False)"
#=============================================================================
# DESCRIPTION: Converts string containing terms to be separated
# by white-space and reduces that white-space produced by \t, \n,
# and multiple spaces to a single space between each term.
# STATUS: Working
#=============================================================================
# EXAMPLE INPUT AND OUTPUT:
# Given: """ Parameters
# a(i)    capacity of plant i in cases
#         / Seattle   350
#           San-Diego 600 /
# b(j) 	demand at market j in cases
#         / New-York  325
#           Chicago   300
#           Topeka    275 / ; """
# Returns: "Parameters a(i) capacity of plant i in cases / Seattle 
#       350 San-Diego 600 / b(j) demand at market j in cases /  
#       New-York 325 Chicago 300 Topeka 275 / ;"
#=============================================================================
# CODE:
def minimize_white_space(string1, comma = False):
    if comma == False:
        temp1 = string1.lstrip().rstrip().replace("\n"," ")
        temp1 = temp1.replace("\t"," ").replace(","," ")
        test = False
    
        while test == False:
            temp2 = temp1.replace("  ", " ")
        
            if temp1 == temp2:
                test = True
                return temp2
            temp1 = temp2
    else:
        temp1 = string1.lstrip().rstrip().replace("\n"," ").replace("\t"," ")
        test = False
    
        while test == False:
            temp2 = temp1.replace("  ", " ")
        
            if temp1 == temp2:
                test = True
                return temp2
            temp1 = temp2
        
##############################################################################



##############################################################################
" NAME: split_block_into_dec_def_pairs(string)"
#=============================================================================
# DESCRIPTION: Converts a string containing single or multiple 
# pairs of declarations and definitions.
# STATUS: Working
#=============================================================================
# EXAMPLE INPUT AND OUTPUT:
# Given: """ Parameters
# a(i)    capacity of plant i in cases
#         / Seattle   350
#           San-Diego 600 /
# b(j) 	demand at market j in cases
#         / New-York  325
#           Chicago   300
#           Topeka    275 / ; """
# Returns: [['Parameters a(i) capacity of plant i in cases ', 
#   ' b(j) demand at market j in cases '], 
#       [' Seattle 350 San-Diego 600 ', 
#           ' New-York 325 Chicago 300 Topeka 275 ']]
#=============================================================================
# CODE:
def split_block_into_dec_def_pairs(block):
    # Works for: Sets, Parameter Lists
    # Split block at "/"s
    block_segments = block.split("/")


    first_portion  = [] # Contains set identifier(s) and 
                        #   description(s)
    second_portion = [] # Contains the list(s) of set elements

    # While loop to separate into parts
    while len(block_segments) > 0:

        # In case of trailing white space at end of statement
        if len(block_segments) == 1:
            break

        first_portion.append(block_segments.pop(0))
        second_portion.append(block_segments.pop(0))

    return first_portion, second_portion
##############################################################################



##############################################################################
" NAME: separate_identifier_from_description(list(strings))"
#=============================================================================
# DESCRIPTION: Converts a list of strings, each string is of the 
# form -- '<white-space><id><white-space><description><white-space>'
# into two lists. The first list contains all the ids the second
# the descriptions.
# STATUS: Working
#=============================================================================
# EXAMPLE INPUT AND OUTPUT:
# Given: ['Parameters a(i) capacity of plant i in cases ', 
#   ' b(j) demand at market j in cases ']
# Returns: (['a(i)', 'b(j)'], ['capacity of plant i in cases', 
#   'demand at market j in cases'])
#=============================================================================
# CODE:
def separate_identifier_from_description(list_of_first_portions):
    identifiers  = [] # Contains set identifier(s)
    descriptions = [] # Contains set description(s)

    # for loop to separate identifiers from descriptions within
    #   first_portion terms
    for groups in list_of_first_portions:

        # first_portion split terms at whitespace
        terms = clean_split(groups, True)

        stmnt_ids = ("Set","Parameter", "Scalar", "Table")
        # remove statement identifier "Set(s)" or Null if present
        if terms[0].startswith(stmnt_ids) or len(terms[0]) == 0:
            terms.pop(0)

        identifiers.append(terms.pop(0))
        descriptions.append(" ".join(terms))
    return identifiers, descriptions
##############################################################################



##############################################################################
" NAME: transform_list_into_couples(string)"
#=============================================================================
# DESCRIPTION: Converts a list containing unpartitioned pairs into
# a list of pairs, where there pairs are in tuples.
# STATUS: Working
#=============================================================================
# EXAMPLE INPUT AND OUTPUT:
# Given: ['Seattle', '350', 'San-Diego', '600']
# Returns: [('Seattle', '350'), ('San-Diego', '600')]
#=============================================================================
# CODE:
def transform_list_into_couples(data_list):
    flat_list = data_list
    
    couples = []
        
    while len(flat_list) > 0:
        first = flat_list.pop(0)

        if len(flat_list) == 0:
            return couples

        second = flat_list.pop(0)

        couple = (first, second)

        couples.append(couple)

        if len(flat_list) == 0:
            return couples
##############################################################################



##############################################################################
" NAME: transform_list_into_triples(string)"
#=============================================================================
# DESCRIPTION: Converts a list containing unpartitioned trios into
# a list of trios, where their trios are in tuples.
# STATUS: Working
#=============================================================================
# EXAMPLE INPUT AND OUTPUT:
# Given: ['Seattle', 'Whoop', '350', 'San-Diego', 'Da-Whoop', '600']
# Returns: [('Seattle', 'Whoop', '350'), ('San-Diego', 'Da-Whoop', '600')]
#=============================================================================
# CODE:
def transform_list_into_triples(data_list):
    flat_list = data_list
    
    triples = []
        
    while len(flat_list) > 0:
        first = flat_list.pop(0)

        if len(flat_list) == 0:
            return triples

        second = flat_list.pop(0)

        if len(flat_list) == 0:
            return triples

        third = flat_list.pop(0)

        triple = (first, second, third)

        triples.append(triple)

        if len(flat_list) == 0:
            return triples
##############################################################################



##############################################################################
" NAME: transform_list_into_quadruples(string)"
#=============================================================================
# DESCRIPTION: Converts a list containing unpartitioned quads into
# a list of quads, where their quads are in quadruples.
# STATUS: Working
#=============================================================================
# EXAMPLE INPUT AND OUTPUT:
# Given: ['Now', 'sit', 'down', 'please', 'I', 'am', 'talking', 'bro']
# Returns: [('Now', 'sit', 'down', 'please'), ('I', 'am', 'talking', 'bro')]
#=============================================================================
# CODE:
def transform_list_into_quadruples(data_list):
    flat_list = data_list
    
    quadruples = []
        
    while len(flat_list) > 0:
        first = flat_list.pop(0)

        if len(flat_list) == 0:
            return quadruples

        second = flat_list.pop(0)

        if len(flat_list) == 0:
            return quadruples

        third = flat_list.pop(0)

        if len(flat_list) == 0:
            return quadruples

        forth = flat_list.pop(0)

        quadruple = (first, second, third, forth)

        quadruples.append(quadruple)

        if len(flat_list) == 0:
            return quadruples
##############################################################################



##############################################################################
" NAME: transform_list_into_quintuples(string)"
#=============================================================================
# DESCRIPTION: Converts a list containing unpartitioned quints into
# a list of quints, where their quints are in quintuples.
# STATUS: Working
#=============================================================================
# EXAMPLE INPUT AND OUTPUT:
# Given: ['a', 'b', 'c', 'd', 'e', '1', '2', '3', '4', '5']
# Returns: [('a', 'b', 'c', 'd', 'e'), ('1', '2', '3', '4', '5')]
#=============================================================================
# CODE:
def transform_list_into_quintuples(data_list):
    flat_list = data_list
    
    quintuples = []
        
    while len(flat_list) > 0:
        first = flat_list.pop(0)

        if len(flat_list) == 0:
            return quintuples

        second = flat_list.pop(0)

        if len(flat_list) == 0:
            return quintuples

        third = flat_list.pop(0)

        if len(flat_list) == 0:
            return quintuples

        forth = flat_list.pop(0)

        if len(flat_list) == 0:
            return quintuples

        fifth = flat_list.pop(0)

        quintuple = (first, second, third, forth, fifth)

        quintuples.append(quintuple)

        if len(flat_list) == 0:
            return quintuples
##############################################################################



##############################################################################
" NAME: clean_split(string, comma = False)"
#=============================================================================
# DESCRIPTION: Converts string containing terms to be separated
# by white-space, indentations, commas, or new lines into a
# list of lists containing the partitioned terms without the 
# separators.
# STATUS: Working
#=============================================================================
# EXAMPLE INPUT AND OUTPUT:
# Given: ' Seattle\n 350 San-Diego \t600 '
# Returns: ['Seattle', '350', 'San-Diego', '600']
#=============================================================================
# CODE:
def clean_split(dirty_string, comma = False):
    clean_string = minimize_white_space(dirty_string, comma)
    return clean_string.split(" ")
##############################################################################



##############################################################################
" NAME: clean_split_on_list_of_strings(list(strings), comma = False)"
#=============================================================================
# DESCRIPTION: Converts a list of strings containing terms to be 
# separated by white-space, indentations, commas, or new lines 
# into a list of lists containing the partitioned terms without
# the separators.
# STATUS: Working
#=============================================================================
# EXAMPLE INPUT AND OUTPUT:
# Given: [' Seattle 350 San-Diego 600 ', 
#   ' New-York 325 Chicago 300 Topeka 275 ']
# Returns: [['Seattle', '350', 'San-Diego', '600'], 
#   ['New-York', '325', 'Chicago', '300', 'Topeka', '275']]
#=============================================================================
# CODE:
def clean_split_on_list_of_strings(list_of_strings, comma = False):
    dirty_list = list_of_strings
    clean_list = []

    if comma == False:
        for string in dirty_list:
            clean_list.append(clean_split(string))
    else:
        for string in dirty_list:
            clean_list.append(clean_split(string, True))
    return clean_list
##############################################################################



##############################################################################
" NAME: convert_flat_pair_lists(list(strings))"
#=============================================================================
# DESCRIPTION: Converts a list of strings containing unpartitioned 
# pairs into a list of lists containing, in this case, key value 
# pairs as tuples.
# STATUS: Working
#=============================================================================
# EXAMPLE INPUT AND OUTPUT:
# Given: [' Seattle 350 San-Diego 600 ', 
#   ' New-York 325 Chicago 300 Topeka 275 ']
# Returns: [[('Seattle', '350'), ('San-Diego', '600')], 
#   [('New-York', '325'), ('Chicago', '300'), ('Topeka', '275')]]
#=============================================================================
# CODE:
def convert_flat_pair_lists(list_of_data_entries):
    

    pair_list = []
    for string in list_of_data_entries:
        list_from_string = clean_split(string)
        key_value_pair_list = transform_list_into_couples(list_from_string)
        pair_list.append(key_value_pair_list)

    return pair_list
##############################################################################



##############################################################################
" NAME: split_clean_and_test_ids(identifiers, DeclaredIdentifiers)"
#=============================================================================
# DESCRIPTION: Converts a list of strings containing unpartitioned 
# pairs into a list of lists containing, in this case, key value 
# pairs as tuples.
# STATUS: Working
#=============================================================================
# EXAMPLE INPUT AND OUTPUT:
# Given: ['a(i)', 'b(j)', 'p'], ['i', 'm', 's']
# Returns: [['a', 'b', 'p'], [['i'], ['j'], []], [True, False, True]]
#=============================================================================
# CODE:
def split_clean_and_test_ids(identifiers, DeclaredIdentifiers): 
    ids = []
    doms = []
    tests = []
    for identifier in identifiers:
        if ")" in identifier:
            id, domain, test = process_identifier(identifier, 
                                                  DeclaredIdentifiers)
             
            ids.append(id)
            doms.append(domain)
            tests.append(test)

        else:
            ids.append(minimize_white_space(identifier))
            doms.append([])
            tests.append(True) 

    return ids, doms, tests
##############################################################################



##############################################################################
" NAME: process_identifier(string, DeclaredIdentifiers)"
#=============================================================================
# DESCRIPTION: Converts a string, containing an identifier and a 
# domain, by splitting it into its parts, then testing if the  
# domains that are specified with the indentifier have been
# declared. 
# STATUS: Working
#=============================================================================
# EXAMPLE INPUT AND OUTPUT:
# Given: "a( i, j  )", ["i","j"]
# Returns: ('a', ['i', 'j'], True)
# Given: "  a   ( i, m  )", ["i","j"]
# Returns: ('a', ['i', 'm'], False)
#=============================================================================
# CODE:
def process_identifier(identifier, DeclaredIdentifiers):
    
    temp = minimize_white_space(identifier)  
    id_comma_domains = "".join(temp.split(")")).split("(")
    id = minimize_white_space(id_comma_domains.pop(0))
    
    domains = clean_split(id_comma_domains.pop(0))

    for domain in domains:
        contained = domain in DeclaredIdentifiers
        if contained == False:
            return id, domains, False
    return id, domains, True
##############################################################################



##############################################################################
" NAME: list_length_check(list_of_lists)"
#=============================================================================
# DESCRIPTION: Checks to see if each list in a list of lists has the same 
# length
# STATUS: Working
#=============================================================================
# EXAMPLE INPUT AND OUTPUT:
# Given: [['a', 'b'], [['i'], ['j']], [True, True], [('Seattle', '350'), 
#   ('San-Diego', '600')]]
# Returns: True
# Given: [['a', 'b' , 'c'], [['i'], ['j']]]
# Returns: False
#=============================================================================
# CODE:
def list_length_check(list_of_lists):
    temp2 = -1
    for lst in list_of_lists:
        temp1 = len(lst)
        if temp2 == -1:
            pass
        elif not (temp1 == temp2): 
            return False
        temp2 = temp1
    return True
##############################################################################



##############################################################################
" NAME: compile_parameter_lists(ids, doms, descr, dom_tests, lst_of_kv_lsts)"
#=============================================================================
# DESCRIPTION: Converts several lists of parameter attributes into a list of
# quadruples each containing the attributes of a parameter.
# STATUS: Works
#=============================================================================
# EXAMPLE INPUT AND OUTPUT:
# Given: ['a', 'b'], [['i'], ['j']], 
#        ['capacity of plant i in cases', "demand at market j in cases"], 
#        [True, True], [[('Seattle', '350'), ('San-Diego', '600')], 
#                       [('New-York', '325'), ('Chicago', '300'), 
#                           ('Topeka', '275')]]
# Returns: [('a', ['i'], 'capacity of plant i in cases', True, 
#               [('Seattle', '350'), ('San-Diego', '600')]), 
#          ('b', ['j'], 'demand at market j in cases', True, 
#               [('New-York', '325'), ('Chicago', '300'), ('Topeka', '275')])]
#=============================================================================
# CODE:
def compile_parameter_lists(ids, doms, descr, dom_tests, lst_of_kv_lsts):
    parameters = []
    for i in range(len(ids)):
        parameter = [ids[i], doms[i], descr[i], dom_tests[i], 
                     lst_of_kv_lsts[i]]
        parameters.append(parameter)
    return parameters
##############################################################################



##############################################################################
" NAME: compile_data(id, type, data)"
#=============================================================================
# DESCRIPTION: Converts several lists of parameter attributes into a list of
# quadruples each containing the attributes of a parameter.
# STATUS: Works
#=============================================================================
# EXAMPLE INPUT AND OUTPUT:
# Given: ['a', 'b'], [['i'], ['j']], 
#        ['capacity of plant i in cases', "demand at market j in cases"], 
#        [True, True], [[('Seattle', '350'), ('San-Diego', '600')], 
#                       [('New-York', '325'), ('Chicago', '300'), 
#                           ('Topeka', '275')]]
# Returns: [('a', ['i'], 'capacity of plant i in cases', True, 
#               [('Seattle', '350'), ('San-Diego', '600')]), 
#          ('b', ['j'], 'demand at market j in cases', True, 
#               [('New-York', '325'), ('Chicago', '300'), ('Topeka', '275')])]
#=============================================================================
# CODE:
def compile_data(ids, type, data):
    data = []
    for i in range(len(ids)):
        datum = (ids[i], type[i], data[i])
        data.append(datum)
    return data
##############################################################################



##############################################################################
" NAME: compile_variable_lists(ids, doms, descr, dom_tests)"
#=============================================================================
# DESCRIPTION: Converts several lists of parameter attributes into a list of
# quadruples each containing the attributes of a parameter.
# STATUS: Works
#=============================================================================
# EXAMPLE INPUT AND OUTPUT:
# Given: ['a', 'b'], [['i'], ['j']], 
#        ['capacity of plant i in cases', "demand at market j in cases"], 
#        [True, True], [[('Seattle', '350'), ('San-Diego', '600')], 
#                       [('New-York', '325'), ('Chicago', '300'), 
#                           ('Topeka', '275')]]
# Returns: [('a', ['i'], 'capacity of plant i in cases', True, 
#               [('Seattle', '350'), ('San-Diego', '600')]), 
#          ('b', ['j'], 'demand at market j in cases', True, 
#               [('New-York', '325'), ('Chicago', '300'), ('Topeka', '275')])]
#=============================================================================
# CODE:
def compile_variable_lists(ids, doms, descr, dom_tests):
    parameters = []
    for i in range(len(ids)):
        parameter = [ids[i], doms[i], descr[i], dom_tests[i]]
        parameters.append(parameter)
    return parameters
##############################################################################



##############################################################################
" NAME: compile_set_lists(ids, descr, members)"
#=============================================================================
# DESCRIPTION: Converts several lists of set attributes into a list of
# triples each containing the attributes of a set.
# STATUS: Unknown
#=============================================================================
# EXAMPLE INPUT AND OUTPUT:
# Given: [['a', 'b'], [['i'], ['j']], [True, True], [[('Seattle', '350'), 
#   ('San-Diego', '600')], [('New-York', '325'), ('Chicago', '300'), 
#       ('Topeka', '275')]]]
# Returns: [('a', ['i'], True, [('Seattle', '350'), ('San-Diego', '600')]), 
#   ('b', ['j'], True, [('New-York', '325'), ('Chicago', '300'), 
#       ('Topeka', '275')])]
#=============================================================================
# CODE:
def compile_set_lists(ids, descr, members):
    sets = []
    for i in range(len(ids)):
        set = [ids[i], descr[i], members[i]]
        sets.append(set)
    return sets
##############################################################################



##############################################################################
" NAME: convert_raw_list_data_to_n_tuple_list(doms, data_portion)"
#=============================================================================
# DESCRIPTION: Converts a list of the data for each parameter into a list of 
# n-tuples, where n is equal to the size of the domain of a given parameter
# plus one, this list is then compiled into a master list.
# STATUS: []Working, [X]In Progress, []Broken
#=============================================================================
# EXAMPLE INPUT AND OUTPUT:
# Given: [['i'], ['i', 'j'], ['i', 'j', 'k'], ['i', 'j', 'k', 'l']],
#        ["a 1 b 2 c 3", "a 1 cab b 2 jeez", "a b c d 4 3 2 1", 
#         "a b c d e 1 2 3 4 5"]        
# Returns: [[('a', '1'), ('b', '2'), ('c', '3')], 
#           [('a', '1', 'cab'), ('b', '2', 'jeez')], 
#           [('a', 'b', 'c', 'd'), ('4', '3', '2', '1')], 
#           [('a', 'b', 'c', 'd', 'e'), ('1', '2', '3', '4', '5')]]
#=============================================================================
# CODE:
def convert_raw_list_data_to_n_tuple_list(doms, data_portion):
    keyvalue_lists = []

    for i in range(len(doms)):
        raw_data = clean_split(data_portion[i])
        if len(doms[i]) == 1:
            keyvalue_lists.append(transform_list_into_couples(raw_data))
        elif len(doms[i]) == 2:
            keyvalue_lists.append(transform_list_into_triples(raw_data))
        elif len(doms[i]) == 3:
            keyvalue_lists.append(transform_list_into_quadruples(raw_data))
        elif len(doms[i]) == 4:
            keyvalue_lists.append(transform_list_into_quintuples(raw_data))
    return keyvalue_lists
##############################################################################



##############################################################################
" NAME: find_the_iteration_range(string1, string2)"
#=============================================================================
# DESCRIPTION: Function to determine terminal subsequences of digits of a 
# pair of strings
# STATUS: Working
#=============================================================================
# EXAMPLE INPUT AND OUTPUT:
# Given: "wiggle1", "wiggle12"
# Returns: ('1', '12')
#=============================================================================
# CODE:
def find_the_iteration_range(string1, string2):
    temp1 = string1
    temp2 = string2
    while not (temp1.isdigit() or temp2.isdigit()):
        _temp1 = list(temp1)
        _temp2 = list(temp2)
        _temp1.pop(0)
        _temp2.pop(0)
        temp1 = "".join(_temp1)
        temp2 = "".join(_temp2)
        if temp1.isdigit() and temp2.isdigit():
            return temp1, temp2
##############################################################################



##############################################################################
" NAME: process_parameter_list_block(block, DeclaredIdentifiers)"
#=============================================================================
# DESCRIPTION: Takes a parameter declaration and definition in the form of a 
# string and converts it into lists containing the following info for each 
# item being declared: id, domain, description, domain test result, values
# STATUS: Working
#=============================================================================
# EXAMPLE INPUT AND OUTPUT:
# Given: """ Parameters
# a(i)    capacity of plant i in cases
#        / Seattle   350
#          San-Diego 600 /
# b(j) \tdemand at market j in cases
#        / New-York  325
#          Chicago   300
#          Topeka    275 / ; """, ['i', 'j']
# Returns: [('a', ['i'], 'capacity of plant i in cases', True, 
#               [('Seattle', '350'), ('San-Diego', '600')]), 
#          ('b', ['j'], 'demand at market j in cases', True, 
#               [('New-York', '325'), ('Chicago', '300'), ('Topeka', '275')])]
#=============================================================================
# CODE:
def process_parameter_list_block(block, DeclaredIdentifiers):

    #remove excess whitespace within block
    stripped_block = minimize_white_space(block)

    # split block to separate declarations and definitions
    portion1, portion2 = split_block_into_dec_def_pairs(stripped_block)

    # Convert declaration portions into a list of raw ids and descriptions 
    raw_ids, descriptions = separate_identifier_from_description(portion1)
    # Refine raw ids and check that the set in the domain has been declared
    ids, doms, dom_tests = split_clean_and_test_ids(raw_ids, 
                                                    DeclaredIdentifiers)


    # Convert the raw data portion of each parameters definition into a list 
    # of n-tuples, producing a list of lists of n-tuples. Where n is equal
    # to the length of the domain plus 1, and is less than 5.
    keyvalue_lists = convert_raw_list_data_to_n_tuple_list(doms, portion2)

    # Check to make sure each list of values is the same length
    if not list_length_check([ids, doms, descriptions, dom_tests, 
                              keyvalue_lists]):
        return 'error'

    # Compile these separate portions into a list of parameters
    parameters = compile_parameter_lists(ids, doms, descriptions, dom_tests, 
                                         keyvalue_lists)

    return parameters
##############################################################################



##############################################################################
" NAME: process_raw_set_data(portion)"
#=============================================================================
# DESCRIPTION: for loop to separate/enumerate the list(s) of set elements
# STATUS: Works
#=============================================================================
# EXAMPLE INPUT AND OUTPUT:
# Given: [' Seattle San-Diego ', ' New-York Chicago Topeka ', 
#           ' wiggle1*wiggle6 ']
# Returns: [['Seattle', 'San-Diego'], ['New-York', 'Chicago', 'Topeka'], 
#          ['wiggle1', 'wiggle2', 'wiggle3', 'wiggle4', 'wiggle5', 'wiggle6']]
#=============================================================================
# CODE:
def process_raw_set_data(portion):
    element_list = [] # Contains set of set elements list(s)
            
    # for loop to separate/enumerate the list(s) of set elements
    for groups in portion:

        # Check for asterisk enumeration
        test = groups
        if len(test.split("*")) > 1:
            temp = test.strip().split("*")
            split_list = []
            for item in temp:
                split_list.append(item.strip())                              

            temp1, temp2 = find_the_iteration_range(split_list[0], 
                                                    split_list[1])
       
            root = split_list[0].partition(temp1)[0]
        
            list_of_elements = []
            for i in range(convert_string_to_number(temp1), 
                           convert_string_to_number(temp2) + 1):
                list_of_elements.append(root + str(i))
       
            element_list.append(list_of_elements)
        
        
        
        # If no asterisk is present split string into set elements
        else:
            element_list.append(minimize_white_space(groups).split(" "))

    return element_list
##############################################################################



##############################################################################
" NAME: process_set_block(block)"
#=============================================================================
# DESCRIPTION: Takes a set declaration and definition in the form of a string
# and converts it into lists containing the following info for each 
# set being declared: id, description, members
# STATUS: Working
#=============================================================================
# EXAMPLE INPUT AND OUTPUT:
# Given: """ Sets
#	i canning plants / Seattle, San-Diego /
#   	j markets        / New-York, Chicago, Topeka / 
#    k suits          /    wiggle1*wiggle6   /       """
# Returns: [('i', 'canning plants', ['Seattle', 'San-Diego']), 
#           ('j', 'markets', ['New-York', 'Chicago', 'Topeka']), 
#           ('k', 'suits', ['wiggle1', 'wiggle2', 'wiggle3', 'wiggle4', 
#               'wiggle5', 'wiggle6'])]
#=============================================================================
# CODE:
def process_set_block(block):
    #remove excess whitespace within block
    stripped_block = minimize_white_space(block)

    # split block to separate declarations and definitions
    portion1, portion2 = split_block_into_dec_def_pairs(stripped_block)

    # Convert declaration portions into a list of raw ids and descriptions 
    raw_ids, descriptions = separate_identifier_from_description(portion1)

    # Convert raw set data into a list of element lists
    element_lists = process_raw_set_data(portion2)

    sets = compile_set_lists(raw_ids, descriptions, element_lists)


    return sets
##############################################################################



##############################################################################
" NAME: process_scalar_block(block)"
#=============================================================================
# DESCRIPTION: Takes a scalar declaration and definition in the form of a
# string and converts it into lists containing the following info for each 
# scalar being declared: id, description, value
# STATUS: Working
#=============================================================================
# EXAMPLE INPUT AND OUTPUT:
# Given: """ Scalar f freight in dollars per case per thousand miles /90/"""
# Returns: [('f', 'freight in dollars per case per thousand miles', ['90'])]
#=============================================================================
# CODE:
def process_scalar_block(block):
    #remove excess whitespace within block
    stripped_block = minimize_white_space(block)

    # split block to separate declarations and definitions
    portion1, portion2 = split_block_into_dec_def_pairs(stripped_block)

    # Convert declaration portions into a list of raw ids and descriptions 
    raw_ids, descriptions = separate_identifier_from_description(portion1)

    # Convert raw set data into a list of element lists
    element_lists = process_raw_set_data(portion2)

    scalars = compile_set_lists(raw_ids, descriptions, element_lists)


    return scalars
##############################################################################



##############################################################################
" NAME: process_table(block, DeclaredIdentifiers)"
#=============================================================================
# DESCRIPTION: Takes a table declaration and definition and processes it into
# usable data. The table output is in the format [id, domain, description, 
# domain test result, data] where data represents the table as:
# [[keys for the first domain in the declaration], [keys for the second],
#   [[layer of table representing the first value of the first domain],
#    [layer of table representing the second value], ...]]
# STATUS: Working
#=============================================================================
# EXAMPLE INPUT AND OUTPUT:
# Given: """ Table d(i,j) distance in thousands of miles
#    New-York Chicago Topeka
#           Seattle 2.5 1.7 1.8
#    \tSan-Diego 2.5 1.8 1.4 """
# Returns: ['d', ['i', 'j'], 'distance in thousands of miles', True, 
#           [['Seattle', 'San-Diego'], ['New-York', 'Chicago', 'Topeka'], 
#            [['2.5', '1.7', '1.8'], ['2.5', '1.8', '1.4']]]]
#=============================================================================
# CODE:
def process_table(block, DeclaredIdentifiers):
    declaration, trash, table = block.partition("\n")
    portion1 = [declaration]
    identifiers, descriptions = separate_identifier_from_description(portion1)
    table_layers = clean_split_on_list_of_strings(table.split("\n"))
    across_domain = table_layers.pop(0)
    down_domain = []
    for line in table_layers:
        down_domain.append(line.pop(0))

    ids, doms, tests = split_clean_and_test_ids(identifiers, DeclaredIdentifiers)
    data = [down_domain, across_domain, table_layers]
    table = [ids.pop(0), doms.pop(0), descriptions.pop(0), tests.pop(0), data]

    return table
##############################################################################



##############################################################################
" NAME: process_variables(block, StatementKeys, DeclaredIdentifiers)"
#=============================================================================
# DESCRIPTION: Takes a block of text starting with the Variable declaration
# and converts it into a list containing the declared variables as a quadtuple
# of the form: (identifier, [domain(s)], description, domain test value)
# STATUS: Working
#=============================================================================
# EXAMPLE INPUT AND OUTPUT:
# Given: """
# Variables
# x(i,j) shipment quantities in cases
# z total transportation costs in 1000s of dollars """
#
# Returns: [('x', ['i', 'j'], 'shipment quantities in cases', True), 
#           ('z', [], 'total transportation costs in 1000s of dollars', True)]
#=============================================================================
# CODE:
def process_variables(block, StatementKeys, DeclaredIdentifiers):
    split_block = block.split("\n")
    dirty_list = clean_split_on_list_of_strings(split_block, True)
    clean_list = []
    if dirty_list[0][0].startswith(StatementKeys):
        dirty_list[0].pop(0)
    
    for list in dirty_list:
        if len(list) > 0:
            clean_list.append(" ".join(list))
    
    raw_ids, descriptions = separate_identifier_from_description(clean_list)
    ids, doms, dom_tests = split_clean_and_test_ids(raw_ids, 
                                                    DeclaredIdentifiers)
    variables = compile_variable_lists(ids, doms, descriptions, dom_tests)
    return variables
##############################################################################



"############################################################################"
">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
"                                 Test Area                                  "
">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
"############################################################################"


##############################################################################
" NAME: process_equation(block, StatementKeys, DeclaredIdentifiers)"
#=============================================================================
# DESCRIPTION: Takes a block of text starting with the Equation declaration
# and converts it into a list containing the declared variables as a tuple
# of the form: ([(identifier, [domain(s)], description, domain test value)..],
#               [[identifier, equation]...])
# STATUS: Working
#=============================================================================
# EXAMPLE INPUT AND OUTPUT:
# Given: """
# Equations
#       cost            define objective function
#       supply(i)       observe supply limit at plant i
#       demand(j)       satisfy demand at market j***
# cost..     z =e= sum((i,j), c(i,j)*x(i,j))***
# supply(i)..  sum(j, x(i,j)) =l= a(i)***
# demand(j).. sum(i, x(i,j)) =g= b(j)*** """
#
# Returns: [['cost', [], 'define objective function', True, 
#            ' z =e= sum((i,j), c(i,j)*x(i,j))'], 
#           ['supply', ['i'], 'observe supply limit at plant i', True, 
#            ' sum(j, x(i,j)) =l= a(i)'], 
#           ['demand', ['j'], 'satisfy demand at market j', True, 
#            ' sum(i, x(i,j)) =g= b(j)']]
#=============================================================================
# CODE:
def process_equations(block, StatementKeys, DeclaredIdentifiers):
    split_block = block.split("***")
    declarations = process_variables(split_block.pop(0), StatementKeys, 
                                     DeclaredIdentifiers)

    equations = []
    for equation in split_block:
        clean_equation = minimize_white_space(equation, True)
        if len(clean_equation) > 1:
            equations.append(clean_equation.split(".."))

    for i in range(0, len(declarations)):
        if len(equations) > 1:
            declarations[i].append(equations[i][1])
        else:
            declarations[i].append(equations[i][0])
    return declarations
##############################################################################


# Find Index on the respective domains, then use that value to access table?
##### Might be super slow...






"############################################################################"
">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
"                                 TO DO LIST                                 "
">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
"############################################################################"

# [X]   Sets
# [X]   Parameter-List
# [X]   Parameter-Scalar
# [X]   Tables
# [X]   Parameter-Direct Assignment
# [X]   Variables
# [X]   Variable Types: Free, Positive, Negative, Binary, Integer
# [X]   Equations
 
"############################################################################"
">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
"                                    NOTES                                   "
">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
"############################################################################"
# 1. Zero is the default value for all parameters. Therefore, you only need to
#       include the nonzero entries in the element-value list, and these can 
#       be entered in any order.
# 2. Data should be checked, but not in this module!
# 3. all(iterable) => True if all elements of iterable are true, otherwise 
#       False

"############################################################################"
">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
"                                END of MODULE                               "
">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
"############################################################################"









