def f(Origin):
	Reverse=''
	Result=''
	for i in range (0,len(Origin)):
		if Origin[i]=='T'or Origin[i]=='t':
			Reverse+='A'
		elif Origin[i]=='A'or Origin[i]=='a':
			Reverse+='T'
		elif Origin[i]=='C'or Origin[i]=='c':
			Reverse+='G'
		elif Origin[i]=='G'or Origin[i]=='g':
			Reverse+='C'
	for i in range (0,len(Reverse)):
		Result+=Reverse[len(Reverse)-1-i]
	return Result

print("The example sequence is 'ATCGTAGC'")
print("The result is ",f('ATCGTAGC'))
Origin=input()
f(Origin)



