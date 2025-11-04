class Professor:
    def __init__(self, professor_id, professor_name, rank, course_id):
        self.professor_id = professor_id
        self.professor_name = professor_name
        self.rank = rank
        self.course_id = course_id

    def to_dict(self):
        return {
            "Professor_id": self.professor_id,
            "Professor Name": self.professor_name,
            "Rank": self.rank,
            "Course.id": self.course_id
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            professor_id=data["Professor_id"],
            professor_name=data["Professor Name"],
            rank=data["Rank"],
            course_id=data["Course.id"]
        )

    def __str__(self):
        return f"{self.professor_id} {self.professor_name} {self.rank} {self.course_id}"
