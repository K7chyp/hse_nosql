from pymongo import MongoClient
from faker import Faker
import random
from datetime import datetime, timedelta


fake = Faker("ru_RU")
client = MongoClient(
    host="localhost",
    port=27017,
    username="root",
    password="example",
)
db = client["university_db"]


db.students.delete_many({})
db.teachers.delete_many({})
db.courses.delete_many({})
db.grades.delete_many({})
db.departments.delete_many({})
db.groups.delete_many({})


departments = []
for _ in range(3):
    dept = db.departments.insert_one({"name": fake.unique.company()})
    departments.append(dept.inserted_id)


groups = []
for dept_id in departments:
    for _ in range(5):
        group = db.groups.insert_one(
            {
                "name": f"{fake.random_letter().upper()}-{fake.random_number(digits=2)}",
                "department_id": dept_id,
            }
        )
        groups.append(group.inserted_id)


students = []
for group_id in groups:
    for _ in range(10):
        student = db.students.insert_one(
            {
                "name": fake.name(),
                "email": fake.email(),
                "group_id": group_id,
                "department_id": db.groups.find_one({"_id": group_id})["department_id"],
            }
        )
        students.append(student.inserted_id)


teachers = []
for dept_id in departments:
    for _ in range(5):
        teacher = db.teachers.insert_one(
            {"name": fake.name(), "department_id": dept_id}
        )
        teachers.append(teacher.inserted_id)


courses = []
for teacher_id in teachers:
    for _ in range(3):
        course = db.courses.insert_one(
            {
                "name": fake.catch_phrase(),
                "teacher_id": teacher_id,
                "department_id": db.teachers.find_one({"_id": teacher_id})[
                    "department_id"
                ],
                "semester": random.choice([1, 2]),
                "year": 2023,
            }
        )
        courses.append(course.inserted_id)


for student_id in students:
    for course_id in random.sample(courses, 5):
        y, m, d = map(
            int,
            str(
                fake.date_between_dates(
                    date_start=datetime(2023, 9, 1), date_end=datetime(2024, 6, 30)
                )
            ).split("-"),
        )
        db.grades.insert_one(
            {
                "student_id": student_id,
                "course_id": course_id,
                "grade": random.randint(2, 5),
                "date": datetime(y, m, d),
            }
        )

print("Генерация данных завершена!")
