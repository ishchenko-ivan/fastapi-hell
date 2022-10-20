#Population of the added column with values
import os
print(os.environ)
from db.crud import Session
from db.models import dbItem

s = Session()

items = s.query(dbItem).all()

for item in items:
    item.is_onsale = False
    s.add(item)
    print(f"Item #{item.id} - {item.title} updated...\n")

s.commit()
s.close()