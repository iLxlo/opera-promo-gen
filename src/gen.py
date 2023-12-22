# credits: https://github.com/JOY6IX9INE/OperaGX-Discord-Promo-Gen
# https://github.com/JOY6IX9INE
import requests
import string
import random
import time
import ctypes
import os
import uuid
from random import choice
from src.config import Config

os.system('cls' if os.name == 'nt' else 'clear')

class counter:
    count = 0

red = '\x1b[31m(-)\x1b[0m'
blue = '\x1b[34m(+)\x1b[0m'
green = '\x1b[32m(+)\x1b[0m'
yellow = '\x1b[33m(!)\x1b[0m'

def get_timestamp():
    time_idk = time.strftime('%H:%M:%S')
    timestamp = f'[\x1b[90m{time_idk}\x1b[0m]'
    return timestamp

def read_message():
    with open("./data/message.txt", "r") as file:
        return file.read()

def gen_promo_link(num_links):
    message = read_message()

    with open(Config.PROXIES_FILE) as f:
        proxies = f.read().splitlines()

    generated_links = []

    for _ in range(num_links):
        proxy = choice(proxies) if proxies else None
        link = gen(proxy, message)
        if link:
            generated_links.append(link)

    with open(Config.GENERATED_LINKS_FILE, "a") as output_file:
        for link in generated_links:
            output_file.write(f"{link}")

    return generated_links


def gen(proxy, message):
    url = "https://api.discord.gx.games/v1/direct-fulfillment"
    headers = {
        "Content-Type": "application/json",
        "Sec-Ch-Ua": '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0",
    }

    data = {
        "partnerUserId": str(uuid.uuid4())
    }

    try:
        if proxy is not None:
            credentials, host = proxy.split('@')
            user, password = credentials.split(':')
            host, port = host.split(':')
            formatted_proxy = f"http://{user}:{password}@{host}:{port}"
            response = requests.post(url, json=data, headers=headers, proxies={'http': formatted_proxy, 'https': formatted_proxy}, timeout=5)
        else:
            response = requests.post(url, json=data, headers=headers, timeout=5)

        if response.status_code == 200:
            token = response.json().get('token')
            if token:
                counter.count += 1
                ctypes.windll.kernel32.SetConsoleTitleW(
                        f"Opera Gx Promo Gen | By iLxlo"
                        f" | Generated : {counter.count}")
                link = f"https://discord.com/billing/partner-promotions/1180231712274387115/{token}"
                print(f"{get_timestamp()} {green} Generated Promo Link : {link}")
                return f"{message}{link}"
        elif response.status_code == 429:
            print(f"{get_timestamp()} {yellow} You are being rate-limited!")
        else:
            print(f"{get_timestamp()} {red} Request failed : {response.status_code}")
    except Exception as e:
        print(f"{get_timestamp()} {red} Request Failed : {e}")

    return None 

if __name__ == "__main__":
    generated_links = []
    for _ in range(Config.NUM_THREADS):
        link = gen_promo_link()
        if link:
            generated_links.extend(link)

    with open("./data/output.txt", "w") as output_file:
        for link in generated_links:
            output_file.write(f"{link}")
