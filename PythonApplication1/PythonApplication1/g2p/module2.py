"###############################################################"#############
"####_     ######     _######## ______ #######_   ___ ##########"####      ###
"#####   _  ####  _   #######  _######_  ######   ###__ ########"###___##   ##
"#####   #_  ##  _#   ######  _########_  #####   #####_  ######"########   ##
"#####   ##_    _##   #####_  ##########  _####   ######   #####"#######   ###
"#####   ###_  _###   ######_  ########  _#####   ######  _#####"#####   #####
"#####   ####__####   #######__  ####   _######   #### ___######"###   #######
"####_____########_____########________#######_________#########"###________##
"###############################################################"#############
###                                                                        ###
###                                                                        ###
###        MODULE 2:                                                       ###
###             Everything you need to convert GAMS data as python         ###
###         data into python script, or your money back!                   ###
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
##  for the transcription of python data  structures into python code,  or  ##
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
" NAME: python_function_as_string(id, data, type, args*)"
#=============================================================================
# DESCRIPTION: description of function
# STATUS: Working, In Progress, Broken, etc.
#=============================================================================
# EXAMPLE INPUT AND OUTPUT:
# Given: <sample input>
# Returns: <sample output>
#=============================================================================
# CODE:
def python_structure_as_string(id, data, type):
    return
##############################################################################


def find_bracket_pair_index(sts):
    # sts is the string to search, it should not include the 
    # opening bracket.
    bracket_level = 1
    index_count = 0
    while bracket_level > 0 and index_count <= len(sts):
        if sts[index_count] == ')':
            bracket_level = bracket_level - 1
        elif sts[index_count] == '(':
            bracket_level = bracket_level + 1
        index_count = index_count + 1
    if bracket_level == 0:
        return None
    else:
        return index_count

def find_dependencies(eq_str):
    dependency_list =[]
    temp_str = ''

    for char in eq_str:
        if char.isalpha():
            temp_str = ''.join([temp_str, char])
        elif not temp_str == '':
            if char.isdigit():
                temp_str = ''.join([temp_str, char])
            else:
                if not temp_str in dependency_list:
                    dependency_list.append(temp_str)
                temp_str = ''

    if not temp_str == '':
        dependency_list.append(temp_str)

    return dependency_list

def classify_dependency(dependency):
    if dependency in self.declared_variables.keys():
        classified_dependency = 'V'
    elif dependency in self.declared_variables.keys():
        classified_dependency = 'P'
    elif dependency in GoodFunctionNames:
        classified_dependency = 'G'
    elif dependency in BadFunctionNames:
        classified_dependency = 'B'
    elif dependency in self.declared_equations.keys():
        classified_dependency = 'E'
    else:
        classified_dependency = 'U'
    return classified_dependency

def classify_dependencies(dependency_list):
    classified_dependencies = []
    for item in dependency_list:
        temp = classify_dependency(item)
        classified_dependencies.append(temp)
    return classified_dependencies

def remove_all_whitespace(eq):
    eq_holder = eq
    eq_holder = eq_holder.replace(' ','').replace('\n','')
    eq_holder = eq_holder.replace('\t','')
    return eq_holder

