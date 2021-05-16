class Student(object):
	def __init__(self,firstname,givenname,programme):
		self.firstname=firstname
		self.givenname=givenname
		self.programme=programme
#create a new function in class to make the list
	def student_list(self):
		return 'Name:'+self.firstname+' '+self.givenname+' '+'UndergraduateProgramme:'+self.programme

#give a example
example=Student('Ziyu','Xia','BMS')
print(example.student_list())

#input student information and get the result
input_firstname=input('Firstname:')
input_givenname=input('Givenname:')
input_programme=input('Undergraduate Programme:')
result=Student(input_firstname,input_givenname,input_programme)
print(result.student_list())
