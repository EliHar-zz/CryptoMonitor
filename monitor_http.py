import getpass
import sys
import urllib2
import json
import smtplib
import time
from email.mime.text import MIMEText

print "\nLoging into your mail server...\n"
EMAIL = raw_input("Email address: ")
PWD = getpass.getpass("Email password: ")

# IFTT trigger email
REC = 'trigger@applet.ifttt.com'
SUBJECT = 'TradeAlert!'

# Gmail SMTP server info
SMTP = 'smtp.gmail.com'
PORT = 587
PING_INTERVAL = 5 #min 3 sec

# cryptocompare API params https://www.cryptocompare.com/api
# Make sure the currencies chosen are supported by the exchange
EXCHANGE = 'CCCAGG' # Can be Coinbase, Bittrex, etc...
EXTRA_PARAMS = 'MyMonitor' # Can be anything
FROM_CURR = 'BTC,ETH,LTC' # Can include all currencies supported by the api and exchange
TO_CURR = 'USD'
MAX_RETRY = 10

def sendEmail(From, To, Subject, Message):
	# Create a text/plain message
	msg = MIMEText(Message)
	msg['Subject'] = Subject
	msg['From'] = From
	msg['To'] = To

	# Send the message via our own SMTP server, but don't include the
	# envelope header.
	server = smtplib.SMTP(SMTP, PORT)
	server.ehlo()
	server.starttls()
	server.login(EMAIL, PWD)
	server.sendmail(From, To, msg.as_string())
	server.close()

def getPrices(from_curr, to_curr, exchange, max_retry):
	url = "https://min-api.cryptocompare.com/data/pricemulti?extraParams=" + \
	EXTRA_PARAMS + "&fsyms=" + FROM_CURR + "&tsyms=" + TO_CURR + "&e=" + EXCHANGE
	
	response = {}
	while (max_retry >= 0):
		try:
			response = urllib2.urlopen(url).read()
			response = json.loads(response)
		except Exception:
			print "Failed request. Retrying..."
			max_retry = max_retry - 1
			time.sleep(PING_INTERVAL - 2)
		else:
			max_retry = -1
			if 'Response' in response and response['Response'] == "Error":
				print response['Message']
				exit()	
	return response

def getPricesString(prices):
	prices_str = "===============\n"

	for currency in prices:
		prices_str += currency + ": " + str(prices[currency][TO_CURR]) + "\n"
	
	prices_str += "===============\n"

	return prices_str

# To be modified based on your alarm rules and the coins monitored
def getAlarmMessage(prices):
	message = ''

	if prices == {} or prices == None:
		print "Response is empty..."
		return ''

	btc = str(prices['BTC'][TO_CURR])
	eth = str(prices['ETH'][TO_CURR])
	ltc = str(prices['LTC'][TO_CURR])

	# BTC alarm rules
	if float(btc) < 3000:
		message += 'BTC: '+ btc + '\n'
	elif float(btc) < 3500:
		message += 'BTC: '+ btc + '\n'
	elif float(btc) < 3600:
		message += 'BTC: '+ btc + '\n'
	elif float(btc) < 3700:
		message += 'BTC: '+ btc + '\n'
	elif float(btc) < 3800:
		message += 'BTC: '+ btc + '\n'
	elif float(btc) < 4000:
		message += 'BTC: '+ btc + '\n'


	# ETH alarm rules
	if float(eth) < 290:
		message += 'ETH: '+ eth + '\n'
	elif float(eth) < 300:
		message += 'ETH: '+ eth + '\n'
	elif float(eth) < 305:
		message += 'ETH: '+ eth + '\n'
	elif float(eth) < 310:
		message += 'ETH: '+ eth + '\n'
	elif float(eth) < 320:
		message += 'ETH: '+ eth + '\n'
	elif float(eth) < 330:
		message += 'ETH: '+ eth + '\n'


	# LTC alarm rules
	if float(ltc) < 45:
		message += 'LTC: '+ ltc + '\n'
	elif float(ltc) < 50:
		message += 'LTC: '+ ltc + '\n'
	elif float(ltc) < 55:
		message += 'LTC: '+ ltc + '\n'
	elif float(ltc) < 60:
		message += 'LTC: '+ ltc + '\n'
	elif float(ltc) < 61:
		message += 'LTC: '+ ltc + '\n'

	return message

###################################
while 1:
	prices = getPrices(FROM_CURR, TO_CURR, EXCHANGE, MAX_RETRY)
	
	# Display prices
	print getPricesString(prices)

	message = getAlarmMessage(prices)

	if len(message) > 0:
		sendEmail(EMAIL, REC, SUBJECT, message)

	# wait till next request
	time.sleep(PING_INTERVAL)
