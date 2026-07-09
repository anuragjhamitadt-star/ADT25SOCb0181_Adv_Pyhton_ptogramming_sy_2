#required_and_keyword_argument
def student(rollno, name):
    print(name, rollno)
    
student(13, "Anurag")

#default_argument
def student(rollno, name, division="SY2"):
    print(name, rollno, division)
    
student(14, "Arham")

#Variable_argument
def subjects(*sub):
    print("subjects: ", *sub)
    
subjects("Mathematics", "Python")
subjects("Mathematics", "python", "java", "C", "C++")
subjects("EP", "DELD", "PAI", "DBMS")
