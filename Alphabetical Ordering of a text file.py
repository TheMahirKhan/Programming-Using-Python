#This program takes a text file containing names in unordered manner and writes them in another file in ordered manner



a=open(r"C:\Users\MAHIR\Desktop\Files\unordered.txt","r")          #Opening the file in read mode
L1=[]                                                              #Empty list
for name in a:
    b=name
    
    L1.append(b)                                                    #Append one element to L1 one at a time
L1.sort()                                                           #Sort L1 Alphabetically

print(L1)


a1=open(r"C:\Users\MAHIR\Desktop\Files\ordered.txt","a+")          #Open another file for ordered names only
r=100
for i in range(1,len(L1)):
    r=r+1
    
    
    a1.write(str(r))                                              #Write one element of L1 in file one at a time
    a1.write("                          ")
    a1.write(L1[i])
    a1.write("\n")
    
a.close()
a1.close()
