from fastapi import FastAPI, Path, Query
from typing import Optional

app = FastAPI()

inventory = {
    1: 
    {
     "name"  :"milk",
     "price" : 3.5,
     "brand" :"Sudha"
    }
}
@app.get("/get-item/{item_id}")
def get_item(item_id:int = Path(None, description="The id of the path you want to view",lt=2)):
    return inventory[item_id]

@app.get("/get-by-name/{item_id}")
def get_item(*,item_id:int,name:Optional[str] = None, test:int):
    for item_id in inventory:
        if [item_id]["name"]== None:
            return inventory [item_id]
            return{"data":"not found"}

