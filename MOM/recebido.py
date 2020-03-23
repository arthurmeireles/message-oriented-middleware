#!/usr/bin/env python
import pika
valores = []



#mesma coisa da outra parte
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='soma')

def callback(ch, method, properties, body):
    global valores
    body = int(body)
    valores.append(body)

    print("Soma = %d"%sum(valores)) 

channel.basic_consume(
    queue='soma', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

