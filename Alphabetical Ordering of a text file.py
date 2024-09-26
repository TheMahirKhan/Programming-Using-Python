#This program takes a text file containing names in unordered manner and writes them in another file in ordered manner



a=open(r"C:\Users\MAHIR\Desktop\Files\unordered.txt","r")
L1=[]
for name in a:
    b=name
    
    L1.append(b)
L1.sort()

print(L1)


a1=open(r"C:\Users\MAHIR\Desktop\Files\ordered.txt","a+")
r=100
for i in range(1,len(L1)):
    r=r+1
    
    
    a1.write(str(r))
    a1.write("                          ")
    a1.write(L1[i])
    a1.write("\n")
    
a.close()
a1.close()
