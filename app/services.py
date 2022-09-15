from typing import Type

from sqlalchemy.orm import Session

from .base import Base


class BaseService:
    """
    Base class for services. Handles DB initialization and saving a model
    """
    def __init__(self, db: Session) -> None:
        self.db = db

    def save(self, model: Type[Base]) -> None:
        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)