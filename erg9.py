x = []
p = 0 
infile = open("two_cities_ascii".txt, 'r')
for line in infile:
    p = p + 1
    num = ord(line)
    x.append(num)
infile.close()

for i in  range(p-1):
    a = bin(x[i])
    

        

