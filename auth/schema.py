from app.schema import BaseSchema


class LoginSchema(BaseSchema):
    """
    Login the user
    """
    email: str
    password: str
