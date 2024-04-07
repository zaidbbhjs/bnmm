from fastapi import Response
import requests
import os
import random
import uvicorn
from fastapi import Request
import json
from user_agent import generate_user_agent
from fastapi.responses import JSONResponse
from fastapi import FastAPI
import secrets
cok = secrets.token_hex(8) * 2
app = FastAPI()
a=int(0)
from fastapi import FastAPI, UploadFile

app = FastAPI()

from requests import post as pp
from user_agent import generate_user_agent as gg
from random import choice as cc
from random import randrange as rr

#yy='azertyuiopmlkjhgfdsqwxcvbn'
@app.get('/api/all/{gmail}')
def all(gmail):
	email=gmail
	r=requests.get("https://random-u-f3cbe096c054.herokuapp.com/api/x").json()
	email=(r["email"])
	r=requests.get(f"https://random-u-f3cbe096c054.herokuapp.com/api2/{email}").json()
	st=(r["status"])
	if "Good" in st:
		r=requests.get(f"https://gmilmm-4e572f0bf5f5.herokuapp.com/api/gmail/{email}").json()
		st2=(r["status"])
		if "Good" in st2:
			return         JSONResponse(content={"status":f"Good","email":f"{email}"})
		else:
			return         JSONResponse(content={"status":f"Bad","email":f"{email}"})
	else:
		return         JSONResponse(content={"status":f"Bad","email":f"{email}"})
#uvicorn.run(app,host='0.0.0.0',port=8080)
