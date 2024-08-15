from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class Base(DeclarativeBase):
    pass

class Item(Base):
    __tablename__ = "items"
    id: Mapped[str] = mapped_column(primary_key=True)
    foo: Mapped[str] = mapped_column(String(255))
    bar: Mapped[str] = mapped_column(String(100))
    def __repr__(self) -> str:
        return f"Item(id={self.id!r})"
    
    def to_json(self):
        return {
            "id": self.id,
            "foo": self.foo,
            "bar": self.bar
        }

# if __init__.py