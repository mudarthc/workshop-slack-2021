import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask
from slackeventsapi import SlackEventAdapter

env_path = Path('.')/ '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)

slack_event_adapter = SlackEventAdapter(os.environ['SIGNING_SECRET'],'/slack/events', app)

client = slack.WebClient(token= os.environ['SLACK_TOKEN'])
BOT_ID = client.api_call("auth.test")['user_id']


@slack_event_adapter.on('message')
def message(payload):
	event = payload.get('event', {})
	channel_id = event.get('channel')
	user_id = event.get('user')
	text= event.get('text')
	if BOT_ID != user_id:
		if (text == 'Ontario' or text == "ontario"):
			client.chat_postMessage(channel=channel_id, text="Crisis Lines in Ontario: https://www.talk4healing.com/ , http://www.awhl.org/?gclid=EAIaIQobChMIhY-pkuCS6AIV0ODICh3TSwUNEAAYASAAEgL7n_D_BwE , http://hope247.ca/")
		elif (text == 'british columbia' or text == "British Columbia"):
			client.chat_postMessage(channel=channel_id, text="Crisis Line in British Columbia: https://www2.gov.bc.ca/gov/content/justice/criminal-justice/victims-of-crime/victimlinkbc")
		elif (text == 'Alberta' or text == "alberta"):
			client.chat_postMessage(channel=channel_id, text="Crisis Lines in Alberta: http://www.calgarycasa.com/ , https://casasc.ca/ , https://thedragonflycentre.com/")
		elif (text == 'Manitoba' or text == "manitoba"):
			client.chat_postMessage(channel=channel_id, text="Crisis Line in Manitoba: http://klinic.mb.ca/in-person-counselling/sexual-assault-crisis-counselling/")
		else:
			client.chat_postMessage(channel=channel_id, text="If you are in immediate DANGER or fear for your safety, please CALL 911.")



if __name__ == "__main__": 
 	app.run(debug=True)
