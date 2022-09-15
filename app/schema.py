from typing import Any

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel


class BaseSchema(BaseModel):
    def to_dict(self) -> Any:
        return jsonable_encoder(self)
