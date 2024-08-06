from app import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), unique=True, nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.password}')"
class Car(db.Model):
    __tablename__ = 'car'
    car_id = db.Column(db.Integer, primary_key=True)
    model= db.Column(db.String(200), nullable=False)
    owner = db.Column(db.String(200), nullable=False)
    year = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Car('{self.model}', '{self.owner}', '{self.year}')"
    
# Define the Student model, will be used for the student table, with the following columns, and one to many relationship with the course table

class Student(db.Model):
    __tablename__ = 'student'
    student_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    grade = db.Column(db.String(200), nullable=False)
    course= db.relationship('Course', backref="student") # Define the one to many relationship with the course table, backref is used to access the student from the course table, student is the name of the relationship/ class variable, basically student is a new column in child course

    def __repr__(self):
        return f"Student('{self.name}', '{self.age}', '{self.grade}')"
    
# Define the Course model, will be used for the course table, with the following columns, and many to one relationship with the student table
class Course(db.Model):
    __tablename__ = 'course'
    course_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.student_id')) # Define the many to one relationship with the student table, student_id is the foreign key, name of the class and student id column in the student table

    def __repr__(self):
        return f"Course('{self.name}')"
    
#****************** For one to many relationship practice*********************
#from app import db
# >>> db.create_all()
# >>> 
# >>> adarsh=Student(name="Adarsh", age="20", grade="A+")
# >>> anoop=Student(name="Anoop", age="21", grade="A+")
# >>> rohit=Student(name="David", age="05", grade="B")
# >>> db.session.add_all([adarsh,anoop,rohit])
# >>> db.session.commit()
# >>> course1=Course(name="BBA", student=adarsh)
# >>> db.session.add(course1)
# >>> db.session.commit()
# >>> course1=Course(name="BSC", student=david)
# Traceback (most recent call last):
#   File "/usr/lib/python3.10/code.py", line 90, in runcode
#     exec(code, self.locals)
#   File "<console>", line 1, in <module>
# NameError: name 'david' is not defined
# >>> course1=Course(name="BSC", student=rohit)
# >>> db.session.add(course1)
# >>> db.session.commit()
# >>> course1.name
# 'BSC'
# >>> course1.student
# Student('David', '5', 'B')
# >>> course1.student.name
# 'David'
# >>> adarsh.course
# [Course('BBA')]
# >>> 