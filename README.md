# CryptoVolume: Background of sentiment & cryptocurrencies

*Note: This is a work in progress*
 
The goal is to create a model that can effectively predict the pricing of cryptocurrencies. Sentiment analysis has existed for a long time in the form of [market sentiment](https://en.wikipedia.org/wiki/Market_sentiment#Theory_of_investor_attention), where traders' perception of the market & individual stocks is measured in terms of bullish or bearish, or in other words moving upwards or downwards, respectively. Recently, many researchers have analyzed social media sentiment's impact on the market.  While market sentiment measures traders' perspective of the market,  social media sentiment statistically measures the sentiment of users on Twitter, (and/or other sites such as Facebook, Instagram, Reddit, etc.) many of which may not even be trading in the actual market. Ideally, social media sentiment abstracts out generic news and captures the general public's view on a specific company or stock. Some examples of incidents that would lead to a strong social media sentiment would be the [United Airlines incident (2017)](https://en.wikipedia.org/wiki/United_Express_Flight_3411_incident#Cultural_impact) or [Blizzard's Hong Kong player (2019)](https://www.cbsnews.com/news/blizzard-china-statement-blizzard-president-apologizes-for-hong-kong-player-ban-we-moved-too-quickly/), where both situations were EXTREMELY controversial.

Since cryptocurrency is a newer part of the market, many uncertainties still exist. The price trends are extremely hard to predict and the idea of cryptocurrencies are very controversial as well, which makes social media sentiment analysis an obvious choice to analyze cryptocurrencies.

**However, this project isn't just another sentiment analysis on cryptocurrencies.**

# CryptoVolume: The goal
So now that we know all of these forms of sentiment-related predictions exist, what will CryptoVolume do differently? Instead of analyzing the social media sentiment, CryptoVolume scrapes the volume of tweets per day mentioning 'bitcoin', 'litecoin', and 'ethereum', respectively. After obtaining this data, the goal is to combine it with the core market factors of these respective cryptocurrencies and attempt to determine a correlation between these factors in 2019.

After scraping all data, the cryptocurrencies analyzed (bitcoin, litecoin, & ethereum) will be held constant, as well as the time period. However, the lookback period in which the number of tweets are recorded will vary and attempt to be optimized to reduce the error and strengthen a correlation. This volume will then be combined with (subject to change) the implied volatility of price, idiosyncratic risk, and market capitalization. After training over the year of 2019, predictions will be attempted.

# CryptoVolume: Limitations & assumptions
- Due to run-time limitations, 2018, which is the 'year of cryptocurrencies' (I don't know if thats actually a thing) because it contains the spike of bitcoin to roughly $18k. However, scraping the data takes way too long.
- Twint will not account for typos or instances where there are additional characters in the keyword than what was specified. (i.e. 'a' will search for the word 'a', not all characters containing the letter 'a')
- Twint is actually accurate, or at least accurate enough. Twitter's API has a counts endpoint for the volume of tweets, but is a paid feature so this can't be used. (Plus this brings a whole new set of limitations)
- The relationship is causative between a high volume in tweets and not just a correlation. If this is not true, the model will have little to no substantial value.
# CryptoVolume: Current Progress
- An algorithm to scrape Twitter (included in the repository), utilizing [Twint](https://github.com/twintproject/twint) has been created. Due to the immense number of tweets containing bitcoin & amount of tweets that must be searched through, searches are broken into 10 minute intervals that are cumulatively added together to determine the volume of tweets in a given day. The input is start and end date as a [datetime object](https://docs.python.org/3/library/datetime.html) and a keyword(s). The recorded data is stored to text files to allow easy access to the data.
- A python script was created with hardcoded date ranges & keywords that will terminate upon completion. If terminated early, the start time (10 minute interval) that was to be completed next is recorded, and the script resumes from this start time. This allows the script to easily be ran in parallel

# CryptoVolume: Soon to come
- Full volume data
- Off_by as parameter of twint_scrape.py to make more user friendly *Completed - Off_by file is more or less useless now*
- If a scrape returns 0, force a retry as this is most likely due to a server issue. *Completed - Provide option to force retry blindly or request user input*
- Encountered issue when date was in a form that required modification to terminated file. Working on a fix.
