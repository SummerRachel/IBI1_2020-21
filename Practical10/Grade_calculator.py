class Grade(object):
	def __init__(self,name,code,poster,exam,final):
		self.name=name
		self.code=code
		self.poster=poster
		self.exam=exam
		self.final=final
	def calculator(self):
		self.final=self.code*0.4+self.poster*0.3+self.exam*0.3
		return self.final
#use an example to check the code
print('Name:zy Code_score:100 Poster_score:90 Exam_score:100')

example=Grade('zy',100,90,100,0)


print('Example Name:',example.name,' ','Example final score:',example.calculator())
