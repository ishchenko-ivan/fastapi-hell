import sys, os
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.dirname(__file__) + "/db")
print(sys.path)

from fastapi import FastAPI, Path
from schemas import Item, UpdateItem
from db.models import dbItem
from db.crud import Session, recreate_database
import uvicorn

app = FastAPI()

@app.get("/recreate-db")
def index():
    recreate_database()
    return "The database was succesfully recreated..."

@app.get("/")
def index():
    s = Session()
    result = s.query(dbItem).order_by(dbItem.id.asc()).all()
    s.close()
    return result

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(..., ge=0, description="The ID of the item you are looking for!")):
    s = Session()
    result = s.query(dbItem).filter(dbItem.id == item_id).first()
    s.close()
    if result != None:
        return result
    else:
        return {"Bruh...": "We don`t have such item!"}
        

@app.post("/create-item")
def create_item(item: Item):
    new_item = dbItem(
        title = item.title,
        price = item.price,
        quantity=item.quantity,
        upd_date=item.upd_date
    )

    s = Session()
    s.add(new_item)
    s.commit()
    s.close()

    return {"Successfully added item: \n":item}

@app.put("/update-item/{item_id}")
def update_item(*, item_id: int = Path(..., ge=0, description="The ID of the item you want to create!"), item: UpdateItem):
    s = Session()
    result = s.query(dbItem).filter(dbItem.id == item_id).first()
    
    if result != None:
        if item.title != None:
            result.title = item.title
        if item.price != None:
            result.price = item.price
        if item.quantity != None:
            result.quantity = item.quantity
        if item.upd_date != None:
            result.upd_date = item.upd_date

        s.add(result)
        s.commit()
        id = result.id
        s.close()
        return f"Successfully updated item #{id}"
    else:
        s.close()
        return {"Bruh...": "We don`t have such item!"}

        

@app.delete("/delete-item/{item_id}")
def delete_item(item_id: int = Path(..., ge=0, description="The ID of the item you want to delete!")):
    s = Session()
    result = s.query(dbItem).filter(dbItem.id == item_id).first()
        
    if result != None:
        id = result.id
        s.delete(result)
        s.commit()
        s.close()
        return {f"Success": "You are a horrible person - item id {id}"}
    else:
        s.close()
        return {"Bruh...": "We don`t have such item!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)