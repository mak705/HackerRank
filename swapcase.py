def swap_case(s):
    a = ""
    for let in s:
        if let.isupper() == True:
            a+=(let.lower())
        else:
            a+=(let.upper())
    return a
    
print ''.join([i.lower() if i.isupper() else i.upper() for i in input()])

def swap_case(s):    
    return s.swapcase()
