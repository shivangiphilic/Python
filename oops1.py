class student:
    def marksList(self):
        self.id=int(input("Enter Roll No: "))
        self.name=input("Enter Name: ")
        self.mid1=int(input("Enter Mid 1 marks: "))
        self.mid2=int(input("Enter Mid 2 marks: "))
        self.quiz=int(input("Enter quiz marks: "))
        self.total=self.mid1+self.mid2+self.quiz
        print("name:",self.name)
        print("roll number",self.id)
        print("total",self.total)
        result=self.total
        if result>80:
            print("grade A")
        elif result<80 and result>=60:
            print("grade B")
        elif result<60 and result>=50:
            print("grade C")
        else:
            print("Fail")
stu=student()
stu.marksList()