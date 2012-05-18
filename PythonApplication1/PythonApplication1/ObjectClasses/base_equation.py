from model_base import ModelBase
from fxn_conv_objects import GoodFunctionNames, BadFunctionNames
from fxn_conv_objects import FunctionInfo, IndexedFunctions, Domained

class BaseEquation(ModelBase):
    #################################################################
    ##                         Desciption:                         ##
    #################################################################
    """ This is the Base class for both Equations and Direct Assignments"""
    
    # These are the currently recognized function names that can be used in 
    # model codes

    #################################################################
    ##                 Initialize class attributes                 ##
    #################################################################
    def __init__(self, parent, id, args, type):
        ModelBase.__init__(self, parent, id, args[1], 'Equation')
        self.identifier = id
        self.domain = args[1]
        # These values should be of the form: (rel_path.module, function_name)
        self.imports = []
        self.eqn_slash_eqns = args[3]
        self.declared_variables = parent.declared_variables
        self.declared_parameters = parent.declared_parameters
        self.declared_equations = parent.declared_equations
        self.warning_list = []
        self.processed_eqs = []
        self.domain_checking = parent.domain_checking

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
        else:
            pass
        return
    #################################################################
    ##                     Process Class Data:                     ##
    #################################################################
    def __process__(self):
        for eq in self.eqn_slash_eqns:
            self.processed_eqs.append(parse_equation(eq))
    #################################################################
    ##                   Print to Python Script:                   ##
    #################################################################
    def __descr__(self):
        
        return 'work plz'
    #################################################################
    ##                       Helper Functions                      ##
    #################################################################
    def parse_equation(self, eq):
        args = self.split_equation(eq)
        lhs = arg[0]
        comparison = arg[1] # Comparison dictionary!
        rhs = arg[2]
        ldom, lhs = self.parse_domain(lhs)
        rdom, rhs = self.parse_domain(rhs)
        return (lhs, comparison, rhs)

    def parse_partial_domain(self, eq):

        pass

    def parse_domain(self, eq):
        # Initialize dependency dictionary
        dependency_dict = {}
        # Find the dependencies of the eq
        dependency_list = self.find_dependencies(eq)
        # Classify the dependencies of the eq
        for dependency in dependency_list:
            _d_class_ = classify_dependency(dependency)
            temp = {}

        return dom, p_str

    # string[''.find('id') + len('id'):] == what comes after what you are 
    # looking for use this with find dependencies to slice out the domains 
    # of things

    def func_dom(self, func, args):
        """ Takes the args and identifier of a function, args should not 
            include parentheses """
        # declare an empty function domain
        fxn_dom = []
        # split the args at commas without entering into nested parentheses 
        arg_list = self.level_split(args)
        # Check if func is in IndexedFunctions
        if func in IndexedFunctions:
        # If it is, remove the first arg from the arg_list and, after 
        # stripping and splitting, append to the function domain.
            fxn_dom.append(arg_list.pop(0).rstrip(')').lstrip('(').split(','))

        # Find the domain of the args, as well as their corrected string value
        dom, temp_str, err_list = list_dom(arg_list)

        # If the fxn_dom length equals zero, these values can be returned
        if len(fxn_dom) == 0:
            pass
        return dom, temp_str, err_list

    def arg_dom(self, arg):
        pass
        return dom, temp_str, err_list

    def list_dom(self, arg_list):
        # Initalize processed arg_list, p_args, and domain list, dom_list
        dom_list = []
        p_args = []
        # Initialize err_list
        err_list = []

        # Process each argument
        for item in arg_list:
            args = arg_dom(item)
            dom_list.append(args[0])
            p_args.append(args[1])
            err_list = err_list + args[2]
            pass
        
        return dom, temp_str, err_list

    def broadcast_match(self, l_dom, g_dom, l_str, g_str):
        # l_dom is the domain of the argument with the shorter domain
        for i in range(len(l_dom)):
            # this_id is the one to match
            this_id = l_dom[-i-1]
            # is this_id in g_dom?
            if not this_id in g_dom:
                # Return an error here
                pass
            else:
                # this_id is in g_dom, but is it already in the correct place?
                if not this_id == g_dom[-1-i]:
                    # if not in the correct place, swap the axes of the 
                    # correct id's index, with the correct index
                    g_str = g_str + swap_axes_str(-1-i, g_dom.index(this_id))
                    # make these changes to g_dom
                    g_dom[g_dom.index(this_id)] = g_dom[-1-i]
                    g_dom[-1-i] = this_id
        return g_dom, g_str

    def broadcast_match_list():
        pass

    def swap_axes_str(self, a1, a2):
        return '.swapaxes({v1},{v2})'.format(v1=a1, v2=a2)

    def find_dependencies(self, eq_str):
        dependency_list =[]
        temp_str = ''

        for char in eq_str:
            if char.isalpha():
                temp_str = ''.join([temp_str, char])
            elif not temp_str == '':
                if char.isdigit() or char == '_':
                    temp_str = ''.join([temp_str, char])
                else:
                    if not temp_str in dependency_list:
                        dependency_list.append(temp_str)
                    temp_str = ''

        if not temp_str == '':
            dependency_list.append(temp_str)

        return dependency_list

    def level_split(self, args_str):
        # args_str should be the arguments of a function without enclosing
        # parenthesis
        args = []
        i = 0
        while i in range(len(arg_str)):
            # Check if current character is a comma
            if args_str[i] == ',':
                args.append(args_str[:i-1])
                args_str = args_str[i:]
                i = 0
            # Check if current character is a '('
            elif args_str[i] == '(':
                temp = self.find_bracket_pair_index(args_str[i:])
                if not temp == None:
                    i = i + temp
            else:
                i = i + 1
        args.append(arg_str)
        return args

    def classify_dependency(self, dependency):
        if dependency in self.declared_variables.keys():
            classified_dependency = 'V'
        elif dependency in self.declared_parameters.keys():
            classified_dependency = 'P'
        elif dependency in IndexedFunctions:
            classified_dependency = 'I'
        elif dependency in GoodFunctionNames:
            classified_dependency = 'G'
        elif dependency in BadFunctionNames:
            classified_dependency = 'B'
        elif dependency in self.declared_equations.keys():
            classified_dependency = 'E'
        else:
            classified_dependency = 'U'
        return classified_dependency

    def split_equation(self, eq):
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
        return lhs, comparison, rhs
    

##############################################################################
##                               To do list:                                ##
##############################################################################
"""
1.
2.



"""
    

