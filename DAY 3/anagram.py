#string method

def anagram(s,t):
    if (len(s)==len(t)):
        s=sorted(s)
        t=sorted(t)
        if (s==t):
            return True
        return False
print(anagram("racecar","cecarra"))

print(anagram("racecar", "cecarra"))   
print(anagram("anagram", "nagaram"))  
print(anagram("rat", "car"))           
print(anagram("listen", "silent"))     


#dictionary method
def Ananagram(s,t):
    count_s={}
    count_t={}
    for char in s:
        count_s[char]=count_s.get(char,0)+1
    for char in t:
        count_t[char]=count_t.get(char,0)+1
    return count_s==count_t

print(anagram("racecar","cecarra"))
print(Ananagram("racecar", "cecarra"))  
print(Ananagram("rat", "car"))          
print(Ananagram("listen", "silent"))    


