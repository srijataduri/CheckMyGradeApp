class Grades:
    def __init__(self, grade_id, grade, marks_range):
        self.grade_id = grade_id
        self.grade = grade
        self.marks_range = marks_range

    def to_dict(self):
        return {
            "Grade_id" : self.grade_id,
            "Grade" : self.grade,
            "Marks_range" : self.marks_range
        }
    @classmethod
    def from_dict(cls, data):
        return cls(
            grade_id = data["Grade_id"],
            grade = data["Grade"],
            marks_range = data["Marks_range"]
        )
