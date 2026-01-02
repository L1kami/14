class GroupLimitError(Exception):
    def __init__(self, message="Max 10 students allowed"):
        self.message = message
        super().__init__(self.message)

class Person:
    def __init__(self, gender: str, age: int, first_name: str, last_name: str):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Student(Person):
    def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __eq__(self, other):
        if isinstance(other, Student):
            return str(self) == str(other)
        return False

    def __hash__(self):
        return hash(str(self))

class Group:
    def __init__(self, title: str):
        self.title = title
        self.students = []

    def add_student(self, student: Student):
        if len(self.students) >= 10:
            raise GroupLimitError()
        if isinstance(student, Student):
            self.students.append(student)

    def delete_student(self, last_name: str):
        student = self.find_student(last_name)
        if student:
            self.students.remove(student)

    def find_student(self, last_name: str):
        for student in self.students:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = "\n".join(str(student) for student in self.students)
        return f"Group: {self.title}\n{all_students}"

if __name__ == "__main__":
    st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
    st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

    gr = Group('PD1')

    gr.add_student(st1)
    gr.add_student(st2)

    print(gr)

    assert gr.find_student('Jobs') == st1
    assert gr.find_student('Jobs2') is None

    gr.delete_student('Taylor')

    print(gr)