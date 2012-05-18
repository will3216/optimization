##############################################################################
##          Version: 1.0                Updated: February 29th 2012         ##
##############################################################################
##                                                                          ##
##               GGGG          AAA      MMM       MMM     SSSSSS            ##
##            GGG    GG       AA AA     MMMM     MMMM   SS                  ##
##           GG              AA   AA    MM MM   MM MM     SSSSSS            ##
##           GG     GGGGG   AAAAAAAAA   MM  MM MM  MM           SS          ##
##            GGG    GG G   AA     AA   MM   MMM   MM   SSS    SSS          ##
##               GGGG   G   AA     AA   MM    M    MM      SSSS             ##
##                                                                          ##
"#                                                                          #"
"#                                222222                                    #"
"#                              22      22                                  #"
"#==============================     222  ==================================#"
"#                                222                                       #"
"#                              22                                          #"
"#                              2222222222                                  #"
"#                                                                          #"
##                                                                          ##
##        PPPPPPP                      HH                                   ##
##        PP     PP             TT     HH                                   ##
##        PP     PP           TTTTTTT  HH HHH      OOOO    NN NNN           ##
##        PPPPPPP    YY   YY    TT     HHH  HHH  OO    OO  NNN   NNN        ##
##        PP         YY   YY    TT     HH    HH  OO    OO  NN     NN        ##
##        PP           YYYYY     TTT   HH    HH    OOOO    NN     NN        ##
##                       YY                                                 ##
##                  YY  YY                                                  ##
##                    YY                                                    ##
##                                                                          ##
##############################################################################
##                             William Bryant                               ##
##                      Tabu Search Software Project                        ##
##                         Camarda Research Group                           ##
##                          University of Kansas                            ##
##############################################################################
##     DESCRIPTION:                                                         ##
##                                                                          ##
##          This  script  takes the name of a text file  containing an      ##
##      optimization model formulation, which is in the standard  GAMS      ##
##      submission format, and converts  it to a python code formatted      ##
##      to be optimized by [INSERT NAME OF PROGRAM].                        ##
##                                                                          ##
##      See the attached ReadMe.txt for more information on submission      ##
##      formatting.                                                         ##
##                                                                          ##
##############################################################################

#================================== Notes! ==================================#
# Look into string formatting:                                               #
#       http://docs.python.org/release/3.1.3/library/string.html             #
#                                                                            #
#                                                                            #
#============================================================================#
#============================================================================#
#============================================================================#

"############################################################################"
">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
"                                   IMPORTS                                  "
">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
"############################################################################"

import module1

"############################################################################"
">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
"                              GLOBAL VARIABLES                              "
">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
"############################################################################"

StatementKeys = ('Set', 'Parameter', 'Table', 'Scalar', 'Variables', 
                 'Positive', 'Binary', 'Negative', 'Integer', 'Free', 
                 'Equation')
VariableKeys = ('Free', 'Positive', 'Negative', 'Binary', 'Integer')

DeclaredIdentifiers = []
IdentifierTypes = []
IdentifierData = []
DeclaredVariables = []



"############################################################################"
">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
"                                  FUNCTIONS                                 "
">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
"############################################################################"
#=============================================================================
#=============================================================================
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
#=============================================================================
#=============================================================================



##############################################################################
" NAME: ConvertedData"
#=============================================================================
# DESCRIPTION: Compiles the separate lists of variable names, types, and 
# definitions into one list containing 3-tuples of each declared item.
# STATUS: Working
#=============================================================================
# EXAMPLE INPUT AND OUTPUT:
# Given: None
# Returns: [('i', 'Set', ['canning plants', ['seattle', 'san-diego']]), 
#           ('j', 'Set', ['markets', ['new-york', 'chicago', 'topeka']]), 
#           ('a', 'Param List', [['i'], 'capacity of plant i in cases', True, 
#                                [('seattle', '350'), ('san-diego', '600')]]),
#           ('b', 'Param List', [['j'], 'demand at market j in cases', True, 
#                                [('new-york', '325'), ('chicago', '300'), 
#                                 ('topeka', '275')]]), 
#           ('d', 'Table', [['i', 'j'], 'distance in thousands of miles',
#                           True, [['seattle', 'san-diego'], 
#                           ['new-york', 'chicago', 'topeka'], 
#                           [['2.5', '1.7', '1.8'], ['2.5', '1.8', '1.4']]]]),
#           ('f', 'Scalar', ['freight in dollars per case per thousand miles', 
#                            ['90']]), 
#           ('c', 'Param DA', [['i', 'j'], 
#            'transport cost in 1000s of dollars per case', True, 
#            'c(i,j) = f*d(i,j)/1000']), 
#           ('x', 'Variable', [['i', 'j'], 'shipment quantities in cases', 
#                              True]), 
#           ('z', 'Variable', [[], 
#                              'total transportion costs in 1000s of dollars',
#                              True]), 
#           ('cost', 'Equation', [[], 'define objective function', True, 
#            ' z =e= sum((i,j), c(i,j)*x(i,j))']), 
#           ('supply', 'Equation', [['i'], 'observe supply limit at plant i', 
#                                   True, ' sum(j, x(i,j)) =l= a(i)']), 
#           ('demand', 'Equation', [['j'], 'satisfy demand at market j', True,
#                                   ' sum(i, x(i,j)) =g= b(j)'])]
#=============================================================================
# CODE:
def ConvertedData():
    data = []
    for i in range(len(DeclaredIdentifiers)):
        if IdentifierTypes[i] == 'Variable':
            for item in DeclaredVariables:
                if item[0] == DeclaredIdentifiers[i]:
                    IdentifierData[i].append(item[1])
        datum = (DeclaredIdentifiers[i], IdentifierTypes[i], 
                 IdentifierData[i])
        data.append(datum)
    return data
