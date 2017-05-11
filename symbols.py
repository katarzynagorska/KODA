"""
KODA 17L: Team 4
Simple functions for encoding and decoding single symbols
Golomb encoding and decoding implementation based on
D. Salomon, "Data Compression. The Complete Reference", Springer, 2007.
"""

"""
function encoding single nonnegative integer depending on m-parameter
params:
    * int number: 	nonnegative integer we want to convert
    * int m:		m parameter of the Golomb Code
                            (m should depend on the probability p
                            and on the median of the run lengths)
returns:
    * string code:	Golomb encoded symbol
"""
def encode (number, m):
#Variables:
    #return string
    code = ""
    # Golomb code quptient
    q = math.floor(number/m)
    # Golomb code reminder
    
    return code
