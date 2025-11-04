from csvutils import save_to_csv
from prof import Professor

class ProfessorUtils:
    def __init__(self, professors=None):
        self.professors = professors if professors is not None else []
        self.file_path = "data/professors.csv"
    def add_new_professor(self, professor: Professor):
        self.professors.append(professor)
    def display_records(self):
        for s in self.professors:
            print(s)
    def find_by_id(self, professor_id):
        for p in self.professors:
            if p.professor_id == professor_id:
                return p
        return None
    def delete_professor(self, professor_id):
        self.professors = [p for p in self.professors if p.professor_id != professor_id]
        print('Deleted professor with id - ' + professor_id)
    def modify_professor_details(self, professor_id, professor_name=None, rank=None, course_id=None):
        prof = self.find_by_id(professor_id)
        if not prof:
            return False
        if professor_name is not None:
            prof.professor_name = professor_name
        if rank is not None:
            prof.rank = rank
        if course_id is not None:
            prof.course_id = course_id
        return True
    def show_course_detalis_by_prof(self):
        for s in self.professors:
            print(f"{s.professor_name} - {s.course_id}")
    def sorted_by_last_name(self):
        return sorted(self.professors, key=lambda p: p.last_name.lower())
    def save(self):
        save_to_csv(
            self.file_path,
            self.students,
            fieldnames=[
                "Professor_id",
                "Professor Name",
                "Rank",
                "Course.id"
            ]
        )