def parse_partial_eq(eq, func=None, in_dom=False, in_func=False):
    operators = ['+','-','/']
    ambi_operators = ['*','**']
    

    eq_str = ''
    holder_str = ''
    num_str = ''
    str_str = ''
    arg_str = ''
    last_func = ''
    last_id = ''
    
    arg_list = []
    err_list = []
    fxn_dom = []
    arg_dom = []
    dom_holder = []

    building_id = False
    building_num = False
    building_string = False
    
    
    while len(eq_holder) > 0 and len(err_list) > 0:

        # Are we building an id?
        if building_id:
            # Is the current character alphanumeric?
            if eq_holder[0].isalnum():
                holder_str = holder_str + eq_holder[0]
                eq_holder = eq_holder[1:]
            # Is the current character an underschore?
            elif eq_holder[0] == '_':
                holder_str = holder_str + eq_holder[0]
                eq_holder = eq_holder[1:]
            # Is the current character a period?
            elif eq_holder == '.':
                # Add current character to holder_str
                holder_str = holder_str + eq_holder[0]
                # Remove current character from eq_holder
                eq_holder = eq_holder[1:]
                # Add warning about sending a python function through a GAMS
                # Parser
                warning_msg = 'Python module specification may not '
                warning_msg = warning_msg + 'convert correctly in :'
                self.warning_list.append(warning_msg)
            else:
                # Classify the newly built id
                class_id = classify_dependency(holder_str)
                # Modify accordingly
                if class_id   == 'V':
                    # Check type to see if a domain is expected to follow
                        
                    self.last_id = holder_str
                    pass
                elif class_id == 'P':
                    # Check type to see if a domain is expected to follow
                        
                    self.last_id = holder_str
                    pass
                elif class_id == 'G':


                    self.last_func = holder_str
                    pass
                elif class_id == 'B':
                    error_msg = 'The GAMS function identifier "'
                    error_msg = error_msg + holder_str + '" is not current'
                    error_msg = error_msg + 'ly supported, in :'
                elif class_id == 'E':
                    warning_msg = 'Could not determine what to do with id'
                    warning_msg = warning_msg + 'entifier "' + holder_str
                    warning_msg = warning_msg + '" in :'
                    self.warning_list.append(warning_msg)
                else:
                    warning_msg = 'Could not determine type of ident'
                    warning_msg = warning_msg + 'ifier "' + holder_str
                    warning_msg = warning_msg + '" in :'
                    self.warning_list.append(warning_msg)
                # Append to eq_str
                eq_str = eq_str + holder_str
                # Clear holder_str
                holder_str = ''
                # Set building_id to False
                building_id = False


        # Are we building a number?
        elif building_num:
            # Is the next character a digit?
            if eq_holder[0].isdigit():
                # Add it to the num_str!
                num_str = eq_holder[0]
                # Remove it from the eq_holder
                eq_holder = eq_holder[1:]
            # Is the next character a period?
            elif eq_holder[0] == '.':
                # Does the current number being built already have a period?
                if '.' in num_str:
                    # This is an error, add it to the error list
                    err_list.append("Unexpected '.' in ")
                else:
                    # Add it to the number string
                    num_str = eq_holder[0]
                    eq_holder = eq_holder[1:]
            # End the number building process
            else:
                # Are we in a function right now?
                if in_func:
                # Is this a new argument in a function?
                    if new_arg:
                # If so, append it to the arg_list
                        pass
                # If not, append it to the current arg in the arg_list
                    else:
                        pass
                # If not in a function, append it to the eq_str
                else:
                    eq_str = eq_str + num_str
                # Clear the num_str
                num_str = ''
                # End the building string process
                building_num = False


        # Are we building a string?
        elif building_string:
            # Match the closing ' or " to an index
            endex = eq_holder.find(str_str)
            # Add the rest of the string to the string holder
            str_str = str_str + eq_holder[:endex]
            # Remove the rest of the string from the eq holder
            eq_holder = eq_holder[endex:]
            # Is this in the domain of something?
            if in_dom:
                # If so, append to the domain of whatever it is
                dom_holder.append(str_str)
                # Clear the string holder
                str_str = ''
            # If not, wtf is a string doing here? ERROR!
            else:
                err_list.append('Unexpected string "' + str_str + '" in ')



        # If we are not currently building a string, num, or id, 
        # what are we building?
        elif len(holder_str) == 0:
            # Is it a new ID?
            if eq_holder[0].isalpha():
                # Add current char to id holder
                holder_str = eq_holder[0]
                # Remove current char from eq_holder
                eq_holder = eq_holder[1:]
                # Start the id build process
                building_id = True
            # Is it a new num?
            elif eq_holder[0].isdigit():
                # Add current char to num_holder
                num_str = eq_holder[0]
                # Remove current char from eq_holder
                eq_holder = eq_holder [1:]
                # Set build status to num
                building_num = True


            # Is it an operator?
            elif eq_holder[0] in operators:
                last_id = ''
                last_func = ''
                # Are we in a function?
                if in_func:
                    # Is this the beginning of a new arg?
                    if len(arg_str) == 0:
                        # Is the current char a '-'?
                        if eq_holder[0] == '-':
                            # Add the current char to the arg_str
                            arg_str = eq_holder[0]
                            # Remove the current char from eq_holder
                            eq_holder = eq_holder[1:]
                        else:
                            # Return an error, because an arg cannot begin
                            # with '+' or '/' (BECAUSE I SAID SO!)
                            err_msg = 'Unexpected "' + eq_holder[0] 
                            err_msg = err_msg + '" at the beginning'
                            err_msg = err_msg + ' of an expression in '
                            err_list.append(err_msg)
                    # Add the current char to the current arg_str
                    else:
                        arg_str = arg_str + eq_holder[0]
                        # Remove the current char from the eq_holder
                        eq_holder = eq_holder [1:]
                # Are we in a domain? (You cannot slice domains... yet)
                elif in_dom:
                    # Return an error, because I just said you can't slice domains!
                    err_msg = 'Unexpected "' + eq_holder[0] 
                    err_msg = err_msg + '" at the beginning'
                    err_msg = err_msg + ' of an expression in '
                    err_list.append(err_msg)
                # Well, then we should be in the main equation!
                else:
                    # So, let's add this operator to the main equation!
                    # But first, let's check to see if it is the first 
                    # char to be added to it
                    if len(eq_str) == 0:
                        # This means it can only be a '-', but is it?
                        if eq_holder[0] == '-':
                            # Add current character to the eq_str
                            eq_str = eq_holder[0]
                            # Remove it from the eq_holder
                            eq_holder = eq_holder[1:]
                        # Otherwise return an error!
                        else:
                            err_msg = 'Unexpected "' + eq_holder[0] 
                            err_msg = err_msg + '" at the beginning'
                            err_msg = err_msg + ' of an expression in '
                            err_list.append(err_msg)
                    # If eq_str is not empty!
                    else:
                        # Was the last character an operator?
                        if eq_str[-1] in operators:
                            # If so, this operator can't be anything but '-'
                            if eq_holder[0] == '-':
                                # Add the minus!
                                eq_str = eq_str + eq_holder[0]
                                # Subtract that minus!
                                eq_holder = eq_holder[1:]
                            # Otherwise and error should be returned
                            else:
                                err_msg = 'Unexpected "' + eq_holder[0] 
                                err_msg = err_msg + '" after an operator'
                                err_msg = err_msg + ' in '
                                err_list.append(err_msg)
                        # Was it an ambi_operator(s)?
                        elif eq_str[-1] in ambi_operators:
                            # If so, this operator can't be anything but '-'
                            if eq_holder[0] == '-':
                                # Add the minus!
                                eq_str = eq_str + eq_holder[0]
                                # Subtract that minus!
                                eq_holder = eq_holder[1:]
                            # Otherwise and error should be returned
                            else:
                                err_msg = 'Unexpected "' + eq_holder[0] 
                                err_msg = err_msg + '" after an operator'
                                err_msg = err_msg + ' in '
                                err_list.append(err_msg)
                        # If not an operator, add this operator to eq_str
                        else:
                            # Add the current character to the eq_str
                            eq_str = eq_str + eq_holder[0]
                            # Remove the current character from the eq_holder
                            eq_holder = eq_holder[1:]


            # Is it a more ambiguous operator?
            elif eq_holder[0] in ambi_operators:
                last_id = ''
                last_func = ''
                # Are we in a function?
                if in_func:
                    # Is this the beginning of a new arg?
                    if len(arg_str) == 0:
                        # Return an error, because an arg cannot begin
                        # with '*' or '**' (BECAUSE I SAID SO!)
                        err_msg = 'Unexpected "' + eq_holder[0] 
                        err_msg = err_msg + '" at the beginning'
                        err_msg = err_msg + ' of an expression in '
                        err_list.append(err_msg)
                    # Add the current char to the current arg_str
                    else:
                        arg_str = arg_str + eq_holder[0]
                        # Remove the current char from the eq_holder
                        eq_holder = eq_holder [1:]
                # Are we in a domain? (You cannot slice domains... yet)
                elif in_dom:
                    # Return an error, because I just said you can't slice domains!
                    err_msg = 'Unexpected "' + eq_holder[0] 
                    err_msg = err_msg + '" in a domain expression in '
                    err_list.append(err_msg)
                # Well, then we should be in the main equation!
                else:
                    # So, let's add this operator to the main equation!
                    # But first, let's check to see if it is the first 
                    # char to be added to it
                    if len(eq_str) == 0:
                        # Return error, because you cannot start an expression with *
                        err_msg = 'Unexpected "' + eq_holder[0] 
                        err_msg = err_msg + '" at the beginning'
                        err_msg = err_msg + ' of an expression in '
                        err_list.append(err_msg)
                    # If eq_str is not empty!
                    else:
                        # Was the last character an operator?
                        if eq_str[-1] in operators:
                            # An error should be returned
                            err_msg = 'Unexpected "' + eq_holder[0] 
                            err_msg = err_msg + '" after an operator'
                            err_msg = err_msg + ' in '
                            err_list.append(err_msg)
                        # Was it an ambi_operator(s)?
                        elif eq_str[-1] in ambi_operators:
                            # If so, this operator can't be anything but '*'
                            if eq_holder[0] == '*':
                                # Add the multiplier!
                                eq_str = eq_str + eq_holder[0]
                                # Subtract that multiplier!
                                eq_holder = eq_holder[1:]
                            # Otherwise and error should be returned
                            else:
                                err_msg = 'Unexpected "' + eq_holder[0] 
                                err_msg = err_msg + '" after an operator'
                                err_msg = err_msg + ' in '
                                err_list.append(err_msg)
                        # If not an operator, add this operator to eq_str
                        else:
                            # Add the current character to the eq_str
                            eq_str = eq_str + eq_holder[0]
                            # Remove the current character from the eq_holder
                            eq_holder = eq_holder[1:]
            

            # Is it a new str?
            elif eq_holder[0] == "'" or eq_holder == '"':
                # Toggle building string to True
                building_string = True
                # Add the current character to the string holder
                str_str = eq_holder[0]
                # remove the current character from the eq_holder
                eq_holder = eq_holder[1:]
            # Is it a comma?
            elif eq_holder[0] == ',':
                last_id = ''
                last_func = ''
                # In a function?
                if in_func:
                    # Add argument to arg_list
                    arg_list.append(eq_str)
                    # Clear eq string
                    eq_str = ''
                    # Remove current character from eq_holder
                    eq_holder = eq_holder[1:]
                # In a domain?
                elif in_dom:
                    # Add argument to arg_list
                    arg_list.append(eq_str)
                    # Clear eq string
                    eq_str = ''
                    # Remove current character from eq_holder
                    eq_holder = eq_holder[1:]
                # Otherwise error!
                else:
                    error_msg = 'Unexpected "," in '
                    err_list.append(error_msg)


            # Is it an open paren?
            elif eq_holder[0] == '(':
                # Find closing indice
                closing_ind = find_bracket_pair_index(eq_holder[1:])
                # Check to see if a closing indice was found
                if closing_ind == None:
                    err_list.append('Could not find a closing paren in ')
                # List of Indexed functions
                indexed_functions = ['sum', 'prod', 'smin', 'smax']
                # bool that checks if this is an indexed function
                index_bool = func in indexed_functions and eq_str == ''
                index_bool = index_bool and len(arg_list) == 0

                # Is this in an indexed function?
                if index_bool:
                    # Slice the eq_holder to get the arguments between 
                    # parenthesis
                    dom_slice = eq_holder[1:]
                    dom_slice = dom_slice[:closing_ind - 1]
                    # Recurse this back through the function
                    _eq, _err, _dom = parse_partial_eq(dom_slice, in_dom=True)
                    # Append the function domain into the fxn_dom list
                    fxn_dom.append(_dom)
                    # Append any errors to error list
                    err_list.append(_err)
                    # Check to see if the returned eq_str is empty as it is
                    # suppose to be
                    if len(_eq) > 0:
                        err_list.append('Unexpected values, line 382')
                    # Remove the processed slice and parenthesis from the
                    # eq_holder
                    eq_holder = eq_holder[closing_ind + 2:]

                # Is this at the beginning of a new expression?
                elif eq_str == '':
                    # Slice the eq_holder to get the arguments between 
                    # parenthesis
                    expr_slice = eq_holder[1:]
                    expr_slice = expr_slice[:closing_ind - 1]
                    # Recurse this back through the function
                    _eq, _err, _dom = parse_partial_eq(expr_slice)
                    # Append the function domain into the arg_dom list
                    arg_dom.append(_dom)
                    # Append any errors to error list
                    err_list.append(_err)
                    # Check to see if the returned eq_str is non-empty as it is
                    # suppose to be
                    if not len(_eq) > 0:
                        err_list.append('Unexpected values, line 382')
                    else:
                        # Add, processed slice to eq_str
                        eq_str = eq_str + '(' + _eq + ')'
                    # Remove the processed slice and parenthesis from the
                    # eq_holder
                    eq_holder = eq_holder[closing_ind + 2:]

                # Is this following an operator?
                elif eq_str[-1] in operators or eq_str[-1] in ambi_operators:
                    # Slice the eq_holder to get the arguments between 
                    # parenthesis
                    expr_slice = eq_holder[1:]
                    expr_slice = expr_slice[:closing_ind - 1]
                    # Recurse this back through the function
                    _eq, _err, _dom = parse_partial_eq(expr_slice)
                    # Append the function domain into the arg_dom list
                    arg_dom.append(_dom)
                    # Append any errors to error list
                    err_list.append(_err)
                    # Check to see if the returned eq_str is non-empty as it is
                    # suppose to be
                    if not len(_eq) > 0:
                        err_list.append('Unexpected values, line 382')
                    else:
                        # Add, processed slice to eq_str
                        eq_str = eq_str + '(' + _eq + ')'
                    # Remove the processed slice and parenthesis from the
                    # eq_holder
                    eq_holder = eq_holder[closing_ind + 2:]

                # Is this following a func id?
                elif not last_func == '':
                    # Slice the eq_holder to get the arguments between 
                    # parenthesis
                    expr_slice = eq_holder[1:]
                    expr_slice = expr_slice[:closing_ind - 1]
                    # Recurse this back through the function
                    _eq, _err, _dom = parse_partial_eq(expr_slice, last_func, False, True)
                    # Append the function domain into the arg_dom list
                    arg_dom.append(_dom)
                    # Append any errors to error list
                    err_list.append(_err)
                    # Check to see if the returned eq_str is non-empty as it is
                    # suppose to be
                    if not len(_eq) > 0:
                        err_list.append('Unexpected values, line 382')
                    else:
                        # Add, processed slice to eq_str
                        eq_str = eq_str + '(' + _eq + ')'
                    # Remove the processed slice and parenthesis from the
                    # eq_holder
                    eq_holder = eq_holder[closing_ind + 2:]

                # Is this following a param/var id?
                elif not last_id == '':
                    # Slice the eq_holder to get the arguments between 
                    # parenthesis
                    dom_slice = eq_holder[1:]
                    dom_slice = dom_slice[:closing_ind - 1]
                    # Recurse this back through the function
                    _eq, _err, _dom = parse_partial_eq(dom_slice, in_dom=True)
                    # Append the function domain into the fxn_dom list
                    arg_dom.append(_dom)
                    # Append any errors to error list
                    err_list.append(_err)
                    # Check to see if the returned eq_str is empty as it is
                    # suppose to be
                    if len(_eq) > 0:
                        err_list.append('Unexpected values, line 382')
                    # Remove the processed slice and parenthesis from the
                    # eq_holder
                    eq_holder = eq_holder[closing_ind + 2:]

                # Otherwise, return an error
                else:
                    err_list.append('Unaccounted for "(" in ')


            # Is it a close paren?
            elif eq_holder[0] == ')':
                err_list.append('Unaccounted for ")" in ')
            else:
                error_msg = 'Unexpected character "'+ eq_holder[0] + '" in '
                err_list.append(error_msg)
    return eq_str, err_list, arg_dom

def parse_equation(eq):
    splitted = False
    rhs = ''
    lhs = ''
    comparison = ''
    if '=e=' in eq:
        temp = eq.partition('=e=')
        lhs = temp[0]
        comparison = temp[1]
        rhs = temp[2]
    elif '=g=' in eq:
        temp = eq.partition('=g=')
        lhs = temp[0]
        comparison = temp[1]
        rhs = temp[2]
    elif '=l=' in eq:
        temp = eq.partition('=l=')
        lhs = temp[0]
        comparison = temp[1]
        rhs = temp[2]
    elif '=n=' in eq:
        temp = eq.partition('=n=')
        lhs = temp[0]
        comparison = temp[1]
        rhs = temp[2]
    elif '=' in eq:
        temp = eq.partition('=')
        lhs = temp[0]
        comparison = temp[1]
        rhs = temp[2]
    else:
        return 'error!'
    rhs = parse_partial_equation(rhs)
    lhs = parse_partial_equation(lhs)
    comparison = comparison
    return (rhs, comparison, lhs)


"############################################################################"
">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
"                                   CLASSES                                  "
">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
"############################################################################"
