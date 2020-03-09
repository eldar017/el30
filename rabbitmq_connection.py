import pika
import traceback

host = "172.18.51.120"
port = 5672
virtual_host = '/'
username = 'rabbit'
password = 'rabbit'
ex_name = 'ex_om'
q_name = 'q_om'
rk = 'rk_om'
credentials = pika.PlainCredentials(username, password)
parameters = pika.ConnectionParameters(host,
                                   port,
                                   virtual_host,
                                   credentials)

connection = pika.BlockingConnection(parameters)

channel = connection.channel()

channel.queue_declare(queue=q_name)

message = 'Python Queue - Message Sent from sender.py {N|T}'
i =0
while i in range(10):
    channel.basic_publish(exchange=ex_name,
                          routing_key=rk,
                          body=(message))
    i += 1
    print(i)
    print(" [x] Sent 'Hello World!'")

connection.close()
