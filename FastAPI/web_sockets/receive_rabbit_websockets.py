# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 12:19:48 2020

@author: krish
"""

import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#channel.exchange_declare(exchange='logs', exchange_type='fanout')
channel.exchange_declare(exchange='Actions', exchange_type='fanout')
channel.queue_declare(queue='action2', durable=True)
#result = channel.queue_declare(queue='check', exclusive=True)
#queue_name = result.method.queue
severities = 'info'
#channel.queue_bind(exchange='logs', queue=queue_name)
channel.queue_bind(
        exchange='Actions', queue='action2')#, rc1outing_key='action2')

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))



channel.basic_consume(
    queue='action2', on_message_callback=callback, auto_ack=True)

channel.start_consuming()






# severities = 'info'
# if not severities:
#     sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
#     sys.exit(1)

# for severity in severities:
#     channel.queue_bind(
#         exchange='direct_logs', queue=queue_name, routing_key=severity)

# print(' [*] Waiting for logs. To exit press CTRL+C')


# def callback(ch, method, properties, body):
#     print(" [x] %r:%r" % (method.routing_key, body))


# channel.basic_consume(
#     queue=queue_name, on_message_callback=callback, auto_ack=True)

# channel.start_consuming()