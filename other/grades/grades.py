class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        if grade > 0:
            self.grades.append(grade)
            return(f"Grade Added: {grade}")

    def average_grade(self):
        if len(self.grades) < 1:
            return 0
        return ((sum(self.grades)) / len(self.grades))

    def calculate_gpa(self):
        if not self.grades:
            return 0
        def grade_to_gpa(grade):
            if 93 <= grade <= 100:
                return 4.0
            elif 90 <= grade <= 92:
                return 3.7
            elif 87 <= grade <= 89:
                return 3.3
            elif 83 <= grade <= 86:
                return 3.0
            elif 80 <= grade <= 82:
                return 2.7
            elif 77 <= grade <= 79:
                return 2.3
            elif 73 <= grade <= 76:
                return 2.0
            elif 70 <= grade <= 72:
                return 1.7
            elif 67 <= grade <= 69:
                return 1.3
            elif 63 <= grade <= 66:
                return 1.0
            elif 60 <= grade <= 62:
                return 0.7
            else:
                return 0.0
        gpa_values = [grade_to_gpa(grade) for grade in self.grades]
        return sum(gpa_values) / len(gpa_values)

    def print_report(self):
        average = self.average_grade()  # Get the average grade
        gpa = self.calculate_gpa()  # Calculate the GPA
        print(f"Student: {self.name} (ID: {self.student_id})")
        print(f"Grades: {self.grades}")
        print(f"Average Grade: {average:.2f}")
        print(f"GPA: {gpa:.2f}")


daniel = Student('daniel', 101)

print(daniel.print_report())

daniel.add_grade(90)
daniel.add_grade(95)
daniel.add_grade(92)

print(daniel.average_grade())
