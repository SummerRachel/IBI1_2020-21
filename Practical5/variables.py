a=140102
b=190784
c=100321
d=abs(a-c)
e=abs(a-b)
print"a=",a,"b=",b,"c=",c,"d=",d,"e=",e
if d-e<0:
 print("d<e")
elif d-e>0:
 print("d>e")
else:
 print("d=e")

X=True
Y=False
Z=(X and not Y)or(Y and not X)
if(Z==True):
 print"Z is true"
else:
 print"Z is false"
W=X!=Y
if(W==Z):
 print"W and Z are always the same"
else:
 print"W and Z are not always the same"
