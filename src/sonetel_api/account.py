import requests

# Generate an access token
def get_token(username: str = None, password: str = None, auth_url: str = None) -> str:
    """
    Create an API access token from the user's Sonetel email address and password.
    :param username: Your Sonetel email address.
    :param password: Your Sonetel password.
    :param auth_url: The API URL for generating access token.
    :return: Returns the access token.
    """

    if username is None or username == '':
        raise ValueError("username is required")
    elif password is None or password == '':
        raise ValueError("password is required")
    elif auth_url is None or auth_url == '':
        raise ValueError("auth_url is required")

    body = f"grant_type=password&username={username}&password={password}&refresh=no"
    auth = ('sonetel-web', 'sonetel-web')
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    r = requests.post(
        url=auth_url,
        data=body,
        headers=headers,
        auth=auth
    )

    if r.status_code == requests.codes.ok:
        data = r.json()
        if 'access_token' in data.keys():
            return data['access_token']
        else:
            return None
    else:
        print(r.json())
        r.raise_for_status()

# Get the account ID
def get_accountid(token: str = None, base_url: str = None):

    """
    Get the Sonetel account ID of a user.

    :param token: API access token generated using the token() function.
    :param base_url: The API base URL.
    :return: The Sonetel account ID.
    """

    if token is None:
        raise ValueError(token)
    elif base_url is None:
        raise ValueError(base_url)
    else:
        url = f"{base_url}/account/"
        header = {
                "Authorization": "Bearer " + token,
                "Content-Type": "application/json"
        }
        r = requests.get(url=url, headers=header)
        if r.status_code == requests.codes.ok:
            response = r.json()
            return response['response']['account_id']
        else:
            print(r.json())
            r.raise_for_status()

# Get the current prepaid balance
def get_balance(token: str = None, currency: bool = False, base_url: str = None) -> str:
    """
    Get the prepaid account balance. Example, '3.74 USD' or '3.74'

    :param token: API access token generated using the token() function.
    :param currency: Boolean value to specify if the currency should be returned or not. False by default.
    :param base_url: The API base URL.
    :return: The current prepaid balance.
    """

    if token is None:
        raise ValueError(token)
    else:
        url = f"{base_url}/account/"
        header = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json"
        }
        r = requests.get(url=url, headers=header)
        if r.status_code == requests.codes.ok:
            response = r.json()
            if currency is False:
                return response['response']['credit_balance']
            else:
                return response['response']['credit_balance'] + ' ' + response['response']['currency']
        else:
            print(r.json())
            r.raise_for_status()

# Fetch details of all users in account
def get_all_users():
    pass