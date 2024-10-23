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
    get_auth_url()

    oauth_verifier = get_oauth_verifier()

    access_token, access_token_secret = get_access_token(oauth_verifier)

    identity = client.identity()

    print("CONSUMER_KEY:", CONSUMER_KEY)
    print("CONSUMER_SECRET:", CONSUMER_SECRET)
    print("Access Token:", access_token)
    print("Access Token Secret:", access_token_secret)
    print("Identity:", identity)

def get_auth_url():
    request_token, request_secret, auth_url = client.get_authorize_url()
    print("Visit this URL to authorize: " + auth_url)
    return request_token, request_secret, auth_url

def get_oauth_verifier():
    oauth_verifier = input('Enter OAuth Verifier: ')
    return oauth_verifier

def get_access_token(oauth_verifier):
    return client.get_access_token(oauth_verifier)

main()
