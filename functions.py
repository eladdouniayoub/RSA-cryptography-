import json
from math import gcd
from egcd import egcd


def alphabetIndex(char):
	return ord(char.upper())-65

def indexAlphabet(index):
	return chr(65+index)

def comput_N(PNumber,QNumber):
    return PNumber * QNumber


def indexEuler(PNumber,QNumber):
    return (PNumber-1)*(QNumber-1)

def nbr_Premier_Euler(PNumber,QNumber):
    indEuler =(PNumber-1)*(QNumber-1)
    Dic = []
    for x in range(2,indEuler):
        if gcd(x,indEuler)==1:    
            Dic.append(x)
        else:
            pass
    return Dic

def modinv(Nbr_choisi, IndEuler):
    g, x, y = egcd(Nbr_choisi, IndEuler)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % IndEuler


def crypter(Text, Public_key1, Public_key2):
	indexes = [ ]
	for char in Text:
		num = alphabetIndex(char)
		num_pow = num**Public_key1
		num_pow_res = num_pow % Public_key2
		indexes.append(num_pow_res)
	chars = [ ]
	for index in indexes:
		char = indexAlphabet(index)
		chars.append(char)
	return chars
		
