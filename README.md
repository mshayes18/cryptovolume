# CryptoVolume: Background of Sentiment & Cryptocurrencies

*Note: This is a work in progress*
 
The goal is to create a model that can effectively predict the pricing of cryptocurrencies. Sentiment analysis has existed for years in the form of [market sentiment](https://en.wikipedia.org/wiki/Market_sentiment#Theory_of_investor_attention), where traders' perception of the market & individual stocks is measured in terms of bullish or bearish, indicating if the market is moving upwards or downwards, respectively. Recently, many researchers have analyzed the impact of social media sentiment on the market.  While market sentiment measures traders' perspective of the market,  social media sentiment statistically measures the sentiment of users on Twitter, (and/or other sites such as Facebook, Instagram, Reddit, etc.) many of which may not even be trading in the actual market. Ideally, social media sentiment abstracts out generic news and captures the general public's view on a specific company or stock. Some examples of incidents that would lead to a strong social media sentiment would be the [United Airlines incident (2017)](https://en.wikipedia.org/wiki/United_Express_Flight_3411_incident#Cultural_impact) or [Blizzard's Hong Kong player (2019)](https://www.cbsnews.com/news/blizzard-china-statement-blizzard-president-apologizes-for-hong-kong-player-ban-we-moved-too-quickly/), where both situations were EXTREMELY controversial.

Since cryptocurrencies are a newer part of the market, many uncertainties still exist. The price trends do not seem to have a strong basis and the idea of cryptocurrencies are very controversial as well, making social media sentiment analysis an obvious choice to predict the behavior of cryptocurrencies.

**However, this project isn't just another sentiment analysis on cryptocurrencies.**

# CryptoVolume: The Goal
So now that we know all of these forms of sentiment-related predictions exist, what will CryptoVolume do differently? The impact of social media sentiment has been analyzed **too** frequently. While it is clearly a powerful tool, I wanted to use a lesser known metric. Instead of analyzing the social media sentiment, CryptoVolume scrapes the volume of tweets per day mentioning a specific cryptocurrency. The assumption is that a stronger volume of tweets will correspond to a greater volume in which the stock is being traded, whether it is being bought or sold. In the proof of concept, I chose to scrape and analyze Bitcoin, the most widely known cryptocurrency. After obtaining this data, the goal is to combine it with pricing factors of the respective cryptocurrency and create predictions of the price, given this data with a nueral network.

While asset-backed stocks are easier to predict given market data, these predictions cannot be made with machine learning due to a key reason. These stocks are extremely volatile towards reports and news that depend on the companies performance, which generally cannot be predicted by past data. As a result, most machine learning models will choose the previous day's pricing as the most likely value. However, cryptocurrencies differ in that they are NOT asset-backed. There is no performance reports and news is generally far more infrequent, but also potentially more severe. As a result, these predictions will be limited to short term, but also have the potential to be more accurately predicted given past data.

# CryptoVolume: Scraping & Data
The greatest limitation in this project is access to the data. Twitter does not provide an exhaustive search feature or counts endpoint in their non-enterprise API. As a result, I chose to use Twint which acts as a bot, retrieving data from each webpage. The script that was created ran on AWS using cron job's task management to schedule and kill the script by the hour, preventing parallelization which would kill the instance. After roughly 140 hours, the data was scraped for the first 306 days of 2019 and recorded into a text file. The scraped data is depicted below.

<p align="center">
 <sup>Close Price vs. Tweet Count</sup>
 </p>

![Close Price vs. Tweet Count](https://i.imgur.com/O0AxsHe.png)

# CryptoVolume: Choosing a Model
After scraping data, a neural network will be trained over the first 240 days of 2019 -- ranging from January 1st, 2019 to August 29th, 2019. After doing so, various statistical measures of the tweet count will be used to determine the best predicting factor. This statistical measure of tweet count, volume, and pricing metrics (open/close/low/high) will then be used to predict the next 60 days and compared against actual values to determine accuracy of the model.

While the tweet count is important to predictions, a raw value does not indicate the trend of the population's sentiment towards the cryptocurrency. As a result, I chose to use a moving average. Initially, I expected an exponential moving average to provide the best predictions, but some testing led to choosing a 7 day simple moving average. The data used is included as a CSV file and depicted below for easier visualization.
*Note: This may be biased, as a single data set was tested. Future testing may indicate a different average provides better performance.

<p align="center">
 <sup>Close/Open/Low/High Pricing</sup>
 </p>

![Close/Open/Low/High Pricing](https://i.imgur.com/BmgQ0Zt.png)

<p align="center">
 <sup>Close Price vs. 7-Day SMA</sup>
 </p>

![Close Price vs. 7-Day SMA](https://i.imgur.com/C2dvUtu.png)

# CryptoVolume: Predictions
After creating the model & scraping the data, the validity of the assumption that tweet count would be a strong indicator needed to be tested. Initially, I tested various parameters to determine what predicted Bitcoin pricing best, given pricing and dollar volume. After settling on these parameters, the model was given two additional columns -- a simple moving average and the tweet count. The results are depicted below.

There are 2 sets of graphs. The first pair of graphs are predictions given Open/Close/Low/High/Volume. The orange line indicates the actual pricing, while blue indicates predictions. The first 240 days are the training set, and indicated by the graph prior to the vertical blue line. Rightward of the line are the predictions, where the actual pricing for these days is NOT used in these predictions. Instead, it is merely graphed to show the accuracy of the model. The predictions are blown up to better show the accuracy and the vertical lines in this graph are used to show the start date of large price movements and allow a better visualization of when these large movements line up with the predictions on these given days. The second pair of graphs are predictions given Open/Close/Low/High/Volume/Tweet Count/7-Day SMA. The training set and parameters of the model are identical.

<p align="center">
 <sup>Volume Predictions & Training</sup>
 </p>

![Volume Predictions & Training](https://i.imgur.com/ut9M4Nm.png)

<p align="center">
 <sup>Volume Predictions (Enlarged)</sup>
 </p>

![Volume Predictions (Enlarged)](https://i.imgur.com/m1GU7t3.png)

<p align="center">
 <sup>Tweet Predictions & Training</sup>
 </p>

![Tweet Predictions & Training](https://i.imgur.com/v7M509t.png)

<p align="center">
 <sup>Tweet Predictions (Enlarged)</sup>
 </p>

![Tweet Predictions (Enlarged)](https://i.imgur.com/W9oETUl.png)

Evidently, the tweet count and moving average of this data *strongly* improves accuracy of the predictions. While small day to day movements are not accurately predicted, the tweet-based model perfectly predicts the large movements, while the model with exclusively volume/pricing data struggles to accurately make these predictions. This reinforces the idea that cryptocurrencies can be predicted by machine learning due to the fact that they are a non-asset-backed equity. Furthermore, this implies that the model is best at predicting large movements in the short term, but that the oscillation of price day to day is not easily predicted.

In an attempt to analyze the error, I attempted to measure the risk of these predictions. While a statistical error analysis would be useful, it would contain bias. As I mentioned, "large" jumps are best predicted, but what indicates "large"? By choosing a value, this is inserting bias into the model, as this value would clearly be tuned to best fit the model and as a result, potentially make the model look better than it is.

Instead, I chose to create a model on the basis that there are 4 possible situations, only one of which, is a risky and bad situation. If the model predicts an increase and the actual pricing increases or the model predicts a decrease and the actual pricing decreases, this is a positive. When the model predicts a decrease and the actual pricing increases, it is not an ideal situation, but there is no risk, as the predictions do not cause you to lose money. *However*, if the model predicts an increase and the actual pricing decreases, the model is extremely risky. As a result, I weighted the values as such, and created a graph where negative values indicate risk. Furthermore, the discrepancy from zero indicates the discrepancy between the predicted and actual.

<p align="center">
 <sup>Error Analysis</sup>
 </p>

![Error Analysis](https://i.imgur.com/mlOUdSy.png)

Thus, after seeing the graph, the conclusion that the model is risk adverse can be made. This further strengthens the proof of concept that tweet count can be used to predict the pricing of cryptocurrencies. The negative dips are minimal, and most likely due to inaccurate predictions of the oscillating price.

# CryptoVolume: Improvements
*Soon to come*
