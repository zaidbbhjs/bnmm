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
@app.get('/api/gmail/{gmail}')
async def ga(gmail: str, request: Request):

    global a,tl,cok,yy
    f5i =  open('host.txt','r').read().splitlines()
    fi =  open('token.txt','r').read().splitlines()
    try:
        tl =  random.choice(fi)
        host =  random.choice(f5i)
    except :
        n1=''.join(cc(yy)for i in range(rr(6,9)))
        n2=''.join(cc(yy)for i in range(rr(3,9)))
        host=''.join(cc(yy)for i in range(rr(15,30)))
        cookies = {
      '__Host-GAPS': host,
  }
        headers = {
      'authority': 'accounts.google.com',
      'accept': '*/*',
      'accept-language': 'en-US,en;q=0.9',
      'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
      'google-accounts-xsrf': '1',
      'origin': 'https://accounts.google.com',
      'referer': 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp',
      'user-agent': gg(),
  }
        data = {
    'f.req': '["AEThLlz4luDk2yFWsQRU_KlZsoYtu6wNeZxocOIcj1BG20WA078YKjPYBHlgL8qq82PZDts7UWS0jQ2QmOU-Fh9UrfhgvRXgjlgxmWn2VptjYAi-emfCuzIezrd4IbKkWLbdSPxnA_mTSmtNVuiqJU_VZfR-KE3MtZf8qft2oqLdafTBloXqbn65aQv_o_DuwIR7pG6MmB_g","'+n1+'","'+n2+'","'+n1+'","'+n2+'",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
    'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',
  }
        response = pp(
      'https://accounts.google.com/_/signup/validatepersonaldetails',
      cookies=cookies,
      headers=headers,
      data=data,
  )
        tl=str(response.text).split('",null,"')[1].split('"')[0]
        host=response.cookies.get_dict()['__Host-GAPS']
        for i in range(2):
        	print("wait")
        	with open("token.txt","a") as f:
        		f.write(tl+"\n")
        	with open("host.txt","a") as f:
        		f.write(host+"\n")
    cookies = {
    '__Host-GAPS': host
  }
    import requests
    email=gmail
    n1=''.join(cc(yy)for i in range(rr(6,9)))
    n2=''.join(cc(yy)for i in range(rr(3,9)))
    host=''.join(cc(yy)for i in range(rr(15,30)))
    cookies = {
      '__Host-GAPS': host,
  }
    headers = {
      'authority': 'accounts.google.com',
      'accept': '*/*',
      'accept-language': 'en-US,en;q=0.9',
      'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
      'google-accounts-xsrf': '1',
      'origin': 'https://accounts.google.com',
      'referer': 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp',
      'user-agent': gg(),
  }
    data = {
    'f.req': '["AEThLlz4luDk2yFWsQRU_KlZsoYtu6wNeZxocOIcj1BG20WA078YKjPYBHlgL8qq82PZDts7UWS0jQ2QmOU-Fh9UrfhgvRXgjlgxmWn2VptjYAi-emfCuzIezrd4IbKkWLbdSPxnA_mTSmtNVuiqJU_VZfR-KE3MtZf8qft2oqLdafTBloXqbn65aQv_o_DuwIR7pG6MmB_g","'+n1+'","'+n2+'","'+n1+'","'+n2+'",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
    'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',
  }
    response = pp(
      'https://accounts.google.com/_/signup/validatepersonaldetails',
      cookies=cookies,
      headers=headers,
      data=data,
  )
    tl=str(response.text).split('",null,"')[1].split('"')[0]
    host=response.cookies.get_dict()['__Host-GAPS']
    print(tl,host)
    tl=tl
    host=host
    if "@" in email:
    	email=email.split("@")[0]
    else:
    	pass
    cookies = {
    '__Host-GAPS': host
  }
    url = f"https://accounts.google.com/_/signup/usernameavailability?hl=ar&TL={tl}&_reqid=756176&rt=j" 


    headers = {

	 'Accept': '*/*',

	 'Accept-Encoding': 'gzip, deflate, br, zstd',

	 'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',

	 'Content-Length': '1028',

	 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',

	 'Google-Accounts-Xsrf': '1',

	 'Origin': 'https://accounts.google.com',

	 'Referer': f'https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp&TL={tl}',

	 'Sec-Ch-Ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',

	 'Sec-Ch-Ua-Arch': '"x86"',

	 'Sec-Ch-Ua-Bitness': '"64"',

	 'Sec-Ch-Ua-Full-Version': '"123.0.6312.106"',

	 'Sec-Ch-Ua-Full-Version-List': '"Google Chrome";v="123.0.6312.106", "Not:A-Brand";v="8.0.0.0", "Chromium";v="123.0.6312.106"',

	 'Sec-Ch-Ua-Mobile': '?0',

	 'Sec-Ch-Ua-Model': '""',

	 'Sec-Ch-Ua-Platform': '"Windows"',

	 'Sec-Ch-Ua-Platform-Version': '"10.0.0"',

	 'Sec-Ch-Ua-Wow64': '?0',

	 'Sec-Fetch-Dest': 'empty',

	 'Sec-Fetch-Mode': 'cors',

	 'Sec-Fetch-Site': 'same-origin',

	 'User-Agent': gg(),

	 'X-Chrome-Id-Consistency-Request': 'version=1,client_id=77185425430.apps.googleusercontent.com,device_id=1ea6888d-8951-4adc-86b8-a87aa2b417d2,signin_mode=all_accounts,signout_mode=show_confirmation',

	 'X-Client-Data': 'CKa1yQEIlbbJAQimtskBCKmdygEIw/nKAQiUocsBCIWgzQEI4+zNAQjahM4BCLOFzgEI+4XOAQjnhs4BCMC3yiIImu7LIhizqcoBGPXJzQEYmPXNARjS/s0BGNiGzgE=Decoded:',

	 'X-Same-Domain': '1',

} 


    data = {

	 'continue': 'https://mail.google.com/mail/u/0/',

	 'service': 'mail',

	 'theme': 'mn',

	 'ddm': '0',

	 'f.req': f'["TL:{tl}","{email}",1,0,1,null,0,303022]',

	 'azt': 'AFoagUXgnd8kyIQjiP5mK5OO7paE_wJNsg:1712320514767',

	 'cookiesDisabled': 'false',

	 'deviceinfo': '[null,null,null,null,null,"IQ",null,null,null,"GlifWebSignIn",null,[null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"1ea6888d-8951-4adc-86b8-a87aa2b417d2",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5]],null,null,null,null,1,null,0,1,"",null,null,2,1]',

	 'gmscoreversion': 'undefined',

	 'flowName': 'GlifWebSignIn',

	 'checkConnection': 'youtube:695',

	 'checkedDomains': 'youtube',

	 'pstMsg': '1',

}
    r=requests.post(url,headers=headers,data=data,cookies=cookies).text
    print(r)
    if "er" in r :
    	
    	ln = open('token.txt', 'r').read().splitlines()