##############################################################################



##############################################################################
" NAME: input()"
#=============================================================================
# DESCRIPTION: Takes a filename which is currently inputted via a prompt but
# will eventually be inputted from the user-interface. This text file is 
# opened and then copied to a string. This string is then split at the "####"
# which separates the optimization model, or "model" from the search method
# configuration and parameters, or "solve" portion. The model portion is then
# sent to the model_parse function to be converted to python script, and the 
# search method portion is sent to the solve_parse function.
#=============================================================================
# STATUS: Working
#=============================================================================
# EXAMPLE INPUT AND OUTPUT:
# Given: "Inputfile.txt"
# Returns: None
#=============================================================================
# CODE:
def input(filename):  

    # Open submission file to read
    openfile = open(filename, 'r')

    # Copy the contents of the submission file and split it into the 
    # model and solve portions.
    model_solve_split = openfile.read().split("####") # = [model, solve]

    # Convert the model portion into python objects and return them and the 
    # solve portion of the submission.
    return model_parse(model_solve_split[0]), model_solve_split[1]
##############################################################################



##############################################################################
" NAME: set_variable_type(block)"
#=============================================================================
# DESCRIPTION: description of function
# STATUS: Working, In Progress, Broken, etc.
#=============================================================================
# EXAMPLE INPUT AND OUTPUT:
# Given: <sample input>
# Returns: <sample output>
#=============================================================================
# CODE:
def set_variable_type(block):
    v_type, trash, dirty_vars = block.partition("variable")
    vars = module1.clean_split(dirty_vars)

    for var in vars:
        var_decl = (var, v_type)
        for variable in DeclaredVariables:
            if var == variable[0]:
                variable[1] = v_type

    return
##############################################################################



##############################################################################
##                             PARSING THE MODEL                            ##
##############################################################################
## DESCRIPTION:                                                             ##
##                                                                          ##
##           Takes a string of text which represents the model portion      ##
##      of the input file. This string is then split at each semicolon,     ##
##      ";" which denotes the end of a statement.  These statements are     ##
##      then passed through a switch function which is used to identify     ##
##      the  type of statement being made,  sending each to the correct     ##
##      function to process the text into python code.                      ##
##                                                                          ##
##############################################################################

#============================================================================#
#============================  MODEL_PARSE CODE  ============================#
#============================================================================#

def model_parse(model_string):

