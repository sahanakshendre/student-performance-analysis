class Student:

    def __init__(self, student_id, name, branch, marks):
        self.student_id = student_id
        self.name = name
        self.branch = branch
        self.marks = marks

    def calculate_total(self):
        return sum(self.marks)

    def calculate_average(self):
        return sum(self.marks) / len(self.marks)

    def calculate_grade(self):
        avg = self.calculate_average()

        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"