listasw=[]
listart=[]
listadevice=[]
lista=["R2","R2","R3",
       "S1","S2","S3",
       "R4","R5","PC"]
for i in lista:
    if 'S' in i:
        listasw.append(i)
    elif "R" in i:
        listart.append(i)
    else:
        listadevice.append(i)
print("Switches: ",listasw,"\nRouters: ",listart,"\nDevice: ",listadevice)
  
