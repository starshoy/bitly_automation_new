# Bitly URL shortener

Project is aimed to give user an ability to:
- make shorten links via Bitly Url service
- to get the bitly link statistics

### How to install

To be able to run the project `BITLY_OAUTH_TOKEN` should be stored in .env file.
Register first on Bitly Service, to generate the token on https://app.bitly.com/settings/integrations/

Python3 should already be installed. 
Use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### How to use

To run the script url should be passed as additional argument in terminal

- To make a short link 
```commandline
$ python main.py http://google.com 
```
- To get a bitly link statistics 
```commandline
$ python main.py https://bit.ly/3EkIOz8
```

### Project Goals

This code was written for educational purposes as part of an online course for web developers at [dvmn.org](https://dvmn.org/).