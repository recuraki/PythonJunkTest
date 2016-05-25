#!/usr/bin/env python
import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))
channel = connection.channel()
channel.queue_declare(queue='hello')

msg = dict()
msg["cmd"] = "SRXsCreate"
msg["orderid"] = 1
msg["cid"] = 1
msg["wfid"] = 1
msg["stepid"] = 1


channel.basic_publish(exchange='',
                      routing_key='SJJOB',
                      body=json.dumps(msg))
print(" [x] Sent 'Hello World!'")
connection.close()
