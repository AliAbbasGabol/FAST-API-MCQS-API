import bcrypt


class Hash():
    @staticmethod
    def encryptor(password):
        encoded = password.encode("utf-8")
        hashed_password = bcrypt.hashpw(encoded, bcrypt.gensalt())
        return hashed_password
    

    @staticmethod
    def verify(password, hashed):
        return bcrypt.checkpw(password.encode("utf-8"), hashed)
    
