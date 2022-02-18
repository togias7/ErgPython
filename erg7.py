infile = open("two_cities_ascii".txt, 'r')
for line in infile:
    listDic = [line.rstrip() for line in infile]
    
infile.close()


a = listDic[1] ##h prwth thesh ths listas periexei ena leksiko poy exei ta idia kleidia me ta upoloipa
list(a.keys()) ##ta kleidia einai idia se ola ta leksika 
print(list) 
key = input("Enter a key from the list: ")

p = 0
max = 0

for item in listDic:
    d = listDic[item]
    
    
    if p == 0: ##sthn prwth epanalhpsh pairnoume ws katw fragma thn prwth timh
        min = d[key]
        if d[key] > max:
            max = d[key]
    else:
        if d[key] < min:
            min = d[key]
        if d[key] > max:
            max = d[key]

    p = p + 1            
print (min, max)
   

    

