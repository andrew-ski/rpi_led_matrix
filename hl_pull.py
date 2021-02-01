import time

while True:
  with open("hl_csv.csv", 'r') as f:
    print(f.readlines()[-1]) #or your own manipulations
    f.close()
    time.sleep(3)
