from typing import Type

from sqlalchemy import Column, String

from app.base import Base


class User(Base):
    """
    Model for user; used for auth and all.
    """
    email = Column(String(255), unique=True, index=True, nullable=False)

    @classmethod
    def to_dict(cls, instance: Type[Base]):
        """
        Additional functionality to convert a User instance into a dictionary
        so it can be used as keyword arguments
        """
        result = {}

        for column in instance.__table__.columns:
            result[column.name] = str(getattr(instance, column.name))

        return result