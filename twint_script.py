import twint_scrape
from twint_scrape import scrape
import datetime

if __name__ == '__main__':
    ''' Script to run scrape function. Picks up where killed last '''
    # Enter parameters for scraping
    keyword = 'bitcoin'
    start = datetime.datetime(year = 2019, month = 1, day = 24)
    end = datetime.datetime(year = 2019, month = 4, day = 1)
    # Don't modify
    off_by = 0

    # Ensure file exists, create if not
    file = openfile = open(str(keyword) + '_terminated.txt', 'a')
    file.close()
    # Read file of where script terminated last
    file = open(str(keyword) + '_terminated.txt', 'r')
    left_off = file.read()
    file.close()
    if left_off != '':
        # Set start date to time in which it terminated at
        s_year = int(left_off[:4])
        s_month = int(left_off[5:7])
        s_day = int(left_off[8:10])
        s_hour = int(left_off[11:13])
        s_minute = int(left_off[14:16])
        start = datetime.datetime(year = s_year, month = s_month, day = s_day, hour = s_hour, minute = s_minute)

        # Write this time & value in a file to show script was killed,
        # use the value as input to scrape since that is tweets scraped
        # thus far on that date
        file = open(str(keyword) + '_off_by.txt', 'a')
        file.write(left_off + '\n')
        file.close()
        off_by = int(left_off[20:])
        
    output = scrape(start, end, keyword, off_by)
    print(output)
