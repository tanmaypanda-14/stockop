# STOCKOP

STOCKOP is a one-stop solution that helps to analyze, track and learn more about the stock market. It aims to provide news and provide real-time tracking. This app focuses on bringing together multiple investment opportunities for the growing number of first-time and young investors thus bringing new generations into it.


#Sentiment analysis of articles

This the main featur of our app. Basically this fearure scraps articles from the newsapi website and runs a nlp model on it and provides us with the compund score of the article. If the compound score is positive the article is good for the performance of the stock. The same goes for the negative part. 

this thus reduces the amount of time spent by investment bankers on reading articles and is also a good way for beginners to enter this field

### Dependencies
```
pip3 install nltk newsapi-python pandas 
```

### Getting the app to run

```
git clone https://github.com/uneconomicalfairy14/stockop.git
cd stockop
python3 init.py
```


# Predictor

Another aspect of our app is the stock trades predictor that will tell the user how many stocks he/she should trade in the coming time period

We hv made use of the Random forest algorithm which works as a decision tree for us and we have also scrapped data from yahoo finance using yfinance api

you can navigate to the colab sheet by clicking on the badge below

[<img src="https://img.shields.io/badge/google-colab-brightgreen?logo=LOGO">](<https://colab.research.google.com/drive/1mA1V03Cn94mGMjxPk4ztLyhIC4bkRyTo?usp=sharing>)
