#!/usr/bin/env python

### BEGIN INIT INFO
# Provides:	slack-shutdown-notify
# Required-Start:
# Required-Stop:
# Default-Start:	2 3 4 5
# Default-Stop:	0 1 6
# Short-Description:	Slack alert of system shutdown
# Description:	Slack alert of system shutdown
### END INIT INFO

import json
import urllib2
import socket

hostname = socket.gethostname()

# Slack incoming web hook URL
slack_url = 'https://hooks.slack.com/services/YOUR_INCOMMING_WEBHOOK_URL'

def SendToSlack(output_data):
	req = urllib2.Request(slack_url)
	req.add_header('Content-Type', 'application/json')
	response = urllib2.urlopen(req, json.dumps(output_data))
	return;

output_data = {}
output_data['text'] = 'Server Status Change'
output_data['response_type'] = "ephemeral"
output_data['attachments'] = [ {'text' : hostname + ' is going down', 'color': 'danger' } ]

SendToSlack(output_data)