#    	print('7')
    	if tl in ln:
    	       with open("token.txt", "r") as f:
    	       	lines = f.readlines()
    	       with open("token.txt", "w") as f:
    	                   for line in lines:
    	                       if line.strip("\n") != "{}".format(tl):
    	                       	f.write(line)
    	                       print('ok')
    	                   n1=''.join(cc(yy)for i in range(rr(6,9)))
    	                   n2=''.join(cc(yy)for i in range(rr(3,9)))
    	                   host=''.join(cc(yy)for i in range(rr(15,30)))
    	                   cookies = {
      '__Host-GAPS': host,
  }
    	                   headers = {
      'authority': 'accounts.google.com',
      'accept': '*/*',
      'accept-language': 'en-US,en;q=0.9',
      'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
      'google-accounts-xsrf': '1',
      'origin': 'https://accounts.google.com',
      'referer': 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp',
      'user-agent': gg(),
  }
    	                   data = {
    'f.req': '["AEThLlz4luDk2yFWsQRU_KlZsoYtu6wNeZxocOIcj1BG20WA078YKjPYBHlgL8qq82PZDts7UWS0jQ2QmOU-Fh9UrfhgvRXgjlgxmWn2VptjYAi-emfCuzIezrd4IbKkWLbdSPxnA_mTSmtNVuiqJU_VZfR-KE3MtZf8qft2oqLdafTBloXqbn65aQv_o_DuwIR7pG6MmB_g","'+n1+'","'+n2+'","'+n1+'","'+n2+'",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
    'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',
  }
    	                   response = pp(
      'https://accounts.google.com/_/signup/validatepersonaldetails',
      cookies=cookies,
      headers=headers,
      data=data,
  )
    	                   tl=str(response.text).split('",null,"')[1].split('"')[0]
    	                   host=response.cookies.get_dict()['__Host-GAPS']
    	                   for i in range(2):
    	                   	print("wait")
    	                   	with open("token.txt","a") as f:f.write(tl+"\n")
    	                   	with open("host.txt","a") as f:f.write(host+"\n")
                       
    elif '"gf.uar",1' in r:
    	return         JSONResponse(content={"status":"Good"})
    elif '"gf.uar",2' in r:
    	return         JSONResponse(content={"status":"Bad"})
    elif '"gf.uar",3' in r:
    	return         JSONResponse(content={"status":"Error"})
    else:
    	return         JSONResponse(content={"status":"Error"})
uvicorn.run(app,host='0.0.0.0',port=8080)
