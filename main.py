from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from datetime import datetime
import logging

from config import ConfigEnv
from utils import pt_func

app = FastAPI()

# Logs Config
logging.basicConfig(filename='logs/qmenta.log',
                    format='%(levelname)s %(asctime)s: %(message)s',
                    datefmt='%d/%m/%Y %H:%M:%S',
                    level=ConfigEnv())


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    try:
        data_time = datetime.now().date()
        logging.info("Loading Home - Date: {}".format(data_time))
        return templates.TemplateResponse("index.html", {
            "request": request,
            "data_time": data_time
        })
    except Exception as e:
        logging.error("Error Load Home: {}".format(e))


@app.get("/reconnect")
async def reconnect():
    try:
        data_time = datetime.now().date()
        logging.info("Reconnect - Date: {}".format(data_time))
        return {"response": str(data_time)}

    except Exception as e:
        logging.error("Error Reconnect : {}".format(e))


@app.get("/patient")
async def patient():
    try:
        logging.info(" Patient Name Uploaded: {}".format(pt_func()))
        return {"response": pt_func()}

    except Exception as e:
        logging.error("Error loading Patient Name: {}".format(e))


app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
