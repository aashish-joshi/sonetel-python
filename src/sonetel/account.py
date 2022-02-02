import requests

# Generate an access token
def token(username: str, password: str, auth_url: str = 'https://api.sonetel.com/SonetelAuth/beta/oauth/token',
          refresh: str = "no", grant_type: str = "password", refresh_token: str = None) -> dict:
    """
    Create an API access token from the user's Sonetel email address and password.
    Optionally, generate a refresh token as well. Set the `grant_type` to `refresh_token` to refresh an
    existing access token.
    More information is available at https://docs.sonetel.com/docs/sonetel-documentation/YXBpOjExMzI3NDM3-authentication

    :param username: Your Sonetel email address.
    :param password: Your Sonetel password.
    :param auth_url: The API URL for generating access token.
    :param refresh: Optional. Flag to control whether a refresh token is included in the response. Defaults to 'no'
    :param grant_type: Optional. The OAuth2 grant type. Defaults to 'password'
    :parameter refresh_token: Optional. Pass the `refresh_token` in this field to generate a new access_token.
    :return: Returns the access token.
    """

    if grant_type == 'refresh_token' and refresh_token is None:
        raise ValueError("A refresh_token is needed when grant type is refresh_token.")

    # Prepare the request body.
    body = f"grant_type={grant_type}&username={username}&password={password}&refresh={refresh}"

    # Add the refresh token to the request body if passed to the function
    if refresh_token is not None:
        body += f"&refresh_token={refresh_token}"

    auth = ('sonetel-web', 'sonetel-web')

    # Prepare the request headers
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    # Send the request
    r = requests.post(
        url=auth_url,
        data=body,
        headers=headers,
        auth=auth
    )

    # Check the response and handle accordingly.
    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        print(r.json())
        r.raise_for_status()


# Get information about the Sonetel account
def get_account(token: str, base_url: str = 'https://public-api.sonetel.com', return_only_accountid: bool = False):

    """
    Get information about Sonetel account such as the account ID, prepaid balance, currency, country, etc.
    More information is available at https://docs.sonetel.com/docs/sonetel-documentation/b3A6MTUyNTkwNTM-get-your-account-information

    :param token: API access token generated using the token() function.
    :param base_url: The API base URL.
    :param return_only_accountid: Optional. Returns only the account ID string if set to true. Else, returns the complete JSON response.
    :return: A dict with the the Sonetel account details.
    """

    # Prepare the request Header
    header = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json"
    }

    # Send the request
    r = requests.get(
        url=f"{base_url}/account/",
        headers=header)

    # Check the response and handle accordingly
    if r.status_code == requests.codes.ok:
        response = r.json()
        if not return_only_accountid:
            return response
        else:
            return response['response']['account_id']
    else:
        print(r.json())
        r.raise_for_status()


# Get the current prepaid balance
def get_balance(token: str, base_url: str = 'https://public-api.sonetel.com', currency: bool = False) -> str:
    """
    Get the prepaid account balance. Example, '3.74 USD' or '3.74'.
    More information is available at https://docs.sonetel.com/docs/sonetel-documentation/b3A6MTUyNTkwNTM-get-your-account-information

    :param token: API access token generated using the token() function.
    :param base_url: The API base URL.
    :param currency: Optional. Flag to specify if the currency should be returned or not. Defaults to False
    :return: The current prepaid balance.
    """

    # Prepare the request Header
    header = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json"
    }

    # Send the request
    r = requests.get(
        url=f"{base_url}/account/",
        headers=header)

    # Check the response and handle accordingly
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
def get_all_users(token: str, accountid: str, base_url: str = 'https://public-api.sonetel.com') -> list:
    """
    Get a list of all the users in the Sonetel account along with their settings such as title, email, password status, etc.
    More information is available at https://docs.sonetel.com/docs/sonetel-documentation/b3A6MTY4MzEyMDQ-list-all-users

    :param token: API access token generated using the token() function.
    :param accountid: Your Sonetel account ID.
    :param base_url: The API base URL.
    :return: Returns a list containing the user information
    """

    # Prepare the request Header
    request_header = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json"
    }

    # Send the request
    r = requests.get(
        url=f'{base_url}/account/{accountid}/user/',
        headers=request_header
    )
    # Check the response and handle accordingly
    if r.status_code == requests.codes.ok:
        response = r.json()
        return response['response']
    else:
        print(r.json())
        r.raise_for_status()
