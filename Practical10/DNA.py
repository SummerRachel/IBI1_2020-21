Origin=input()
def f(Origin):
	Reverse=''
	for i in range (0,len(Origin)):
		if Origin[i]=='T'or Origin[i]=='t':
			Reverse+='A'
		elif Origin[i]=='A'or Origin[i]=='a':
			Reverse+='T'
		elif Origin[i]=='C'or Origin[i]=='c':
			Reverse+='G'
		elif Origin[i]=='G'or Origin[i]=='g':
			Reverse+='C'
	return Reverse

print(Reverse)



