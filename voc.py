#!/usr/bin/env  python3


import sys, getopt, random

path=sys.argv[1]
lang_in=int(sys.argv[2])
if lang_in == 1:
    lang_out=2
if lang_in == 2:
    lang_out=1

file = open(path,'r').readlines()

file_x=open(path+"_x",'w')
file_ok=open(path+"_ok",'w')
file_rest=open(path+"_rest",'w')


dict=[]
for line in file:
    row = line.split(";")
    dict.append(row)

#print("Erzeuge zufällige Reihenfolge.")
# Nicht sauber: Das kann dauern.
rand_list=[]
while len(rand_list)<len(dict):
    i=random.randint(1,len(dict))
    if i in rand_list:
        pass
    else:
        rand_list.append(i)
#print(rand_list)
print()

count=0
for i in rand_list:
    count=count+1
    answer = input("["+str(count)+"/"+str(len(dict))+"] "+dict[i-1][lang_in-1]+": ")
    if answer == dict[i-1][lang_out-1]:
        file_ok.write(file[i-1])
    else:
        print("Antwort: "+dict[i-1][lang_out-1])
        #if dict[i-1][2] !="":
        #print("Kommentar: " + dict[i-1][2])
        entscheidung= input("[Enter=ok, x=Wiederholen, .= Ende]")
        if entscheidung == ".":
            k=i
            while k<=len(rand_list)-1:
                file_rest.write(file[k-1])
                k=k+1
            break
        if entscheidung == "":
            file_ok.write(file[i-1])
        if entscheidung == "x":
            file_x.write(file[i-1])
    print()
file_x.close()
file_ok.close()
file_rest.close()
print("Fails in " +path+"_x")
print("Gewusst in " +path+"_ok")
print("Rest in " +path+"_rest") 
    


