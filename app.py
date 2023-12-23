from fastapi import FastAPI
import uvicorn
import sys
import os

from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from src.textsummarizer.pipeline.prediction  import PredictionPipeline


text:str = 'What is Text Summarization?'

app = FastAPI()


@app.get('/',tags=['authentication'])
async def index():
    return RedirectResponse(url='/docs')


@app.get('/train')
async def training():
    try:
        os.system('python main.py')
        return Response('Training Successful!')
    
    except Exception as e:
        return Response('Error Occurred! {}'.format(e))



@app.post('/prediction')
async def prediction_route(text):

    try:
        obj = PredictionPipeline()
        res = obj.predict(text)
        return res

    except Exception as e:
        raise e



if __name__ == "__main__":
    uvicorn.run(app, host = '0.0.0.0',port =5500)