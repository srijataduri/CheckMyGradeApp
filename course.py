class Course:
    def __init__(self, course_id, course_name, description):
        self.course_id = course_id
        self.course_name = course_name
        self.description = description

    def to_dict(self):
        return {
            "Course_id": self.course_id,
            "Course_name": self.course_name,
            "Description": self.description,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            course_id=data["Course_id"],
            course_name=data["Course_name"],
            description =data["Description"]
        )

    def __str__(self):
        return f"{self.course_id} {self.course_name} {self.description}"
