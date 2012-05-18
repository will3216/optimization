from numpy import equal, multiply, add, divide, array, square, sqrt, float
from numpy import int, log, negative, power, subtract, logical_and, greater
from numpy import less_equal, absolute, copysign, not_equal, logical_not
from numpy import isnan, isinf, exp
import math

# Tests Passed
def div0(dividend, divisor):
    a = equal(divisor, 0).astype(float)
    multiply(a, 1E-350, a)
    add(divisor, a, a)
    return divide(dividend, a)


# Tests Passed: These do not work on non-narray types
def eDist1(a):
    b = square(a)
    sqrt(b, b)
    return b

def eDist2(a, b):
    c = square(a)
    d = square(b)
    add(c, d, c)
    return sqrt(c)

def eDist3(a, b, c):
    d = square(a)
    e = square(b)
    add(e, d, e)
    square(c, d)
    add(e, d, e)
    return sqrt(e)

def eDist4(a, b, c, f):
    d = square(a)
    e = square(b)
    add(e, d, e)
    square(c, d)
    add(e, d, e)
    square(f, d)
    add(e, d, e)
    return sqrt(e)

def eDist5(a, b, c, f, g):
    d = square(a)
    e = square(b)
    add(e, d, e)
    square(c, d)
    add(e, d, e)
    square(f, d)
    add(e, d, e)
    square(g, d)
    add(e, d, e)
    return sqrt(e)

def eDist6(a, b, c, f, g, h):
    d = square(a)
    e = square(b)
    add(e, d, e)
    square(c, d)
    add(e, d, e)
    square(f, d)
    add(e, d, e)
    square(g, d)
    add(e, d, e)
    square(h, d)
    add(e, d, e)
    return sqrt(e)

# Tests Passed: This does not work on non-narray types
def poly(x, a, b=None, c=None, d=None, e=None, f=None):
    
    m = 0
    y = a
    x1 = x
    if b == 0:
        multiply(x1, x, x1)
    else:
        multiply(x1, x, x1)
        multiply(x1, b, m)
        add(y, m, y)
    if c == None:
        return y
    else:
        if c == 0:
            multiply(x1, x, x1)
        else:
            multiply(x1, x, x1)
            multiply(x1, c, m)
            add(y, m, y)
        if d == None:
            return y
        else:
            if d == 0:
                multiply(x1, x, x1)
            else:
                multiply(x1, x, x1)
                multiply(x1, d, m)
                add(y, m, y)
            if e == None:
                return y
            else:
                if e == 0:
                    multiply(x1, x, x1)
                else:
                    multiply(x1, x, x1)
                    multiply(x1, e, m)
                    add(y, m, y)
        
                if f == None or f == 0:
                    return y
                else:
                    multiply(x1, x, x1)
                    multiply(x1, y, m)
                    add(y, m, y)


    return y

def signPower(x, y):
    s = copySign(x)
    z = absolute(x, y)
    power(x, y, z)
    return multiply(z, s)

def ifThen(cond, iftrue, iffalse):
    try:
        x = multiply(cond.astype(int), iftrue)
        y = logical_not(cond).astype(int)
        y = multiply(iffalse)
        return add(x, y)
    except:
        x = multiply(cond.astype(int), iftrue.astype(int)).astype(bool)
        y = logical_not(cond).astype(int)
        y = multiply(iffalse.astype(int))
        return add(x, y).astype(bool)
    

def bool_eqv(x, y):
    try:
        i = logical_xor(x, y)
        return logical_not(i, i)
    except:
        i = logical_xor(x.astype(bool), y.astype(bool))
        return logical_not(i, i)

def bool_imp(x, y):
    try:
        i = logical_not(x)
        return logical_and(i, y, i)
    except:
        i = logical_not(x.astype(bool))
        return logical_and(i, y.astype(bool), i)
    

# Tests Passed: This does not work on non-narray types
def entropy(x):
    y = log(x)
    multiply(x, y, y)
    return negative(y)


