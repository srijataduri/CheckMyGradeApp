class Account:
    def __init__(self, user_id, password):
        self.user_id = user_id
        self.password = password
    def to_dict(self):
        return {
            "user_id": self.user_id,
            "password": self.password
        }
    @classmethod
    def from_dict(cls, data):
        return cls(
            user_id = data["User_id"],
            password = data["Password"]
        )

    def __str__(self):
        return f"{self.user_id} - {self.password}"

