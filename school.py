class School:
    def __init__(self,name,address):
        self.name = name
        self.address = address
        self.teachers = {} # {"Bangla" : teacher_object}
        self.classrooms = {} # {"eight" : classroom_object}

    def add_classroom(self,classroom):
        self.classrooms[classroom.name] = classroom
    
    def add_teacher(self,subject,teacher):
        self.teachers[subject] = teacher
    
    def student_admission(self,student):
        classname = student.classroom.name
        self.classrooms[classname].add_student(student)

    @staticmethod
    def calculate_grade(marks):
        if marks >= 80 and marks <= 100:
            return 'A+'
        elif marks >= 70 and marks < 80:
            return 'A'
        elif marks >= 60 and marks < 70:
            return 'A-'
        elif marks >= 50 and marks < 60:
            return 'B'
        elif marks >= 40 and marks < 50:
            return 'C'
        elif marks >= 33 and marks < 40:
            return 'D'
        else:
            return 'F'

    @staticmethod
    def grade_to_value(grade):
        grade_map = {
            'A+' : 5.00,
            'A' : 4.50,
            'A-' : 4.00,
            'B' : 3.00,
            'C' : 2.50,
            'D' : 1.50,
            'F' : 0.00
        }
        return grade_map[grade]
    
    @staticmethod
    def value_to_grade(value):
        if value >= 4.50 and value <= 5.00:
            return 'A+'
        elif value >= 4.00 and value < 4.50:
            return 'A-'
        elif value >= 3.00 and value < 4.00:
            return 'B'
        elif value >= 2.50 and value < 3.00:
            return 'C'
        elif value >= 1.50 and value < 2.50:
            return 'D'
        else:
            return 'F'
        
    
    def __repr__(self):
        # all classroom
        for key in self.classrooms.keys():
            print(key)
        # all students
        print("All Students")
        result = ''
        for key,value in self.classrooms.items():
            result += f"---{key.upper()} ClassRoom Students\n"
            for student in value.students:
                result += f"{student.name}\n"
        print(result)
        # all subjects
        subject = ''
        for key,value in self.classrooms.items():
            subject += f"---{key.upper()} ClassRoom Subjects\n"
            for sub in value.subjects:
                subject += f"{sub.name}\n"
        print(subject)
        # all teachers
        # all students result
        print("Students Results")
        for key,value in self.classrooms.items():
            for student in value.students:
                for k,v in student.marks.items():
                    print(student.name,k,v,student.subject_grade[k])
                print(student.calculate_final_grade())