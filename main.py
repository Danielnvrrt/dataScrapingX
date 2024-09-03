import asyncio
from twikit import Client, TooManyRequests
import time
from datetime import datetime
import csv
import os
from configparser import ConfigParser
from random import randint


# Definir el número de tweets a extraer
MINIMUM_TWEETS = 3000

# Definir la query de búsqueda. Siempre tiene que ir 
# envuelta entre comillas simples ('')
QUERY = 'tarjetita lang:es'

# Definir el nombre del fichero csv que se va a generar. Siempre tiene
# que ir envuelta entre comillas simples ('') y con la extensión .csv
# Si el nombre del fichero se repite se sobreescribirá el archivo anterior
CSV_NAME = 'tarjetita.csv'

# Archivo que contiene las cookies con las credenciales para iniciar sesión
COOKIES = 'cookies.json'


# Initialize client
client = Client('es-ES')

# Login to the client if cookies.json file does not exist
async def first_login():
    config = ConfigParser(interpolation=None)
    config.read('config.ini')
    username = config['X']['username']
    email = config['X']['email']
    password = config['X']['password']
    await client.login(auth_info_1=username, auth_info_2=email, password=password)
    client.save_cookies('cookies.json')

# Login using cookies
def login_cookies():  
    client.load_cookies(COOKIES)

# Get tweets
async def get_tweets(tweets):
    if tweets is None:
        # get tweets
        print(f'{datetime.now()} - Extrayendo tweets...')
        tweets = await client.search_tweet(QUERY, 'Latest', 20)
    else:
        wait_time = randint(5, 10)
        print(f'{datetime.now()} - Extrayendo los siguientes tweets despues de {wait_time}s...')
        time.sleep(wait_time)
        tweets = await tweets.next()

    return tweets


async def main():
    # Create a csv file if not exist
    if not os.path.exists(CSV_NAME):
        with open(CSV_NAME, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Usuario', 'Contenido', 'Ubicación'])

    # Login        
    if os.path.exists(COOKIES):
        login_cookies()
    else:
        await first_login()


    tweet_count = 0
    tweets = None
    while tweet_count < MINIMUM_TWEETS:
        try:
            tweets = await get_tweets(tweets)
        except TooManyRequests as e:
            rate_limit_reset = datetime.fromtimestamp(e.rate_limit_reset)
            print(f'\n{datetime.now()} - Límite alcanzado. Esperando hasta {rate_limit_reset}\n')
            wait_time = rate_limit_reset - datetime.now()
            time.sleep(wait_time.total_seconds())
            continue

        if not tweets:
            print(f'{datetime.now()} - No se han encontrado más tweets')
            break

        for tweet in tweets:
            if tweet._data['core']['user_results']['result']['legacy']['location'] != '':
                tweet_count += 1
                tweet_data = [tweet.user.name, tweet.text, tweet._data['core']['user_results']['result']['legacy']['location']]
                
                with open(CSV_NAME, 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(tweet_data)
                if not tweet_count < MINIMUM_TWEETS:
                    break
                if tweet_count % 100 == 0:
                    print(f'\n{MINIMUM_TWEETS - tweet_count} tweets restantes.\n')

    print(f'{datetime.now()} - {tweet_count} tweets obtenidos')


asyncio.run(main())