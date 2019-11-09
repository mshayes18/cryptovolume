import twint
from twint import run
import datetime

def scrape(start, finish, keyword):
    ''' Given a start/finish datetime instance and keyword(s) to scrape for,
    search and return a dictionary with first key as start date '''
    # Initialize twint configuration
    c = twint.Config()
    c.Search = keyword
    c.Pandas = True
    c.Hide_output = True
    c.Retries_count = 100
    c.Count = True #To ensure running

    # Dictionary to be returned
    daily = {}
    # Key counter, i = 0 is start date
    i = 0
    num_per_day = 0
    # timedelta value
    time_span = finish - start
    # Increment by a timedelta value of 10 minutes
    time_add = 10
    incr = start + datetime.timedelta(minutes = time_add)

    # Create file write num_per_day for each day in file and name by start date
    # Use second file to keep track of parameters if terminated early
    filename = str(keyword) + '_' + str(start)[:10] + '.txt'
    file = open(filename, 'a')
    
    # Increment start/finish dates until the end date is reached
    while time_span != datetime.timedelta(0):
        # Use new start, incr values to search
        start_new = str(start)
        incr_new = str(incr)
        # print(start_new, incr_new) # Can comment out
        c.Since = start_new
        c.Until = incr_new
        twint.run.Search(c)
        # Store tweets in a variable, keep track of number of tweets
        tweets = twint.storage.panda.Tweets_df
        num_per_day += len(tweets)
        
        # If hour & min = 0, day has changed. Thus, reset num_per_day vals
        # and increment key counter
        if incr.hour == 0 and incr.minute == 0:
            file.write(str(num_per_day) + '\n')
            file.close
            file = open(filename, 'a')
            daily[i] = num_per_day
            num_per_day = 0
            i += 1

        # After a search has been conducted, keep track of where to pick up
        # again if terminated early.
        # After search & num_per_day reset to ensure that num_per_day is
        # the sum of tweets thus far on that day with start time incr
        file2 = open(str(keyword) + '_terminated.txt', 'w')
        file2.write(str(incr) + '  ' + str(num_per_day)) # time for next start
        file2.close
            
        # decrease time discrepancy and increment start, incr
        time_span = time_span - datetime.timedelta(minutes = 10)
        start = incr
        # print(start) # Can comment out
        incr = incr + datetime.timedelta(minutes = time_add)
        # print(incr) # Can comment out
        
    file.write(str(num_per_day) + '\n')
    file.close
    
    # If the loop terminated early, append if not in dictionary
    if num_per_day not in daily:
        daily[i] = num_per_day
        file = open(filename, 'a')
        file.write(str(num_per_day) + '\n')
        file.close
    return daily

# Sources/Libraries
''' https://docs.python.org/3/library/datetime.html#examples-of-usage-timedelta
https://github.com/twintproject/twint '''
