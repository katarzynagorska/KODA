"""
KODA 17L: Team 4
Simple functions for encoding and decoding single symbols
Golomb encoding and decoding implementation based on
D. Salomon, "Data Compression. The Complete Reference", Springer, 2007.
"""
import math


"""
function encoding single nonnegative integer 
params:
    * int n: 		Nonnegative integer we want to convert
returns:
    * str code:	Unary encoded symbol
"""
def unaryEncode (n):
    # Checking arguments:
    if not type(n) is int:
        raise TypeError('n must be an integer not a ', str(type(n)))
    if n < 0:
        raise ValueError('n must be a nonnegative integer')

    # Unary encoded n 1...10
    code = "1" * n + "0"    
    return code


"""
function decoding unary code 
params:
    str code: 		Unary code of symbol
returns:
    int n:     	Decoded number
"""
def unaryDecode(code):
    # Checking arguments:
    if not type(code) is str:
        raise TypeError('code must be a str, not a ', str(type(code)))
    if code.count('0') != 1 \
       or code[len(code)-1] != '0'\
       or not all(c in '01' for c in code):
        raise ValueError('Invalid unary code: ', code)

    # Decoding:
    n = len(code)-1
    return n


"""
function encoding non negative integer returning binary string
params:
    int n 		: Nonegative integer
    int c 		: Fixed number of bytes
returns:
    str code	: binary encoded string (fixed length)
"""
def binaryEncode(n,c):
    # TODO Checking arguments:
    # if c is not big enough
    # if wrong types
    # if wrong values (n<0)

    # Encodnig
    code = '{0:{fill}{width}b}'.format(n, fill= '0', width=c)
    return code 

"""
function decoding binary number
params:
    str code : 	Binary encoded string (fixed length)   
returns:
      int n : 		Nonnegative integer  
"""
def binaryDecode(code):
    # TODO Checking arguments:

    # Decodnig
    n = int(code, 2)
    return n


"""
function encoding single nonnegative integer depending on m-parameter
params:
    int n: 		Nonnegative integer we want to convert
    int m:		M parameter of the Golomb code
						* here m > 0
						* m should depend on the probability p
						  and on the median of the run lengths            
returns:
    str code:	Golomb code of n
"""
def golombEncode(n, m):
    # TODO Checking parameters:

    # Encoding
    if m == 1:
        code = unaryEncode(n)     
    else:
        q = math.floor(n/m)     		# Golomb code quotient
        r = n - q*m 					# Golomb code reminder  
        c = math.ceil(math.log2(m)) 	# Golomb code c
										
        if m == math.pow(2,c):
            code = unaryEncode(q) +'|'+ binaryEncode(r,c)
        else :
            if r < math.pow(2,c)-m:
                code = unaryEncode(q) + '|' + binaryEncode(r,c-1)
            else:
                code = unaryEncode(q) + '|'+ binaryEncode(r+1,c)    
    return code
"""
function decoding single Golmb code for given m-parameter
params:
    str code : Golomb code of symbol
    int m : M-parameter of Golomb code
returns:
    int n : Decoded number
"""
def golombDecode(code,m):
# TODO Checking arguments:
    if type(code) != str:
        errMsg = "code must be a str, not a"+str(type(code))
        raise TypeError(errMsg)

    # Decoding
    if m == 1 :
        n = unaryDecode(code)
    else:
        #split after first occurence of zero (the end of unary quotient)
        code = code.replace('|','')
        Q = unaryDecode(code.split('0',1)[0]+'0')      
        R = binaryDecode(code.split('0',1)[1])
        c = math.ceil(math.log2(m))
        
        # n = r + q*m
        if m == math.pow(2,c):
            n = Q*m+R
        else:
            if R < math.pow(2,c)-m:
                n = Q*m+R
            else:
                n = Q*m+R-1
    return n

"""
Testing
"""
def main():
    for m in range(1,8):
        print("m = ", m)
        for n in range(0,11):
           code = golombEncode(n,m)
           decode = golombDecode(code,m)
           print(n,":\t",code,"\t",decode)

        
if __name__ == '__main__':
     main()
# TODO @parsowanie plików: liczby dwucyfrowe
