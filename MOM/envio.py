
#importa o pika
import pika

#abre a conexão
connection = pika.BlockingConnection(
    #passa o parametro
    pika.ConnectionParameters(host='localhost'))
#chama o canal da conexão     
channel = connection.channel()

#declaro o nome da conexão
channel.queue_declare(queue='soma')

a = input()
b = input()

channel.basic_publish(exchange='', routing_key='soma', body=a)
channel.basic_publish(exchange='', routing_key='soma', body=b)

print("Mensagem enviada")

#fecha a conexão
connection.close()