#!/usr/bin/python3

### BEGIN INIT INFO
# Provides:	slack-startup-notify
# Required-Start:
# Required-Stop:
# Default-Start:	2 3 4 5
# Default-Stop:	0 1 6
# Short-Description:	Slack alert of system startup
# Description:	Slack alert of system startup
### END INIT INFO

import json
import urllib3
import socket
import certifi

hostname = socket.gethostname()

# Slack incoming web hook URL
slack_url = 'https://hooks.slack.com/services/YOUR_INCOMMING_WEBHOOK_URL'

def SendToSlack(output_data):
	http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())
	req = http.request("POST", slack_url, body=json.dumps(output_data), headers={'Content-Type': 'application/json'})
	return;

output_data = {}
output_data['text'] = 'Server Status Change'
output_data['response_type'] = "ephemeral"
output_data['attachments'] = [ {'text' : hostname + ' is coming up', 'color': 'good' } ]

SendToSlack(output_data)
