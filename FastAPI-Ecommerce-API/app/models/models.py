from sqlalchemy import Column, Integer, String, ForeignKey,Boolean,TIMESTAMP,Float,ARRAY,Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from ..database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    full_name=Column(String,nullable=False)
    is_active = Column(Boolean, server_default="True", nullable=False)
    created_at=Column(TIMESTAMP(timezone=True), server_default=text("NOW()"), nullable=False)
    role = Column(Enum("admin", "user", name="user_roles"), nullable=False, server_default="user")

    # Relationship 
    carts = relationship("Cart", back_populates="user")


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    name=Column(String,unique=True, nullable=False)

    #Relationship
    products = relationship("Product",back_populates="category")


class Product(Base):
    __tablename__ = "products"

    id=Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    title=Column(String, nullable=False)
    price=Column(Float,nullable=False)
    description=Column(String,nullable=False)
    discount_percentage = Column(Float, nullable=False)
    rating=Column(Float, nullable= False)
    stock= Column(Integer, nullable=False)
    images = Column(ARRAY(String), nullable=False)
    is_published = Column(Boolean, server_default="True", nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("NOW()"), nullable=False)
    category_id=Column(ForeignKey("categories.id", ondelete="CASCADE"), nullable=False)

    #Relationship
    category=relationship("Category",back_populates="products")
    cart_items = relationship("CartItem", back_populates="product")




class Cart(Base):
    __tablename__="carts"

    id=Column(Integer,primary_key=True, nullable=False, unique=True, autoincrement=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("NOW()"), nullable=False)
    total_amount=Column(Integer, nullable=False)
    user_id=Column(Float, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    # Relationship
    user = relationship("User", back_populates="carts")
    cart_items=relationship("CartItem", back_populates="carts")


class CartItem(Base):
    __tablename__= "cart_items"

    id=Column(Integer, primary_key=True, nullable= False, unique=True, autoincrement= True)
    cart_id=Column(Integer,ForeignKey("carts.id" , ondelete="CASCADE"),nullable=False)
    product_id=Column(Integer,ForeignKey("products.id", ondelete="CASCADE"),nullable=False)
    quantity=Column(Integer,nullable=False)
    subtotal=Column(Float, nullable=False)

    # Relationship
    carts=relationship("Cart",back_populates="cart_items")
    product=relationship("Product", back_populates="cart_items")





