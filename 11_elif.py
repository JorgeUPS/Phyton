acl=int(input("Ingrese el # de ACL: "))
if acl>=1 and acl<=99:
    print("es una ACL estandar")
elif acl>=10 and acl<=199:
    print("es una ACL extendida")
else:
    print("No es un # de ACL válido")
