
from __future__ import unicode_literals

'''import json
import requests
import config

URL = "https://api.telegram.org/bot{}/".format(config.TOKEN)

def getJSON(url):
	response = requests.get(url)    # response is class that stores data from the url 
	jsonData  = json.loads(response.content.decode("utf-8"))   #converts json data into python dictionary
	return jsonData

def getUpdates(offset=None):
	url = URL + "getUpdates?timeout=100"
	if offset:
		url = url + "&offset={}".format(offset)   #timer is set  to 100 secs for going idle
	jsonData = getJSON(url)
	return jsonData




def getlatestUpdateID(updates):
	ids = []
	for update  in updates["result"]:
		ids.append(int(update["update_id"]))
	return max(ids)

def replyToAll(updates):
	for update in updates["result"]:
		text = update["message"]["text"]
		chatID = update["message"]["chat"]["id"]
		sendMessage(text,chatID)



def sendMessage(text,chatID):
	url = URL + "sendMessage?chat_id={}&text={}".format(chatID,text)
	response = requests.get(url)


lastUpdateID = None
while True:
	updates = getUpdates(lastUpdateID)
	if len(updates["result"])>0:
		lastUpdateID = getlatestUpdateID(updates)+1
		replyToAll(updates)

'''
import json
import requests
import config

URL = "https://api.telegram.org/bot{}/".format(config.TOKEN)
commands = ["ly","pnr","ls"]

def isCommand(text):
	command = text.split("-")[0]
	if command in commands:
		return True
	else:
	    return False	
def process(text):
	if isCommand(text):
		command = text.split("-")
		if command[0]=="ly":
		    song = command[1]
		    artist = command[2]
		    return lyrics(song, artist)
		#if command[0] == "pnr":
		#	pnr =  command[1]
		#	return pnr_status(pnr)
		#if command == "ls":
		#	train_no = command[1]
		#	return live_status(train_no)
	else:
		return text
    	
'''def pnr_status(pnr):
	apikey = "jhd3364g14"
	url = "http://api.railwayapi.com/v2/pnr-status/pnr/{}/apikey/{}/".format(pnr,apikey)
	r = requests.get(url)
	data = json.loads(r.content)
	train_name = data["train"]["name"]
	train_no = data["train"]["number"]
	from_station = data["boarding_point"]["name"]
	to_station = data["reservation_upto"]["name"]
	passengers = data["passengers"]

	for passenger in passengers:
		booking  += "S.No " + passenger["no"]+" " + passenger["current_status"]+"\n"
	output = train_name + "\n" + train_no + "\n" + "From: "+ from_station + "\n"+ to_station + "\n"
	return output + booking'''
	

def lyrics(song,artist):
	url = "https://musixmatchcom-musixmatch.p.mashape.com/wsr/1.1/matcher.lyrics.get?q_artist={}&q_track={}".format(artist,song)
	r = requests.get(url, headers={"X-Mashape-Key": "FIERseaVIDmshPr9IqYtuREhcjgzp1MK11TjsntvJpBCBJPLxz","Accept": "application/json"})
	data = json.loads(r.content)
	return data["lyrics_body"]
def extract(json):
	try:
		text = json["message"]["text"]
	except:
	    text = ""            
	chatID = json["message"]["chat"]["id"]
	return text, chatID

def getJSON(url):
    response = requests.get(url)
    jsonData = json.loads(response.content.decode("utf-8"))
    return jsonData


def getUpdates(offset=None):
    url = URL + "getUpdates?timeout=100"
    if offset:
        url = URL + "getUpdates?offset={}&timeout=1".format(offset)
    jsonData = getJSON(url)
    return jsonData


def getLatestUpdateID(updates):
    ids = []
    for update in updates["result"]:
        ids.append(int(update["update_id"]))
    return max(ids)


def replyToAll(updates):
    for update in updates["result"]:
        text = update["message"]["text"]
        chatID = update["message"]["chat"]["id"]
        sendMessage(text, chatID)


def sendMessage(text, chatID):
    url = URL + "sendMessage?chat_id={}&text={}".format(chatID, text)
    response = requests.get(url)


