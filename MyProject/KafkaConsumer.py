from kafka import KafkaConsumer

consumer = KafkaConsumer(client_id='abc', bootstrap_servers='localhost:9092',
                            group_id='my-group3', auto_offset_reset='latest', enable_auto_commit=False)
consumer.subscribe(['Hello-Kafka'])


# consumer.partitions_for_topic('Hello-Kafka')
# consumer.seek(consumer.partitions_for_topic('Hello-Kafka'), 29560)


print('Kafka Consumer Start...')

for message in consumer:
    # print('my message '+str(message))
    print('my message '+str(message.value))