#>>>>>>>>>>>>>>>>>>>>>>> SUB-ROUTINES of model_parse() <<<<<<<<<<<<<<<<<<<<<<#

    ##########################################################################
    " NAME: correct_first_split(list(string))"
    #=========================================================================
    # DESCRIPTION: Takes the list produced by splitting the model string at ;
    # and correctly separates it with regard to the functions called after the
    # switch function.
    # STATUS: Working
    #=========================================================================
    # EXAMPLE INPUT AND OUTPUT:
    # Given: ['Set woogle', 'Parameter weasle', 'woozle', 'Equation ma',
    #         'ni', 'ac']
    # Returns: ['Set woogle', 'Parameter weasle***woozle', 
    #           'Equation ma***ni***ac']
    #=========================================================================
    # CODE:
    def correct_first_split(split_block):
    
        key_start_list = starts_with_key(split_block)
        good_list = []
    
    
        if key_start_list[0] == False:
            return 'error'
 
        holder = []
        for i in range(len(split_block)):
            if key_start_list[i] == True:
                if len(holder) > 1:
                    good_list.append("***".join(holder))
                elif len(holder) > 0:
                    good_list.append(holder[0])
                holder = [split_block[i]]
            else:
                holder.append(split_block[i])

            if i == len(split_block) - 1:
                if len(holder) > 1:
                    good_list.append("***".join(holder))
                elif len(holder) > 0:
                    good_list.append(holder[0])


        return good_list
    ##########################################################################



    ##############################################################################
    " NAME: starts_with_key(list(string))"
    #=============================================================================
    # DESCRIPTION: Creates a list the same size as input list of strings 
    # containing the truth values of whether they start with one of the keys in
    # the global variable StatementKeys
    # STATUS: Working
    #=============================================================================
    # EXAMPLE INPUT AND OUTPUT:
    # Given: ['Set woogle', 'Parameter weasle', 'woozle', 'Equation ma',
    #         'ni', 'ac']
    # Returns: [True, True, False, True, False, False]
    #=============================================================================
    # CODE:
    def starts_with_key(blocks):
        proper_start_list = []

        
        for i in range(len(blocks)):
                
            if blocks[i].lstrip().startswith(StatementKeys):
                proper_start_list.append(True)
            else:
                proper_start_list.append(False)
        return proper_start_list
    ##############################################################################

    

    ##########################################################################
    " NAME: parse_model_blocks(list(block))"
    #=========================================================================
    # DESCRIPTION: Decides which conversion function should be used for each 
    # block of a list of statements in string form.
    # STATUS: In Progress
    #=========================================================================
    # EXAMPLE INPUT AND OUTPUT:
    # Given: <sample input>
    # Returns: <sample output>
    #=========================================================================
    # CODE:
    def parse_model_blocks(set_of_blocks):
        for un_modified_block in set_of_blocks:

            # Remove any leading whitespace, indentations, or new lines 
            # present before the, now capitalized, statement keyword.
            block = un_modified_block.lstrip('\nt').lstrip().capitalize()

        #___________________________________________________________
        #                                                           |
        # Send statement block to the appropriate parsing function  |
        #___________________________________________________________|

            if block.startswith("Set")         == True:
                print_to_script_set(block)

            elif block.startswith("Parameter") == True:
                print_to_script_parameter(block)

            elif block.startswith("Scalar")    == True:
                print_to_script_scalar(block)

            elif block.startswith("Table")     == True:
                print_to_script_table(block)

            elif block.startswith("Variable")  == True:
                print_to_script_variable(block)

            elif block.startswith("Equation")  == True:
                print_to_script_equation(block)

            elif block.startswith(VariableKeys) == True:
                set_variable_type(block)

            else: 
                print('error')


        data = ConvertedData()    
        return data
    ##########################################################################
   


    ##########################################################################
    " NAME: print_to_script_set(string)"
    #=========================================================================
    # DESCRIPTION: Takes a string of text representing a set statement and 
    # splits it into substrings at each instance of "/" to produce pairs of
    # strings. The first portion contains the set identifier and the
    # description  of  the set,  while the second portion contains a 
    # list  of elements within the set.  There may also be an excess
    # whitespace string at the end which can be discarded.
    #
    # STATUS: In Progress
    #=========================================================================
    # EXAMPLE INPUT AND OUTPUT:
    # Given: """ Sets
    #	i canning plants / Seattle, San-Diego /
    #   	j markets        / New-York, Chicago, Topeka / """
    # Returns: [('i', 'canning plants', ['seattle', 'san-diego']), 
    #           ('j', 'markets', ['new-york', 'chicago', 'topeka'])]
    #=========================================================================
    # CODE:
    def print_to_script_set(block):
        sets = module1.process_set_block(block)

        for item in sets:
            DeclaredIdentifiers.append(item.pop(0))
            IdentifierTypes.append("Set")
            IdentifierData.append(item)
        # Add ids to DeclaredIdentifiers
        # Print to Python Script

        return # Value which indicates error if something fucks up
    ##########################################################################
    


    ##########################################################################
    " NAME: print_to_script_parameter(string)"
    #=========================================================================
    # DESCRIPTION: 
    #
    # STATUS: In Progress
    #=========================================================================
    # EXAMPLE INPUT AND OUTPUT:
    # Given: <sample input>
    # Returns: None
    #=========================================================================
    # CODE:
    def print_to_script_parameter(block):
        if "***" in block:
            parameters = module1.process_equations(block, StatementKeys,
                                                   DeclaredIdentifiers)
            for item in parameters:
                DeclaredIdentifiers.append(item.pop(0))
                IdentifierTypes.append("Param DA")
                IdentifierData.append(item)
        else:
            parameters = module1.process_parameter_list_block(block, 
                                                        DeclaredIdentifiers)
        # Add ids to DeclaredIdentifiers
        # Print to Python Script
            for item in parameters:
                DeclaredIdentifiers.append(item.pop(0))
                IdentifierTypes.append("Param List")
                IdentifierData.append(item)
        
        return # Value which indicates error if something fucks up
    ##########################################################################

    

    ##########################################################################
    " NAME: print_to_script_scalar(string)"
    #=========================================================================
    # DESCRIPTION: 
    #
    # STATUS: In Progress
    #=========================================================================
    # EXAMPLE INPUT AND OUTPUT:
    # Given: <sample input>
    # Returns: [('f', 'freight in dollars per case per thousand miles', 
    #            ['90'])]
    #=========================================================================
    # CODE:
    def print_to_script_scalar(block):
        scalars = module1.process_scalar_block(block)
        # Add ids to DeclaredIdentifiers
        for item in scalars:
            DeclaredIdentifiers.append(item.pop(0))
            IdentifierTypes.append("Scalar")
            IdentifierData.append(item)
        # Print to Python Script
        
        return # Value which indicates error if something fucks up
    ##########################################################################



    ##########################################################################
    " NAME: print_to_script_table(string)"
    #=========================================================================
    # DESCRIPTION: 
    #
    # STATUS: In Progress
    #=========================================================================
    # EXAMPLE INPUT AND OUTPUT:
    # Given: <sample input>
    # Returns: ['d', ['i', 'j'], 'distance in thousands of miles', False, 
    #           [['seattle', 'san-diego'], ['new-york', 'chicago', 'topeka'], 
    #           [['2.5', '1.7', '1.8'], ['2.5', '1.8', '1.4']]]]
    #=========================================================================
    # CODE:
    def print_to_script_table(block):
        table = module1.process_table(block, DeclaredIdentifiers)

        # Add ids to DeclaredIdentifiers
        DeclaredIdentifiers.append(table.pop(0))
        IdentifierTypes.append("Table")
        IdentifierData.append(table)
        # Print to Python Script
        
        return # Value which indicates error if something fucks up
    ##########################################################################



    ##########################################################################
    " NAME: print_to_script_variable(string)"
    #=========================================================================
    # DESCRIPTION: 
    #
    # STATUS: Empty
    #=========================================================================
    # EXAMPLE INPUT AND OUTPUT:
    # Given: <sample input>
    # Returns: None
    #=========================================================================
    # CODE:
    def print_to_script_variable(block):
        variable = module1.process_variables(block, StatementKeys, 
                                             DeclaredIdentifiers)


        for item in variable:
            DeclaredVariables.append([item[0], "Free", item[1]])
            DeclaredIdentifiers.append(item.pop(0))
            IdentifierTypes.append("Variable")
            IdentifierData.append(item)
            
        
        return
    ##########################################################################



    ##########################################################################
    " NAME: print_to_script_equation(string)"
    #=========================================================================
    # DESCRIPTION: 
    #
    # STATUS: Empty
    #=========================================================================
    # EXAMPLE INPUT AND OUTPUT:
    # Given: <sample input>
    # Returns: None
    #=========================================================================
    # CODE:
    def print_to_script_equation(block):
        equations = module1.process_equations(block, StatementKeys, 
                                              DeclaredIdentifiers)
        for item in equations:
            DeclaredIdentifiers.append(item.pop(0))
            IdentifierTypes.append("Equation")
            IdentifierData.append(item)

        return
    ##########################################################################



#============================================================================#
#>>>>>>>>>>>>>>>>>>>>>>>>>>>> END OF SUB-ROUTINES <<<<<<<<<<<<<<<<<<<<<<<<<<<#
#============================================================================#

    # Split the input string into blocks of text representing each 
    # statement.
    blocks = model_string.split(";") # = [stmnt1, stmnt2, ...]

    # Recombine some of the blocks that have no meaning without their 
    # preceding statements
    good_blocks = correct_first_split(blocks)

    # Send the newly segmented statement blocks to be sorted and parsed
    data = parse_model_blocks(good_blocks)
    return data



def __test_module():
    pass

#filename = "inputfile.txt"
#openfile = open(filename, 'r')
#model_portion, solve_portion = openfile.read().split("####") # = [model, solve]

#print(model_parse(model_portion))






