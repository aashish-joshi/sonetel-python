import json
import requests

# Create a phone number subscription
def buy_number(token: str = None, base_url: str = None, accountid: str = None, number=None) -> dict:
    """
    Buy a phone number that is available for purchase based on the /availablephonenumber API endpoint.
    :param token: API access token generated using the token() function.
    :param base_url: The API base URL.
    :param accountid: Your Sonetel account ID.
    :param number: the phone number to add to your account.
    :return: Dict containing the response in case of success.
    """
    if number is None:
        raise ValueError(number)
    elif token is None:
        raise ValueError(token)
    elif accountid is None:
        raise ValueError(accountid)
    elif base_url is None:
        raise ValueError(base_url)
    else:
        body = {
            "phnum": number
        }
        request_header = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json"
        }

        r = requests.post(
            url=f'{base_url}/account/{accountid}/phonenumbersubscription/',
            data=json.dumps(body),
            headers=request_header
        )
        if r.status_code == requests.codes.ok:
            return r.json()
        else:
            r.raise_for_status()

# List existing phone number subscriptions.
def list_all_numbers(token: str = None, base_url: str = None, accountid: str = None) -> dict:
    """
    List all the phone numbers present in the account.

    :param token: API access token generated using the token() function.
    :param base_url: The API base URL.
    :param accountid: Your Sonetel account ID.
    :return: Returns a dict containing the response from the API.
    """
    if base_url is None:
        raise ValueError(base_url)
    elif token is None:
        raise ValueError(token)
    elif accountid is None:
        raise ValueError(accountid)
    else:
        request_header = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json"
        }

        r = requests.get(
            url=f'{base_url}/account/{accountid}/phonenumbersubscription/',
            headers=request_header
        )
        if r.status_code == requests.codes.ok:
            return r.json()
        else:
            r.raise_for_status()
