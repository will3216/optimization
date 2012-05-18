# This is a list of working function names that can be used in the GAMS parser
GoodFunctionNames = [
                    'sum',          #custom_np_fxns.sum
                    'prod',         #custom_np_fxns.prod
                    'smin',         #custom_np_fxns.smin
                    'smax',         #custom_np_fxns.smax
                    'abs',          #numpy.absolute
                    'arccos',       #numpy.arccos
                    'arcsin',       #numpy.arcsin
                    'arctan',       #numpy.arctan
                    'arctan2',      #numpy.arctan2
                    'Beta',         #scipy.special.beta
                    'binomial',     #custom_np_fxns.binomial
                    'ceil',         #numpy.ceil
                    'centropy',     #custom_np_fxns.centropy
                    'cos',          #numpy.cos
                    'cosh',         #numpy.cosh
                    'cvPower',      #numpy.power
                    'div',          #numpy.true_divide
                    'div0',         #custom_np_fxns.div0
                    'eDist',        #custom_np_fxns.eDist#***
                    'entropy',      #custom_np_fxns.entropy
                    'errorf',       #scipy.special.erf
                    'exp',          #numpy.exp
                    'fact',         #custom_np_fxns.fact
                    'floor',        #numpy.floor
                    'frac',         #numpy.remainder
                    'gamma',        #scipy.special.gamma
                    'log',          #numpy.log
                    'logBeta',      #scipy.special.betaln
                    'logGamma',     #scipy.special.gammaln
                    'log10',        #numpy.log10
                    'log2',         #numpy.log2
                    'mapVal',       #custom_np_fxns.mapVal
                    'max',          #numpy.max***
                    'min',          #numpy.min***
                    'mod',          #numpy.mod
                    'normal',       #scipy.stats.norm.rvs
                    'pi',           #math.pi
                    'poly',         #custom_np_fxns.poly
                    'power',        #numpy.power
                    'randBinomial', #scipy.stats.binom.rvs
                    'randTriang',   #scipy.stats.triang.rvs
                    'round',        #numpy.rint ***
                    'rPower',       #numpy.power
                    'sigmoid',      #custom_np_fxns.sigmoid
                    'sign',         #numpy.sign
                    'signPower',    #custom_np_fxns.signPower
                    'sin',          #numpy.sin
                    'sinh',         #numpy.sinh
                    'sqr',          #numpy.square
                    'sqrt',         #numpy.sqrt
                    'tan',          #numpy.tan
                    'tanh',         #numpy.tanh
                    'trunc',        #numpy.rint
                    'uniform',      #scipy.stats.uniform.rvs
                    'vcPower',      #numpy.power
                    'bool_and',     #numpy.logical_and
                    'bool_eqv',     #custom_np_fxns.bool_eqv
                    'bool_imp',     #custom_np_fxns.bool_imp
                    'bool_not',     #numpy.logical_not
                    'bool_or',      #numpy.logical_or
                    'bool_xor',     #numpy.logical_xor
                    'ifThen',       #custom_np_fxns.ifThen
                    'rel_eq',       #numpy.equal
                    'rel_ge',       #numpy.greater_equal
                    'rel_gt',       #numpy.greater
                    'rel_le',       #numpy.less_equal
                    'rel_lt',       #numpy.less
                    'rel_ne',       #numpy.not_equal
]    

# Parameter Class types that have a domain attribute
Domained = ['Param List','Table','Direct Assign', 'Variable']

# Functions that provide indexes as arguments for calculation
IndexedFunctions = ['sum','prod','smin','smax']

