import time
import csv

while True:
  with open ('dht_data.csv') as csv_file:
    csv_reader=csv.DictReader(csv_file,delimiter=',')
    line_count=0
    for row in csv_reader:
      temp=row["temperature"]
      humidity=row["humidity"]
    print(temp)
    print(humidity)
    csv_file.close()
    time.sleep(.005)
