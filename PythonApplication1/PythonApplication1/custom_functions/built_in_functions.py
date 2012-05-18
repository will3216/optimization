"###############################################################"#############
"###############################################################"#############
"###############################################################"#############
"###############################################################"#############
"###############################################################"#############
"###############################################################"#############
"###############################################################"#############
"###############################################################"#############
"###############################################################"#############
###                                                                        ###
###                                                                        ###
###    Customfxns:                                                         ###
###      An assortment of functions used to take the place of built-in     ###
###      GAMs functions once converted to python.  Note that there are     ###
###      two versions of each function. The one with np at the end of      ###
###      its name is for use with numpy objects.                           ###
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

from math import *
import numbers

"""
Functions in the module:

+ centropy(x)
+ div(dividend, divisor)
+ div0(dividend, divisor)
+ entropy(x)
+ logGamma(x)
+ map_val(x [,TOL])
+ sigmoid(x)
+ sign(x)

"""



##############################################################################

# Written, Verified, and Good to go



def div0(dividend, divisor):
    try:
        return dividend/divisor
    except:
        return math.pow(10,299)



def map_val(x, TOL=0.00000001):
    # Check if x is defined
    try:
        x
    except:
        # x is undefined
        return 4

    
    # Check if x is a number
    if isinstance(x, numbers.Number):
        
        if isnan(x):
            # x is NaN
            return 5  
        elif str(type(x)).startswith("<class 'complex'"):
            # x is a complex number
            return 9
        elif isinf(x):
            if sign(x) == -1:
                # x is negative infinitiy
                return 7
            else:
                # x is positive infinity
                return 6     
        elif x < TOL and x > -1*TOL and not x == 0:
            # very close to zero, but not zero
            return 8

        else:
            # x is a real number
            return 0 
    
        
    else:
        # x is defined, but not a numeric type
        return 10



def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    elif x == 0:
        return 0
    else:
        return x


##############################################################################

# Written, Verified, and in need of exception handling

def centropy(x, y, z=0):
    try:
        return x*log((x+z)/(y+z))
    except:
        raise

def div(dividend, divisor):
    try:
        return dividend/divisor
    except:
        raise

def entropy(x):
    try:
        return -x*math.log(x)
    except:
        raise




##############################################################################

# Need to write these functions

def logGamma(x):
    pass




def sigmoid(x):
    pass





        