# Tests Passed: This does not work on non-narray types
def errorf(x):
    def gen_poly(x1, x2, x3, x4, x5, m, a, b, c, d, e, f):
        u = multiply(x1, b)
        y = add(u, a)
        multiply(x2, c, u)
        add(y, u, y)
        multiply(x3, d, u)
        add(y, u, y)
        multiply(x4, e, u)
        add(y, u, y)
        multiply(x5, f, u)
        add(y, u, y)
        return multiply(m, y)
    def gt_0_le_pt5(x1, x2, x3, x4, x5, m):
        a = 0.000000945872413752
        b = 1.12831546858388
        c = 0.00113863779463107
        d = -0.384371522137197
        e = 0.0270229903166182
        f = 0.0772638495545834
        return gen_poly(x1, x2, x3, x4, x5, m, a, b, c, d, e, f)
    def gt_pt5_le_1(x1, x2, x3, x4, x5, m):
        a = 0.00580403137043871
        b = 1.07826934703532
        c = 0.178821386660412
        d = -0.712205987932161
        e = 0.344221330992877
        f = -0.0522090550512075
        return gen_poly(x1, x2, x3, x4, x5, m, a, b, c, d, e, f)
    def gt_1_le_1pt5(x1, x2, x3, x4, x5, m):
        a = 0.0316427877098794
        b = 1.23127579461818
        c = -0.0627370140092589
        d = -0.532315375477541
        e = 0.28431191474665
        f = -0.0461922478862107
        return gen_poly(x1, x2, x3, x4, x5, m, a, b, c, d, e, f)
    def gt_1pt5_le_2(x1, x2, x3, x4, x5, m):
        a = -0.453195448626652
        b = 2.61260658446304
        c = -1.88564027426946
        d = 0.678865676708054
        e = -0.120860756118782
        f = 0.00839726021513343
        return gen_poly(x1, x2, x3, x4, x5, m, a, b, c, d, e, f)
    def gt_2_le_3(x1, x2, x3, x4, x5, m):
        a = -0.150919683363891
        b = 1.99850404725703
        c = -1.39899284756493
        d = 0.493013327857538
        e = -0.0873850146337645
        f = 0.0062269531772472
        return gen_poly(x1, x2, x3, x4, x5, m, a, b, c, d, e, f)
    def gt_3_le_3pt5(x1, x2, x3, x4, x5, m):
        a = 0.991452304282688
        b = 0.00746813288603762
        c = -0.00217815883931507
        d = 0.000212037911296648
        e = 0.0
        f = 0.0
        return gen_poly(x1, x2, x3, x4, x5, m, a, b, c, d, e, f)
    def gt_3pt5_le_4pt5(x1, x2, x3, x4, x5, m):
        a = 0.99880852294105
        b = 0.00114719941799862
        c = -0.000414026835425466
        d = 0.0000663763434567954
        e = -0.00000398825795855373
        f = 0.0
        return gen_poly(x1, x2, x3, x4, x5, m, a, b, c, d, e, f)
    def gt_4pt5(x1, x2, x3, x4, x5, m):        
        return m
    s = copysign(1, x)
    absolute(x, x)
    x1 = add(x, 0)
    x2 = power(x, 2)
    x3 = power(x, 3)
    x4 = power(x, 4)
    x5 = power(x, 5)
    m = logical_and(greater(x, 0), less_equal(x, 0.5))
    y = gt_0_le_pt5(x1, x2, x3, x4, x5, m.astype(int))
    logical_and(greater(x, 0.5), less_equal(x, 1), m)

    add(y, gt_pt5_le_1(x1, x2, x3, x4, x5, m.astype(int)), y)
    logical_and(greater(x, 1), less_equal(x, 1.5), m)

    add(y, gt_1_le_1pt5(x1, x2, x3, x4, x5, m.astype(int)), y)
    logical_and(greater(x, 1.5), less_equal(x, 2), m)

    add(y, gt_1pt5_le_2(x1, x2, x3, x4, x5, m.astype(int)), y)
    logical_and(greater(x, 2), less_equal(x, 3), m)

    add(y, gt_2_le_3(x1, x2, x3, x4, x5, m.astype(int)), y)
    logical_and(greater(x, 3), less_equal(x, 3.5), m)

    add(y, gt_3_le_3pt5(x1, x2, x3, x4, x5, m.astype(int)), y)
    logical_and(greater(x, 3.5), less_equal(x, 4.5), m)

    add(y, gt_3pt5_le_4pt5(x1, x2, x3, x4, x5, m.astype(int)), y)
    greater(x, 4.5, m)

    add(y, gt_4pt5(x1, x2, x3, x4, x5, m.astype(int)), y)
    return multiply(y, s)

# Tests Passed: This does not work on non-narray types
def fact(x):
    p = equal(x, 0)
    k = add(x, p)
    i = not_equal(k, 1).astype(int)
    z = 1
    while i.any().astype(bool):
        
        z = multiply(z, k)
        subtract(k, i, k)
        i = not_equal(k, 1).astype(int)

    return z


# Tests Passed: This does not work on non-narray types
def sigmoid(x):
    k = x
    negative(k, k)
    exp(k, k)
    add(k, 1, k)
    return divide(1, k, k) 




# Tests Passed: This does not work on non-narray types
def binomial(n, p):
    k = p
    i = not_equal(k, 0).astype(int)
    y = subtract(n, k)
    j = 0
    z = 1
    while i.any().astype(bool):
        j = j + 1
        subtract(k, i, k)
        y = subtract(n, k)
        multiply(y, i, y)
        l = logical_not(i.astype(bool)).astype(int)
        x = divide(y, j)
        add(x, l, x)
        z = multiply(z, x)
        i = not_equal(k, 0).astype(int)

    return z

# Tests Passed: This does not work on non-narray types
def centropy(x, y, z= 0):
    i = add(x, z)
    j = add(y, z)
    divide(i, j, i)
    log(i, i)
    multiply(i, x, i)
    return i

# Tests Passed: This does not work on non-narray types
def mapVal(x):
    i = isnan(x).astype(int)
    multiply(i, 5, i)
    j = isinf(x).astype(int)
    k = x.__lt__(0).astype(int)
    multiply(j, k, k)
    multiply(k, 7, k)
    add(i, k, i)
    k = logical_not(x.__lt__(0)).astype(int)
    multiply(j, k, k)
    multiply(k, 6, k)
    add(i, k, i)
    k = logical_and(not_equal(x, 0), 
                    logical_and(x.__lt__(0.0000001), 
                                x.__gt__(-0.0000001))).astype(int)
    multiply(k, 8, k)
    add(i, k, i)
    return i

def sum(domain, array):
    

    pass

def test():
    a = array([5.0,1.0,2.0,5.0,4.0,2.0,6.0,8.0])
    b = array([1.0,1.0,0.0,1.0,2.0,1.0,4.0,5.0])
    #a = float(1.0)
    #b = int(2.0)
    
    
    c = sigmoid(b)
    print type(c)
    return c
