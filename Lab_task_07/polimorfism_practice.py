class Department:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print("Department Name:", self.name)


class Author:
    def __init__(self, book_name):
        self.book_name = book_name

    def write_article(self):
        print("Writing an article...")

    def publish_blog(self):
        print("Publishing a blog...")

    def profile(self):
        print("Author Profile...")


class Teacher(Department):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def schedule_class(self):
        print("For teacher the class is already scheduled")

    def grade_student(self):
        print("Teacher is grading student")

    def display_name(self):
        super().display_name()

    def profile(self):
        print("Teacher Profile...")


class TeacherAuthor(Teacher, Author):
    def __init__(self, name, subject, book_name):
        Teacher.__init__(self, name, subject)
        Author.__init__(self, book_name)

    def info(self):
        self.display_name()
        self.schedule_class()
        self.grade_student()
        self.profile()

        self.write_article()
        self.publish_blog()


TA_1 = TeacherAuthor("CSE", "OOP", "Easy Programming with Java")
TA_2 = TeacherAuthor("CSE", "OOP 2", "Programming with Python")
TA_1.info()
print("\n")
TA_2.info()