from pydantic import EmailStr


class EmailStrToLower(EmailStr):

    @classmethod
    def validate(cls, value):
        value = super().validate(value)
        return value.lower()
