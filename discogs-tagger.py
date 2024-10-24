import discogs_client
import os

from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
# TOKEN = os.getenv("TOKEN")

client = discogs_client.Client(
    'discogs_tagger/0.1',
    consumer_key = CONSUMER_KEY,
    consumer_secret = CONSUMER_SECRET,
    token = ACCESS_TOKEN, #TOKEN
    secret = ACCESS_TOKEN_SECRET
)

def main():
    if ACCESS_TOKEN and ACCESS_TOKEN_SECRET:
        print("Using stored access token and secret.")
        identity = client.identity()
        print("Identity:", identity)
    else:
        print("No stored access token found. Starting OAuth flow.")
        get_auth_url()
        oauth_verifier = get_oauth_verifier()
        access_token, access_token_secret = get_access_token(oauth_verifier)
        store_tokens(access_token, access_token_secret)
        identity = client.identity()
        print("Identity:", identity)

    # print("CONSUMER_KEY:", CONSUMER_KEY)
    # print("CONSUMER_SECRET:", CONSUMER_SECRET)
    # print("Access Token:", access_token)
    # print("Access Token Secret:", access_token_secret)
    # print("Identity:", identity)

def get_auth_url():
    request_token, request_secret, auth_url = client.get_authorize_url()
    print("Visit this URL to authorize: " + auth_url)
    return request_token, request_secret, auth_url

def get_oauth_verifier():
    oauth_verifier = input('Enter OAuth Verifier: ')
    return oauth_verifier

def get_access_token(oauth_verifier):
    return client.get_access_token(oauth_verifier)

def store_tokens(access_token, access_token_secret):
    with open('.env', 'a') as f:
        f.write(f"TOKEN={access_token}\n")
        f.write(f"TOKEN_SECRET={access_token_secret}\n")
    print("Tokens saved to .env file.")

main()
