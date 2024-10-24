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
    # read existing .env file
    with open('.env', 'r') as f:
        lines = f.readlines()

    # prepare updated lines
    updated_lines = []
    found_access_token = False
    found_access_token_secret = False

    for line in lines:
        if line.startswith("ACCESS_TOKEN="):
            updated_lines.append(f"ACCESS_TOKEN={access_token}\n")
            found_access_token = True
        elif line.startswith("ACCESS_TOKEN_SECRET="):
            updated_lines.append(f"ACCESS_TOKEN_SECRET={access_token_secret}\n")
            found_access_token_secret = True
        else:
            updated_lines.append(line)

    # add new tokens if not found
    if not found_access_token:
        updated_lines.append(f"ACCESS_TOKEN={access_token}\n")
    if not found_access_token_secret:
        updated_lines.append(f"ACCESS_TOKEN_SECRET={access_token_secret}\n")

    # write updated .env file
    with open('.env', 'w') as f:
        f.writelines(updated_lines)

    print("Tokens saved to .env file.")

main()
