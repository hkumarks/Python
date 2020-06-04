import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def mean(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]    
    elif w.upper() in data:
        return data[w.upper()]     
    elif len(get_close_matches(w,data.keys()))>0:
        inp=input("Did you mean %s. Type Y for yes and N for no " %get_close_matches(w,data.keys())[0])
        inp=inp.upper()
        if inp=='Y':
            return data[get_close_matches(w,data.keys())[0]]
        elif inp=='N':
            return "The word doesn't exist. Please double check it."    
        else:
            return "We didn't undrstand your entry" 
    else:
        return "The word doesn't exist. Please double check it."          

word=input("Enter a word: ")
output=mean(word)
if type(output)==list:
    for i in output:
        print(i)
else:
    print(output)
    
