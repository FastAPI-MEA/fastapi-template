from datetime import datetime, timedelta
from typing import Any, Dict

from fastapi.security import OAuth2PasswordBearer
from jose import jwt

from app.services import BaseService
from app.settings import settings

# for authentication that works seamlessly with OpenAPI
reuseable_oauth = OAuth2PasswordBearer(
    tokenUrl="/api/v1/user/login",
    scheme_name="JWT"
)


def hash_password(password: str) -> str:
    """Creates a hash of the password"""
    hashed_password = settings.PASSWORD_HASHER.hash(password)
    return hashed_password


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Checks if a password corresponds to a hash"""
    password_is_verified = settings.PASSWORD_HASHER.verify(
        plain_password, hashed_password
    )

    return bool(password_is_verified)


def create_auth_token(payload: Dict[str, Any], expiry: int) -> str:
    """
    This handles the encoding of user information into a token
    that can be used. It is generic so as to accomodate access and
    refresh token.
    """
    expiry_delta = datetime.now() + timedelta(seconds=expiry)
    data_to_encode = {"expiry": str(expiry_delta), "data": payload}
    encoded_data: str = jwt.encode(
        data_to_encode, settings.SECRET_KEY, settings.JWT_ALGORITHM
    )

    return encoded_data


class UserService(BaseService):
    """
    This class helps perform bulk of activities required by the corresponding API
    """
    def a_method(self):
        """
        Here, the use of `self.save` is demonstrated.
        Ensure to take out this method.
        """
        model_instance = ...
        self.save(model_instance)