from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from joblib import load
import pathlib
from fastapi.middleware.cors import CORSMiddleware

origins = ["*"]

app = FastAPI(title = 'Heart Disease Prediction')

app.add_middleware(
   CORSMiddleware,
   allow_origins=origins,
   allow_credentials=True,
   allow_methods=["*"],
   allow_headers=["*"]
)

model = load(pathlib.Path('model/movie_success_rate_v1.joblib'))

class InputData(BaseModel):
    
    Rating:int=7
    Votes:int=757074
    Metascore:int=70
    Action:int=1
    Adventure:int=0
    Aniimation:int=1
    Biography:int=0
    Comedy:int=1
    Crime:int=1
    Drama:int=1
    Family:int=1
    Fantasy:int=0
    History:int=0
    Horror:int=1
    Music:int=0
    Musical:int=0
    Mystery:int=1
    Romance:int=1
    Sport:int=0
    Thriller:int=1
    War:int=0
    Western:int=0
    Success:int=1

class OutputData(BaseModel):
    score:float=0.80318881046519

@app.post('/score', response_model = OutputData)
def score(data:InputData):
    model_input = np.array([v for k,v in data.dict().items()]).reshape(1,-1)
    result = model.predict_proba(model_input)[:,-1]

    return {'score':result}
