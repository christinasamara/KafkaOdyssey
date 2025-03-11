import csv
import json
import datetime as dt
#from kafka import KafkaProducer
import time
import pandas as pd

sending_rate = 50  # ρυθμός αποστολής
time_value = 0
base_timestamp = dt.datetime(2024, 5, 22)

def get_dataset():
    df = pd.read_csv('vehicles_data.csv')
    df = pd.read_csv('vehicles_data.csv')
    new_column_names = ["name", "dn", "origin", "destination", "time", "link", "position", "spacing", "speed"]
    df.columns = new_column_names

    return df


df = get_dataset()
#producer = KafkaProducer(bootstrap_servers='localhost:9092')
topic = "vehicles"

for i in range(0 , 3595, sending_rate):
    # [time] column for this batch
    current_time = base_timestamp + dt.timedelta(seconds=i)

    to_send = df[(df['time'] <= i + sending_rate) & (df['time'] > i) & (df['link'] != 'waiting_at_origin_node') & (df['link'] != 'trip_end')]
    #print(to_send['time'])
    to_send['time'] = current_time.strftime('%Y-%m-%d %H:%M:%S')
    print('---------------------')

    for j in range(len(to_send)) :
        try : # AttributeError when no car       
            row_json = to_send.iloc[j].to_json()
            #producer.send(topic, row_json.encode())
            print(row_json)

        except AttributeError :
            print("No Cars")
    time.sleep(2)
    




#while time_value < 3595:
#    #producer = KafkaProducer(bootstrap_servers='localhost:9092')
#    topic = "vehicles"
#    time_value += sending_rate
#
#    with open(csv_file, 'r') as file:
#        reader = csv.DictReader(file)
#        for row in reader:
#            if int(row['t']) == time_value and row['link'] != 'waiting_at_origin_node' and row['link'] != 'trip_end':
#                timestamp = base_timestamp + timedelta(seconds=int(row['t']))
#                row['t'] = timestamp.strftime('%d/%m/%Y %H:%M:%S')
#
#                data = json.dumps(row, indent=4)
#                #producer.send(topic, data.encode())

                #print(data)
