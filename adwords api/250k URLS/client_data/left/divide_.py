import csv, os

import pandas as pd

df = pd.read_csv('left_urls.csv')

i = 1
while True:
    print 'creating ', i
    temp = df.iloc[(i-1)*10500: i*10500]
    print temp.shape
    if temp.shape[0] ==0:
        break
    else:
        if not os.path.exists('url_set_' + str(i)):
            os.makedirs('url_set_' + str(i))
        temp.to_csv('url_set_' + str(i) + '/' + 'url_set_' + str(i) +'.csv',\
                    index = False, header=False)
    i +=1