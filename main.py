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

yy='azertyuiopmlkjhgfdsqwxcvbn'
@app.get('/check/{id}')
def check(id):
	with open("True.txt", 'r') as file:
		lines = file.read().split("\n")
	print(lines)
	if id in lines:
		return         JSONResponse(content={"status":"Good"})
	else:
		return         JSONResponse(content={"status":"Bad"})
@app.get('/add/{id}')
def add(id):
	with open("True.txt","a") as f:
		f.write(id+"\n")
	return         JSONResponse(content={"status":"Good"})
#uvicorn.run(app,host='0.0.0.0',port=8080)
