class Student:
   def __init__(self, name, student_id):
       self.name = name
       self.student_id = student_id
       self.courses = []
   def enroll(self, course):
       if course not in self.courses:
           self.courses.append(course)
           course.add_student(self)
   def display_info(self):
       print(f"Student: {self.name} (ID: {self.student_id})")
       if self.courses:
           print("Enrolled Courses:")
           for c in self.courses:
               print(f" - {c.course_name} ({c.course_code})")
       else:
           print("No courses enrolled.")
class Course:
   def __init__(self, course_name, course_code, instructor):
       self.course_name = course_name
       self.course_code = course_code
       self.instructor = instructor
       self.students = []
   def add_student(self, student):
       if student not in self.students:
           self.students.append(student)
   def display_info(self):
       print(f"Course: {self.course_name} ({self.course_code})")
       print(f"Instructor: {self.instructor}")
       if self.students:
           print("Enrolled Students:")
           for s in self.students:
               print(f" - {s.name} (ID: {s.student_id})")
       else:
           print("No students enrolled.")
# Usage
student1 = Student("Anbu", "S001")
course1 = Course("Mathematics", "MATH101", "Dr. Smith")
student1.enroll(course1)
student1.display_info()
print()
course1.display_info()
