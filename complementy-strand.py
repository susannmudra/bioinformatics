input = "GATTACA"

def ReverseComplement(Pattern):
    Pattern = Reverse(Pattern) # reverse all letters in a string
    Pattern = Complement(Pattern) # complement each letter in a string
    return Pattern

def Reverse(Pattern):
    rev = ""
    for x in Pattern:
        rev = x + rev
    return(rev)    

def Complement(Pattern):
    comp = ""
    for x in Pattern:
        if x=="A":
            comp = comp + "T"
        if x=="T":
            comp = comp + "A"
        if x=="C":
            comp = comp + "G"
        if x=="G":
            comp = comp + "C"
    return(comp)


def Reverse(Pattern):
    rev = ""
    for x in Pattern:
        rev = x + rev
    return(rev)

print(ReverseComplement(input))
