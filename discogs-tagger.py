import discogs_client
import os

from dotenv import load_dotenv

load_dotenv()

CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
TOKEN = os.getenv("TOKEN")

client = discogs_client.Client(
    'discogs_tagger/0.1',
    consumer_key = CONSUMER_KEY,
    consumer_secret = CONSUMER_SECRET,
    token = TOKEN
)

def main():
    # TO-DO: display URL to user in a more user friendly way
    print(get_auth_url())

    oAuth_access_token = input('Enter oAuth Access Token: ')
    client.get_access_token(oAuth_access_token)
    identity = client.identity()

    print(CONSUMER_KEY)
    print(CONSUMER_SECRET)
    print(TOKEN)
    print(client)
    print(oAuth_access_token)
    print(identity)

def get_auth_url():
    return client.get_authorize_url()

main()
