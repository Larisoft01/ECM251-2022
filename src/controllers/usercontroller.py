from models.user import User

class UserController():
    def __init__(self) -> None:
        #Carrega os dados dos usuários
        
        self.users =[
            User(name = "Dawn", password = "piplups", email = "Dawn_poketrainer@sinnoh.com"),
            User(name = "Hilda", password = "N is my lover", email = "Hilda_poketrainer@unova.com"),
            User(name = "May", password = "torchic12", email ="May_poketrainer@hoenn.com")]
    def checkUser(user):
        return user in self.users
    
    def checkLogin(self, name, password):
        user_test= User(name=name, password=password, email=None)
        for user in self.users:
            if user.name == user_test.name and user.password == user_test.password:
                return True
        return False