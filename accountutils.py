class AccountUtils:
    def __init__(self, accounts=None):
        self.accounts = accounts if accounts is not None else []
        self.current_user = None;
    def login(self, user_id=None, password=None):
        for s in self.accounts:
           if s.user_id == user_id:
               if s.password == password:
                   self.current_user =  s
                   print("You are successfully logged in")
                   return
               else:
                print("Incorrect password")
                return
    def logout(self):
        if self.current_user != None:
            print('There is no logged in user to log out')
        else :
            self.current_user = None
            print('You are successfully logged out')


    def display_all(self):
        for s in self.accounts:
            print(s)
