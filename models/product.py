from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column

class Product(Base):
    __tablename__ = 'products'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(255), nullable=False)
    brand: Mapped[str] = mapped_column(db.String(50))
    category: Mapped[str] = mapped_column(db.String(50), nullable=False)
    price: Mapped[str] = mapped_column(db.String(20), nullable=False)
    
    