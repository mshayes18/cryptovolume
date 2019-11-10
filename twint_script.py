import twint_scrape
from twint_scrape import scrape
import datetime

if __name__ == '__main__':
    ''' Script to run scrape function. Picks up where killed last '''
    # Enter parameters for scraping
    keyword = 'bitcoin'
    start = datetime.datetime(year = 2019, month = 2, day = 16)
    end = datetime.datetime(year = 2019, month = 4, day = 1)
    # Don't modify (default to 0 if not left off mid-script)
    off_by = 0

    # Ensure file exists, create if not
    file = openfile = open(str(keyword) + '_terminated.txt', 'a')
    file.close()
    # Read file of where script terminated last
    file = open(str(keyword) + '_terminated.txt', 'r')
    left_off = file.read()
    file.close()
    if left_off != '':
        # Set start date to time in which it terminated at, but as new
        # parameter so that same file is modified in twint_scrape
        s_year = int(left_off[:4])
        s_month = int(left_off[5:7])
        s_day = int(left_off[8:10])
        s_hour = int(left_off[11:13])
        s_minute = int(left_off[14:16])
        new_start = datetime.datetime(year = s_year, month = s_month, day = s_day, hour = s_hour, minute = s_minute)
        # Tweets scraped thus far on this date
        off_by = int(left_off[20:])
        output = scrape(new_start, end, keyword, start, off_by)
        
    else:
        output = scrape(new_start, end, keyword)
