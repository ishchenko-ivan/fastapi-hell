from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.dialects.postgresql import MONEY

Base = declarative_base()

class dbItem(Base):
    __tablename__ = "Items"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    price = Column(MONEY)
    quantity = Column(Integer)
    upd_date = Column(Date)

    #new column for migration testing
    is_onsale = Column(Boolean)

    def __repr__(self):
        return "<Item(title='{}', price='{}', quantity={}, upd_date={})>"\
                .format(self.title, self.price, self.quantity, self.upd_date)