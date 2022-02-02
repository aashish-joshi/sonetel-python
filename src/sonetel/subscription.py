from json import dumps
import requests

# Create a phone number subscription
def buy_number(token: str, accountid: str, number: str, base_url: str = 'https://public-api.sonetel.com') -> dict:
    """
    Buy a phone number that is available.
    Numbers that are available for purchase can be checked from the /availablephonenumber API endpoint.
    More information is available at https://docs.sonetel.com/docs/sonetel-documentation/YXBpOjE2MjQ3MzI4-phone-numbers

    :param token: API access token generated using the account.token() function.
    :param base_url: The API base URL.
    :param accountid: Your Sonetel account ID.
    :param number: the phone number to add to your account.
    :return: Dict containing the response in case of success.
    """

    # Prepare the request body
    body = {
        "phnum": number
    }

    # Prepare the request Header
    request_header = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json"
    }

    # Send the request
    r = requests.post(
        url=f'{base_url}/account/{accountid}/phonenumbersubscription/',
        data=dumps(body),
        headers=request_header
    )

    # Check the response and handle accordingly
    if r.status_code == requests.codes.ok:
        response = r.json()
        return response['response']
    else:
        r.raise_for_status()

# List existing phone number subscriptions.
def list_all_numbers(token: str, accountid: str, base_url: str = 'https://public-api.sonetel.com') -> list:
    """
    List all the phone numbers present in the account.
    More information is available at https://docs.sonetel.com/docs/sonetel-documentation/YXBpOjE2MjQ3MzI4-phone-numbers

    :param token: API access token generated using the account.token() function.
    :param base_url: The API base URL.
    :param accountid: Your Sonetel account ID.
    :return: Returns a list containing the information about the numbers assigned to you.
    """

    # Prepare the request Header
    request_header = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json"
    }

    # Send the request
    r = requests.get(
        url=f'{base_url}/account/{accountid}/phonenumbersubscription/',
        headers=request_header
    )

    # Check the response and handle accordingly
    if r.status_code == requests.codes.ok:
        response = r.json()
        if response['response'] == 'No entries found':
            return ['No entries found']
        else:
            return response['response']
    else:
        r.raise_for_status()
