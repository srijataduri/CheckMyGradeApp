from course import Course
from csvutils import save_to_csv

class CourseUtils:
    def __init__(self, courses=None):
        self.courses = courses if courses is not None else []
        self.file_path = "data/courses.csv"
    def add_new_course(self, course: Course):
        self.courses.append(course)
    def display_records(self):
        for s in self.courses:
            print(s)
    def find_by_id(self, course_id):
        for c in self.courses:
            if c.course_id == course_id:
                return c
        return None
    def delete_course(self, course_id):
        self.courses = [c for c in self.courses if c.course_id != course_id]
        print('Deleted the course with ID - '+ course_id)
    def update(self, course_id, new_name=None, new_professor_id=None, new_credits=None):
        course = self.find_by_id(course_id)
        if not course:
            return False
        if new_name is not None:
            course.course_name = new_name
        if new_professor_id is not None:
            course.professor_id = new_professor_id
        if new_credits is not None:
            course.credits = new_credits
        return True
    def get_courses_by_professor(self, professor_id):
        return [c for c in self.courses if c.professor_id == professor_id]
    def sorted_by_name(self):
        return sorted(self.courses, key=lambda c: c.course_name.lower())
    def save(self):
        save_to_csv(
            self.file_path,
            self.courses,
            fieldnames=[
                "Course_name",
                "Description",
                "Course_id"
            ]
        )
