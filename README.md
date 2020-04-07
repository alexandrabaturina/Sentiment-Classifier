# Sentiment Classifier

**Sentiment Classifier** application (```sentiment_classifier.py```) is a tool for analyzing tweet data and defining how positive or negative each tweet is. After running the application, the following data is written to the ```resulting_data.csv``` file.
* *Number of retweets*
* *Number of replies*
* *Positive score* — how many happy words are in the tweet 
* *Negative score* –  how many negative words are in the tweet
* *Net score* – how positive or negative the tweet is overall

**Sentiment Classifier** application is build as the final project of the [Python Functions, Files, and Dictionaries](https://www.coursera.org/learn/python-functions-files-dictionaries/home/welcome) course on [Coursera](https://www.coursera.org/) platform.

## Getting Started
### Prerequisites
To use **Sentiment Classifier**, the following files are required.
* ```project_twitter_data.csv``` contains semi-randomly generated tweet data is ```csv``` format
* ```positive_words.txt``` contains a list of words that express positive sentiment
* ```negative_words.txt``` contains a list of words that express negative sentiment

The following folder structure should be created.
```sh
files/
    negative_words.txt
    positive_words.txt
    project_twitter_data.csv
sentiment_classifier.py
```
The ```resulting_data.csv``` file will be also created in the ```files``` directory.

### Running
To run **Sentiment Classifier** from the terminal, use the following command.
```sh
$ python3 sentiment_classifier.py
```
