
from fxn_conv_objects import BadFunctionNames, FunctionInfo, GoodFunctionNames
from model_base import ModelBase


class TestClass(ModelBase):
    DeclaredVariables = {'x':'', 'z':''}
    DeclaredParameters = {'i':'', 'j':'', 'a':'', 'b':'', 'd':'', 'f':'', 'c':''}
    DeclaredEquations = {'cost':'', 'supply':'', 'demand':''}
    test_set = [
            ' sum(j, x(i,j)) =l= a(i)',
            ' sum(i, x(i,j)) =g= b(j)',
            'c(i,j) = f*d(i,j)/1000'

    ]
    def __init__(self):
        self.declared_variables = DeclaredVariables
        self.declared_parameters = DeclaredParameters
        self.declared_equations = DeclaredEquations
        self.warning_list = {}
        self.last_func = ''
        self.last_id = ''
        return

    



    def parse_equation(self, eq):
        # Remove all whitespace from the equation
        eq = remove_all_whitespace(eq)
        # Split the equation at the comparison
        split_eq = split_equation(eq)
        # Check to see if the split was successful (had a comparison or equality
        # to split on)
        if not split_eq == 'error!':
            # Save each portion separately
            lhs, comparison, rhs = split_eq
        else:
            # Pass the error back
            return split_eq

        # Process the equation's left-hand side, lhs
        lhs, errors = self.parse_partial_eq(lhs)

        return lhs, errors

    def remove_all_whitespace(self, eq):
        eq_holder = eq
        eq_holder = eq_holder.replace(' ','').replace('\n','').replace('\t','')
        return eq_holder

    def find_bracket_pair_index(self, sts):
        # sts is the string to search, it should not include the opening bracket
        bracket_level = 1
        index_count = 0
        while bracket_level > 0 and index_count <= len(sts):
            if sts[index_count] == ')':
                bracket_level = bracket_level - 1
            elif sts[index_count] == '(':
                bracket_level = bracket_level + 1
            index_count = index_count + 1
        if bracket_level == 0:
            return index_count
        else:
            return None
      
    def all_in_all(list1, list2):
        # Check if the two lists have the same length
        if len(list1) == len(list2):
            # Return the string '1' if the lengths do not match
            return '1'
        # Check if all of the elements in list1 are in list2
        for item in list1:
            # Check if some of the items don't match
            if not item in list2:
                # Return the string '2' if not all of the items in list1 are
                # in list2
                return '2'
        # Check if the order doesn't match
        if not list1 == list2:
            # Return the string '3' if not all of the items in list1 are in
            # same position as in list2
            return '3'
        else:
            # Return the string '0' if the two lists match
            return '0'

    def compare_g_and_e_doms(self, eq_holder, e_dom):
        dom = []
        err_list = []
        # If a domain is expected find the domain, otherwise
        # report an error.
        if len(e_dom) > 0:
            # Create a temporary slice to find the closing indice
            # with
            eq_holder = eq_holder[1:]
            # Find the closing indice of the given domain
            _ci = self.find_bracket_pair_index(eq_holder)
            # Check if a closing paren was found
            if _ci == None:
                msg1 = '' # ADD_MSG!@! : no closing paren
                err_list.append(msg1)
            # Slice the domain from the eq_holder string
            temp_slice = eq_holder[:_ci - 1]
            # Convert the slice into a list
            g_dom = temp_slice.split(',')
            # Remove domain slice from eq_holder string
            eq_holder = eq_holder[:_ci]
            # Compare the expected domain with the given 
            # domain
            dom_test = all_in_all(g_dom, e_dom)
            if not dom_test == '0':
                # Make error message for each case
                msg1 = '' # ADD_MSG!@! : domain lengths
                # do not match
                msg2 = '' # ADD_MSG!@! : not all values
                # in the expected and given domains match
                msg3 = '' # ADD_MSG!@! : the order of the 
                # the values in the expected and given 
                # domains do not match 
                err_dict = {
                            '1':msg1,
                            '2':msg2,
                            '3':msg3}

                error_msg = err_dict[dom_test]
                err_list.append(error_msg)

            else:
                dom = e_dom

        else:
            # if expecting a domain return an error, otherwise
            # awesome!
            error_msg = '' # ADD_MSG!@! : Domain found, no domain 
            # expected. Check for missing '*'
            err_list.append(error_msg)
        return eq_holder, err_list, dom

    def check_domained(self, eq_holder, holder_str):
        dom = []
        err_list = []
        # Look at the object of the identifier to find the expected domain
        e_dom = self.parent.objects[holder_str].domain
                        
        # Check that an open parenthesis is the next character
        if '(' == eq_holder[0]:
            # Compare the expected and given domains
            args = compare_e_and_g_doms(eq_holder, e_dom)
            # Set the eq_holder to equal what is left after
            # the removal of the domain
            eq_holder = args[0]
            # Append any errors to the list
            err_list.append(args[1])
            # Set the domain equal to the domain from the
            # comparison
            dom = arg[2]
                            
        else:
            # Check if a domain was expected
            if len(e_dom) > 0:
                # Return an error, expected domain not given
                error_msg = ''
                err_list.append(error_msg)
        # Return values
        return eq_holder, err_list, dom

    def check_undomained(self, eq_holder, holder_str):
        dom = []
        err_list = []
                                
        # Check that an open parenthesis is the next character
        if '(' == eq_holder[0]:
            # Return an error message for the unexpected presence of a domain 
            # specification
            error_msg = '' # ADD_MSG!@! : Domain found, no domain 
            # expected. Check for missing '*'
                            
        return eq_holder, err_list, dom



    """ This assumes an ideally specified domain """
    def dom_list_adheres(self, dom_list, overall_domain = False):
        templist = dom_list
        longest = 0
        master_domain = []
        # Find the longest domain
        for domain in dom_list:
            if len(domain) > longest:
                longest = len(domain)
                master_domain = domain
        # Return just the master_domain if specified
        if overall_domain:
            return master_domain

        # Check that all domains in list satisfy broadcasting rules
        test_complete = False
        while len(master_domain) > 0:
            remove_set = master_domain.pop()
            for i in range(len(templist)):
                if len(templist[i]) == 0:
                    'nothing'
                elif templist[i][-1] == remove_set:
                    templist[i].pop()
                else:
                    # Return False
                    return False
        
        
        return True

    def build_function(self, eq_holder, holder_str):
        # Find the closing index for the function
        _cli = self.find_bracket_pair_index(eq_holder[1:])
        # Check if a closing paren was found
        if _cli == None:
            msg1 = '' # ADD_MSG!@! : no closing paren
            err_list.append(msg1)
        # Split args at un-nested commas
        args = level_split(eq_holder[1:_cli])
        # Remove function arguments from eq_holder
        eq_holder = eq_holder[_cli + 2:]
        # Initialize local variables
        p_args = []
        p_err_list = []

        # Get the information on this function
        info = FunctionInfo[holder_str]
        # Process type 'm' functions by getting the corrected name
        if info[2] == 'm':
            # Corrected name
            new_name = holder_str + str(len(args) + 1)
            # Correct info
            info = FunctionInfo[new_name]
        # Add required imports to list
        self.imports.append((info[0],info[1]))
        # Save information regarding processing
        process = info[2]
        # Save information regarding expected number of arguments
        e_args = info[3]

        # Parse each argument in args
        for arg in args:
            p_arg, p_errs = self.parse_partial_eq(arg)
            p_args.append(p_args)
            p_err_list = p_err_list + p_errs
            
                
        # Check that the expected and given number of arguments agree
        if not e_args == len(p_args):
            # Return an error if they do not
            # ADD_MSG!@!
            pass
                    
        # Make a string for the body which adds the parenthesis which were 
        # removed
        temp_str = info[1] + '(' + ','.join(p_args) + ')'
        return temp_str, p_err_list, eq_holder

    def build_identifier(self, eq_holder, holder_str):
        id_built = False
        eq_str = ''
        err_list = []
        
        while not id_built:
        # Are we building an id?
            # Is the current character alphanumeric?
            if eq_holder[0].isalnum():
                holder_str = holder_str + eq_holder[0]
                eq_holder = eq_holder[1:]
            # Is the current character an underschore?
            elif eq_holder[0] == '_':
                holder_str = holder_str + eq_holder[0]
                eq_holder = eq_holder[1:]
            
            # Is this an indexed function argument?
            elif eq_holder[0] == '=':
                # Check if the holder_str is equal to 'axes'
                if holder_str == 'axes':
                    # Add the equal sign to the holder_str
                    holder_str = holder_str + eq_holder[0]
                    # Remove it from the eq_holder
                    eq_holder = eq_holder[1:]
                    # Grab the first number
                    if eq_holder[0].isdigit():
                        # Build the number
                        args = build_number(eq_holder[1:], eq_holder[0])
                        holder_str = holder_str + args[0]
                        err_list = err_list + args[1]
                        eq_holder = args[2]
                    else:
                        # Return an error
                        pass
            else:
                # Classify the newly built id
                c_id = self.classify_dependency(holder_str)
                
                # If this is a function, process it!                
                if c_id == 'G':
                    args = self.build_function(eq_holder, holder_str)
                    holder_str = holder_str + args[0]
                    err_list = err_list + args[1]
                    eq_holder = args[2]
                # If this is a bad function, return error
                elif c_id == 'B':
                    error_msg = 'The GAMS function identifier "'
                    error_msg = error_msg + holder_str + '" is not curren'
                    error_msg = error_msg + 'tly supported, in :'
                    err_list = err_list.append(error_msg)
                    return holder_str, err_list, eq_holder
                # If this is an equation, return error
                elif c_id == 'E':
                    warning_msg = 'Could not determine what to do with id'
                    warning_msg = warning_msg + 'entifier "' + holder_str
                    warning_msg = warning_msg + '" in :'
                    self.warning_list.append(warning_msg)
                    return holder_str, err_list, eq_holder
                # If this is an unidentifiable identifier, return error
                elif c_id == 'U':
                    warning_msg = 'Could not determine type of ident'
                    warning_msg = warning_msg + 'ifier "' + holder_str
                    warning_msg = warning_msg + '" in :'
                    self.warning_list.append(warning_msg)
                    return holder_str, err_list, eq_holder
                
                return holder_str, err_list, eq_holder
                    
    def build_number(self, eq_holder, holder_str):
        num_str = holder_str
        building_num = True
        err_list = []
        while building_num:
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
                # End the building string process
                building_num = False
        return num_str, err_list, eq_holder 

    def parse_partial_eq(self, eq):
        operators = ['+','-','/']
        ambi_operators = ['*','**']
    
        # Initialize local variables
        eq_str = ''
        holder_str = ''
        err_list = []
    
        while len(eq_holder) > 0 and not len(err_list) > 0:
            # What are we building?
            if len(holder_str) == 0:
                # Is it a new ID?
                if eq_holder[0].isalpha():
                    # Add current char to id holder
                    holder_str = eq_holder[0]
                    # Remove current char from eq_holder
                    eq_holder = eq_holder[1:]
                    args = self.build_identifier(eq_holder, holder_str)
                    eq_str = eq_str + args[0]
                    err_list = err_list + args[1]
                    eq_holder = args[2]
                    holder_str = ''

                # Is it a new num?
                elif eq_holder[0].isdigit():
                    # Add current char to holder
                    holder_str = eq_holder[0]
                    # Remove current char from eq_holder
                    eq_holder = eq_holder[1:]
                    args = self.build_number(eq_holder, holder_str)
                    eq_str = eq_str + args[0]
                    err_list = err_list + args[1]
                    eq_holder = args[2]
                    holder_str = ''

                # Is it an operator?
                elif eq_holder[0] in operators:
                    # Check to see if this is the first char to be added to 
                    # the arg
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
                    # Check to see if this is the first char to be added to 
                    # eq_str
                    if len(eq_str) == 0:
                        # Return error, because you cannot start an expression
                        # with *
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
            
                # Is the current character a period?
                elif eq_holder[0] == '.':
                    # Add current character to holder_str
                    holder_str = holder_str + eq_holder[0]
                    # Remove current character from eq_holder
                    eq_holder = eq_holder[1:]
                    # Is this an axes swap?
                    if eq_holder.startswith('swapaxes'):
                        # Add the 'swapaxes(' to holder_str
                        holder_str = holder_str + eq_holder[:9]
                        # Remove the 'swapaxes(' from eq_holder
                        eq_holder = eq_holder[9:]
                        # Find the closing paren
                        _cli = self.find_bracket_pair_index(eq_holder)
                        # Check if a closing paren indice was found
                        if not _cli == None:
                            # Add the swap arguments to the holder_str
                            holder_str = holder_str + eq_holder[:_cli + 1]
                            # Remove the swap arguments from the eq_holder
                            eq_holder = eq_holder[_cli + 1:]
                        else:
                            # Return an error
                            pass
                    else:
                        # Add warning about sending a python function through a GAMS
                        # Parser
                        warning_msg = 'Python module specification may not '
                        warning_msg = warning_msg + 'convert correctly in '
                        self.warning_list.append(warning_msg)

                # Is it a new str?
                elif eq_holder[0] == "'" or eq_holder == '"':
                    # All strings should be removed by now
                    err_msg = 'Unexpected "' + eq_holder[0] 
                    err_msg = err_msg + '" in '
                    err_list.append(err_msg)
                   
                # Is it a comma?
                elif eq_holder[0] == ',':
                    # In a function?
                    error_msg = 'Unexpected "," in '
                    err_list.append(error_msg)


                # Is it an open paren?
                elif eq_holder[0] == '(':
                    # Find closing indice
                    closing_ind = self.find_bracket_pair_index(eq_holder[1:])
                    # Check to see if a closing indice was found
                    if closing_ind == None:
                        err_list.append('Could not find a closing paren in ')
                    # Slice the eq_holder to get the arguments between 
                    # parenthesis
                    expr_slice = eq_holder[1:]
                    expr_slice = expr_slice[:closing_ind - 1]

                    # Is this at the beginning of a new expression?
                    if eq_str == '':
                        # Recurse this slice back through the function
                        _eq, _err = parse_partial_eq(expr_slice)
                        # Append any errors to error list
                        err_list= err_list + _err
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
                        # Recurse this back through the function
                        _eq, _err = parse_partial_eq(expr_slice)
                        # Append any errors to error list
                        err_list = err_list + _err
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

                    # Otherwise, return an error
                    else:
                        err_list.append('Unaccounted for "(" in ')


                # Is it a close paren?
                elif eq_holder[0] == ')':
                    err_list.append('Unaccounted for ")" in ')
                else:
                    error_msg = 'Unexpected character "'+ eq_holder[0] + '" in '
                    err_list.append(error_msg)
        return eq_str, err_list





def test(test_set):
   
    for i in test_set:
        print parse_equation(i)