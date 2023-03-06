import requests
import validators
import os
import argparse
from urllib.parse import urlparse
from dotenv import load_dotenv


def shorten_link(link, token):
    host = "https://api-ssl.bitly.com/v4"
    url = f"{host}/bitlinks"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"long_url": link}
  
    response = requests.post(url=url, 
                             headers=headers, 
                             json=payload)
    response.raise_for_status() 

    return response.json()["link"]


def get_url_without_scheme(url):
    parsed_url = urlparse(url)
    return f"{parsed_url.netloc}{parsed_url.path}"


def is_bitlink(link, token):
    host = "https://api-ssl.bitly.com/v4"
    url = f"{host}/bitlinks/{get_url_without_scheme(link)}"
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(url=url, headers=headers)
    return response.ok
  

def count_clicks(link, token):
    host = "https://api-ssl.bitly.com/v4"
    url = f"{host}/bitlinks/{get_url_without_scheme(link)}/clicks/summary"
    headers = {"Authorization": f"Bearer {token}"}
  
    response = requests.get(url=url, headers=headers)
    response.raise_for_status()

    return response.json()["total_clicks"]


def main():
    load_dotenv()

    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="link to convert")
    args = parser.parse_args()

    bitly_token = os.environ["BITLY_OAUTH_TOKEN"]
  
    link = args.url
    if not validators.url(link):
      raise TypeError("Invalid url. Please check it was type in a proper way")
    
    if is_bitlink(link=link, token=bitly_token):
        print(f"По вашей ссылке прошли: {count_clicks(link=link, token=bitly_token)} раз(а)")
    else:
        print(f"Битлинк: {shorten_link(link=link, token=bitly_token)}")

if __name__ == "__main__":
    main()