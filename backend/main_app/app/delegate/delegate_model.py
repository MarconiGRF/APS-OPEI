import datetime

from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


class Base(DeclarativeBase):
    pass


class Delegate(Base):
    __tablename__ = 'delegate'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    cpf: Mapped[str]
    birthdate: Mapped[datetime.date]

    def __repr__(self):
        return self.name
1