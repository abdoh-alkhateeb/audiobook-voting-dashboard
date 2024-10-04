import os
from typing import Final


class Config:
    SQLALCHEMY_DATABASE_URI: Final[str] = "sqlite:///" + os.path.join(os.path.dirname(__file__), "instance", "audiobooks.db")
    SQLALCHEMY_TRACK_MODIFICATIONS: Final[bool] = False
