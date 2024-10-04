from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from . import db


class Audiobook(db.Model):
    __tablename__: str = "audiobook"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    author: Mapped[str] = mapped_column(String(100), nullable=False)
    cover_image: Mapped[str] = mapped_column(String(200), nullable=False)
    votes: Mapped[int] = mapped_column(Integer, default=0)

    def __repr__(self) -> str:
        return f"<Audiobook {self.title}>"

    def to_dict(self) -> dict[str, int | str]:
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "coverImage": self.cover_image,
            "votes": self.votes,
        }
