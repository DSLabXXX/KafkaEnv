from kafka import KafkaProducer
import datetime


time = str(datetime.datetime.now())

producer = KafkaProducer(bootstrap_servers='localhost:9092')

producer.send('Hello-Kafka', b"time: "+str.encode(time))



