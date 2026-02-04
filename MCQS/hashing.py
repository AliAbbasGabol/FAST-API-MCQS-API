import bcrypt


class Hash():
    def encryptor(password):
        encoded = password.encode("utf-8")
        hashed_password = bcrypt.hashpw(encoded, bcrypt.gensalt())
        return hashed_password