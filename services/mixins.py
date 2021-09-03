import bcrypt


class PasswordHashMixin:

    def get_hashed_password(self, plain_password):
        hash = bcrypt.hashpw(plain_password.encode('utf-8'), bcrypt.gensalt())
        return hash.decode()

    def check_password(self, plain_password, hashed_password):
        return bcrypt.checkpw(
            plain_password.encode('utf-8'),
            hashed_password.encode('utf-8')
        )
