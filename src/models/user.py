class User():
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    
    def get_name(self):
        
        return self.name
    
    
    
    def get_password(self):
        
        return self.password
    
    def get_email(self):
        
        return self.email
    
    def verify_password(self, password):
        
        return self.password == password
    
    def __str__(self) -> str:
        return("User(name:{name}, email:{email}, password:{password})")
    