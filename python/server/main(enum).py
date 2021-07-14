#POST: 데이터를 생성하기 위해.
#GET: 데이터를 읽기 위해.
#PUT: 데이터를 업데이트하기 위해.
#DELETE: 데이터를 삭제하기 위해.

from fastapi import FastAPI

from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value =="lenet":
        return {"model_name": model_name, "message": " LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


