import twint_scrape
from twint_scrape import scrape
import datetime

if __name__ == '__main__':
    ''' Script to run scrape function. Picks up where killed last '''
    keyword = 'bitcoin'
    start = datetime.datetime(year = 2019, month = 1, day = 24)
    end = datetime.datetime(year = 2019, month = 4, day = 1)

    file = openfile = open(str(keyword) + '_terminated.txt', 'a')
    file.close()
    file = open(str(keyword) + '_terminated.txt', 'r')
    left_off = file.read()
    file.close()
    if left_off != '':
        s_year = int(left_off[:4])
        s_month = int(left_off[5:7])
        s_day = int(left_off[8:10])
        s_hour = int(left_off[11:13])
        s_minute = int(left_off[14:16])
        start = datetime.datetime(year = s_year, month = s_month, day = s_day, hour = s_hour, minute = s_minute)
    
        file = open('off_by.txt', 'a')
        file.write(left_off + '\n')
        file.close()
        
    output = scrape(start, end, keyword)
    print(output)
