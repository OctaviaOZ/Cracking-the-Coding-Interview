from typing import List

def isunique_str(s: str) -> bool:
    
    if len(s) > 128: # ASCII
        return False
        
    if len(set(s)) != len(s):
        return False
        
    return True  

def isunique_str1(s: str) -> bool:
    for l in s:
        if s.count(l) > 1:
            return False
        
    return True 

def ispermut_str(s1: str, s2: str) -> bool:
    
    if len(s1) != len(s2):
        return False
    
    if sorted(s1) != sorted(s2):
        return False
        
    return True 

def replace_space(s: str) -> str:
        
    return s.strip().replace(' ', '%20')  


def count_palidrom(s: str) -> bool:
    
    #in polinrom each litera have to be even and some case one in middle
    s = s.replace(' ', '').upper()
    
    onlyonecase = 0
    for l in set(s):
        if (s.count(l) % 2 != 0):
            onlyonecase += 1
        
        if onlyonecase > 1:
            return False
        
    return True     

# insert, delete, replace
def dist_one_modefication(s1: str, s2: str) -> bool:
           
    #check difference
    if (len(set(s1).difference(set(s2))) > 1) | len(set(s2).difference(set(s1))) > 1:
        return False
         
    return True 

def compress_str(s: str) -> str:
    
    comp_litera = ''
    num_litera = 0
    out = ''
    
    for litera in str1:
        if comp_litera == litera:
            num_litera += 1
        elif comp_litera:
            out += comp_litera + str(num_litera)
            num_litera = 1
            comp_litera = litera
        else:    
            num_litera = 1
            comp_litera = litera

    if comp_litera:
        out += comp_litera + str(num_litera)  
        
    return out 