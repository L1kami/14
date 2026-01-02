from typing import List, Optional


class GroupLimitError(Exception):
    def __init__(self, message="Max 10 students allowed"):
        self.message = message
        super().__init__(self.message)


class Person:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def get_info(self) -> str:
        return f"Person: {self.first_name} {self.last_name}"

    def __str__(self):
        return self.get_info()


class Student(Person):
    def __init__(self, first_name: str, last_name: str, student_ticket: str):
        super().__init__(first_name, last_name)
        self.student_ticket = student_ticket

    def get_info(self) -> str:
        return f"Student: {self.first_name} {self.last_name}, Ticket: {self.student_ticket}"


class Group:
    def __init__(self, title: str):
        self.title = title
        self.students: List[Student] = []

    def add_student(self, student: Student) -> None:
        if len(self.students) >= 10:
            raise GroupLimitError()

        if isinstance(student, Student):
            self.students.append(student)
        else:
            raise TypeError("Object must be an instance of Student")

    def search_student(self, last_name: str) -> Optional[Student]:
        for student in self.students:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name: str) -> bool:
        student_to_remove = self.search_student(last_name)

        if student_to_remove:
            self.students.remove(student_to_remove)
            return True
        else:
            return False

    def __str__(self) -> str:
        if not self.students:
            return f"Група {self.title} порожня."

        student_list = "\n".join([f"- {student.get_info()}" for student in self.students])
        return f"Група: {self.title} (Кількість: {len(self.students)})\nСтуденти:\n{student_list}"


if __name__ == "__main__":
    group = Group("Python-Advanced")

    try:
        for i in range(1, 13):
            student = Student(f"Name_{i}", f"Surname_{i}", f"KB-{i}")
            print(f"Adding student {i}...", end=" ")
            group.add_student(student)
            print("Success.")

    except GroupLimitError as e:
        print(f"\nERROR: {e}")
    except Exception as e:
        print(f"Other error: {e}")

    print(group)