class grade:
    def __init__(self,name, code_pro_grade, poster_pre_grade, final_exam_grade):
        self.a = name
        self.b = code_pro_grade
        self.c = poster_pre_grade
        self.d = final_exam_grade
    def total_grade(self):
        return (self.a + " " + str(self.b*0.4 + self.c*0.3 + self.d*0.3))
print (grade('Lizhengxun', 100, 100, 99).total_grade())