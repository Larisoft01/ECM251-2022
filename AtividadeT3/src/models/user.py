class User():
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    def __str__(self) -> str:
        return("User(name:{name}, email:{email}, password:{password})")
    