# Processing info and arguments for supported functions, add equations here
FunctionInfo = [
        ######################################################################
        # PROCESS:
        # In the process column, 'i' stands for an indexed function, '*' 
        # stands for a function whose package name does not match its GAMs 
        # name, 'm' means that it accepts a variety of argument numbers, and 
        # '' means no special treatment is required.
        ######################################################################
        # ARGS:
        # In the args column, a positive number represents the expected number
        # of arguments. A negative number represents a function that takes
        # n arguments, and the absolute value is the minimum required number 
        # of arguments. 
        ######################################################################
        # (GAMS name ::  Function Package :: Package Name :: Process :: Args),
        ######################################################################
            {'sum':          ('custom_np_fxns', 'sum',           'i',    2)},
            {'prod':         ('custom_np_fxns', 'prod',          'i',    2)},
            {'smin':         ('custom_np_fxns', 'smin',          'i',    2)},
            {'smax':         ('custom_np_fxns', 'smax',          'i',    2)},
            {'abs':          ('numpy',          'absolute',      '*',    1)},
            {'arccos':       ('numpy',          'arccos',        '',     1)},
            {'arcsin':       ('numpy',          'arcsin',        '',     1)},
            {'arctan':       ('numpy',          'arctan',        '',     1)},
            {'arctan2':      ('numpy',          'arctan2',       '',     1)},
            {'Beta':         ('scipy.special',  'beta',          '*',    2)},
            {'binomial':     ('custom_np_fxns', 'binomial',      '',     2)},
            {'ceil':         ('numpy',          'ceil',          '',     1)},
            {'centropy':     ('custom_np_fxns', 'centropy',      'm',    None)},
            {'centropy2':    ('custom_np_fxns', 'centropy',      '*',    2)},
            {'centropy3':    ('custom_np_fxns', 'centropy',      '*',    3)},
            {'cos':          ('numpy',          'cos',           '',     1)},
            {'cosh':         ('numpy',          'cosh',          '',     1)},
            {'cvPower':      ('numpy',          'power',         '*',    2)},
            {'div':          ('numpy',          'true_divide',   '*',    2)},
            {'div0':         ('custom_np_fxns', 'div0',          '',     2)},
            {'eDist':        ('custom_np_fxns', 'eDist',         'm',    None)},
            {'eDist1':       ('custom_np_fxns', 'eDist1',        '*',    1)},
            {'eDist2':       ('custom_np_fxns', 'eDist2',        '*',    2)},
            {'eDist3':       ('custom_np_fxns', 'eDist3',        '*',    3)},
            {'eDist4':       ('custom_np_fxns', 'eDist4',        '*',    4)},
            {'eDist5':       ('custom_np_fxns', 'eDist5',        '*',    5)},
            {'eDist6':       ('custom_np_fxns', 'eDist6',        '*',    6)},
            {'entropy':      ('custom_np_fxns', 'entropy',       '',     1)},
            {'errorf':       ('scipy.special',  'erf',           '*',    1)},
            {'exp':          ('numpy',          'exp',           '',     1)},
            {'fact':         ('custom_np_fxns', 'fact',          '',     1)},
            {'floor':        ('numpy',          'floor',         '',     1)},
            {'frac':         ('numpy',          'remainder',     '*',    1)},
            {'gamma':        ('scipy.special',  'gamma',         '',     1)},
            {'log':          ('numpy',          'log',           '',     1)},
            {'logBeta':      ('scipy.special',  'betaln',        '*',    2)},
            {'logGamma':     ('scipy.special',  'gammaln',       '*',    1)},
            {'log10':        ('numpy',          'log10',         '',     1)},
            {'log2':         ('numpy',          'log2',          '',     1)},
            {'mapVal':       ('custom_np_fxns', 'mapVal',        '',     1)},
            {'max':          ('custom_np_fxns', 'max',           'max', -1)},
            {'min':          ('custom_np_fxns', 'min',           'min', -1)},
            {'mod':          ('numpy',          'mod',           '',     1)},
            {'normal':       ('scipy.stats',    'norm.rvs',      '*',    2)},
            {'pi':           ('math',           'pi',            '',     0)},
            {'poly':         ('custom_np_fxns', 'poly',          'm',    None)},
            {'poly2':        ('custom_np_fxns', 'poly',          '*',    2)},
            {'poly3':        ('custom_np_fxns', 'poly',          '*',    3)},
            {'poly4':        ('custom_np_fxns', 'poly',          '*',    4)},
            {'poly5':        ('custom_np_fxns', 'poly',          '*',    5)},
            {'poly6':        ('custom_np_fxns', 'poly',          '*',    6)},
            {'poly7':        ('custom_np_fxns', 'poly',          '*',    7)},
            {'power':        ('numpy',          'power',         '',     2)},
            {'randBinomial': ('scipy.stats',    'binom.rvs',     '*',    2)},
            {'randTriang':   ('scipy.stats',    'triang.rvs',    '*',    3)},
            {'round':        ('numpy',          'rint',          '*',    1)},
            {'rPower':       ('numpy',          'power',         '*',    2)},
            {'sigmoid':      ('custom_np_fxns', 'sigmoid',       '',     1)},
            {'sign':         ('numpy',          'sign',          '',     1)},
            {'signPower':    ('custom_np_fxns', 'signPower',     '',     2)},
            {'sin':          ('numpy',          'sin',           '',     1)},
            {'sinh':         ('numpy',          'sinh',          '',     1)},
            {'sqr':          ('numpy',          'square',        '*',    1)},
            {'sqrt':         ('numpy',          'sqrt',          '',     1)},
            {'tan':          ('numpy',          'tan',           '',     1)},
            {'tanh':         ('numpy',          'tanh',          '',     1)},
            {'trunc':        ('numpy',          'rint',          '*',    1)},
            {'uniform':      ('scipy.stats',    'uniform.rvs',   '*',    2)},
            {'vcPower':      ('numpy',          'power',         '*',    2)},
            {'bool_and':     ('numpy',          'logical_and',   '*',    2)},
            {'bool_eqv':     ('custom_np_fxns', 'bool_eqv',      '',     2)},
            {'bool_imp':     ('custom_np_fxns', 'bool_imp',      '',     2)},
            {'bool_not':     ('numpy',          'logical_not',   '*',    1)},
            {'bool_or':      ('numpy',          'logical_or',    '*',    2)},
            {'bool_xor':     ('numpy',          'logical_xor',   '*',    2)},
            {'ifThen':       ('custom_np_fxns', 'ifThen',        '',     3)},
            {'rel_eq':       ('numpy',          'equal',         '*',    2)},
            {'rel_ge':       ('numpy',          'greater_equal', '*',    2)},
            {'rel_gt':       ('numpy',          'greater',       '*',    2)},
            {'rel_le':       ('numpy',          'less_equal',    '*',    2)},
            {'rel_lt':       ('numpy',          'less',          '*',    2)},
            {'rel_ne':       ('numpy',          'not_equal',     '*',    2)}
]    

BadFunctionNames = [
                    'betaReg',      #
                    'execSeed',     #
                    'gammaReg',     #
                    'ncpF',         #
                    'ncpCM',        #
                    'ncpVUpow',     #
                    'ncpVUsin',     #
                    'randLinear',   #
                    'slexp',        #
                    'sllog10',      #
                    'slrec',        #
                    'sqexp',        #
                    'sqlog10',      #
                    'sqrec',        #
                    'uniformInt',   #
]    
