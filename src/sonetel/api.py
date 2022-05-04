import requests
import re
from json import dumps

class Resource:
    """
    Use Sonetel's Python module to manage your account.

    **API Documentation**: https://docs.sonetel.com/

    """
    __e164pattern = r'^\+?[1-9]\d{8,15}$'

    def __init__(self, username: str, password: str, auth_url='https://api.sonetel.com/SonetelAuth/beta/oauth/token',
                 base_url='https://public-api.sonetel.com'):
        self.__username = username
        self.__password = password

        # API URLs
        self.auth_url = auth_url
        self.base_url = base_url

        # Set the API access token
        token = self.get_token()
        self.token = token["access_token"]

        # Account and User Information
        self.accountid = self.account_info(return_only_accountid=True)
        self.userid = 'userid'

    def get_token(self, refresh: str = "no", grant_type: str = "password", refresh_token: str = None) -> dict:
        """
        Create an API access token from the user's Sonetel email address and password.
        Optionally, generate a refresh token as well. Set the ``grant_type`` to ``refresh_token`` to refresh an
        existing access token.
        **Docs**: https://docs.sonetel.com/docs/sonetel-documentation/YXBpOjExMzI3NDM3-authentication

        :param refresh: Optional. Flag to control whether a refresh token is included in the response. Defaults to 'no'
        :param grant_type: Optional. The OAuth2 grant type. Defaults to 'password'
        :param refresh_token: Optional. Pass the `refresh_token` in this field to generate a new access_token.

        :return: Returns the access token.
        """

        if grant_type == 'refresh_token' and refresh_token is None:
            raise ValueError("A refresh_token is needed when grant type is refresh_token.")

        # Prepare the request body.
        body = f"grant_type={grant_type}&username={self.__username}&password={self.__password}&refresh={refresh}"

        # Add the refresh token to the request body if passed to the function
        if refresh_token is not None:
            body += f"&refresh_token={refresh_token}"

        auth = ('sonetel-web', 'sonetel-web')

        # Prepare the request headers
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        # Send the request
        r = requests.post(
            url=self.auth_url,
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

    def account_info(self, return_only_accountid: bool = False):

        """
        Get information about Sonetel account such as the account ID, prepaid balance, currency, country, etc.
        **Docs**: https://docs.sonetel.com/docs/sonetel-documentation/b3A6MTUyNTkwNTM-get-your-account-information

        :param return_only_accountid: Optional. Returns only the account ID string if set to true. Else, returns the complete JSON response.
        :return: A dict with the the Sonetel account details.
        """

        # Prepare the request Header
        header = {
            "Authorization": "Bearer " + self.token,
            "Content-Type": "application/json"
        }

        # Send the request
        r = requests.get(
            url=f"{self.base_url}/account/",
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

    def account_balance(self, currency: bool = False) -> str:
        """
        Get the prepaid account balance. Example, '3.74 USD' or '3.74'.
        **Docs**: https://docs.sonetel.com/docs/sonetel-documentation/b3A6MTUyNTkwNTM-get-your-account-information

        :param currency: Optional. Flag to specify if the currency should be returned or not. Defaults to False
        :return: The current prepaid balance.
        """

        # Prepare the request Header
        header = {
            "Authorization": "Bearer " + self.token,
            "Content-Type": "application/json"
        }

        # Send the request
        r = requests.get(
            url=f"{self.base_url}/account/",
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
    def account_users(self) -> list:
        """
        Get a list of all the users in the Sonetel account along with their settings such as title, email, password status, etc.
        **Docs**: https://docs.sonetel.com/docs/sonetel-documentation/b3A6MTY4MzEyMDQ-list-all-users

        :return: Returns a list containing the user information
        """

        # Prepare the request Header
        request_header = {
            "Authorization": "Bearer " + self.token
        }

        # Send the request
        r = requests.get(
            url=f'{self.base_url}/account/{self.accountid}/user/',
            headers=request_header
        )
        # Check the response and handle accordingly
        if r.status_code == requests.codes.ok:
            response = r.json()
            return response['response']
        else:
            print(r.json())
            r.raise_for_status()

    def callback(self, num1: str, num2: str, cli1: str = 'automatic', cli2: str = 'automatic'):
        """
        Use Sonetel's CallBack API to make business quality international calls at the cost of 2 local calls.

        **Docs**: https://docs.sonetel.com/docs/sonetel-documentation/YXBpOjE1OTMzOTIy-make-calls

        **Number Format:**\n
        It is recommended that both the phone numbers (num1 and num2) be entered in the international E164 format with a
        leading +. For example, if you want to call a US number (212) 555-1234, it should be set as `'+12125551234'`.

        **Caller ID:**\n
        It is best to use 'automatic' CLI as our system selects the best possible phone to be shown from the numbers
        available in your account. If you don't have a Sonetel number, then your verified mobile number is used as CLI.

        :param num1: Required. The first phone number that will be called. This should be your phone number.
        :param num2: Required.The phone number that you wish to speak to.
        :param cli1: Optional. The caller ID shown to the first person.
        :param cli2: Optional. The caller ID shown to the second person.

        :return: Return the status code and message as a dict.
        """

        # Check if num1 and num2 are in the +NUMBER E164 format.
        if re.search(self.__e164pattern, num1) and re.search(self.__e164pattern, num1):
            # ToDo:
            #  Check cost of call before connecting
            #  Check if the CLI provided, if other than automatic, is a valid e164 number.

            # Initiate the callback
            request_header = {
                'Authorization': 'Bearer ' + self.token,
                'Content-Type': 'application/json;charset=UTF-8'
            }

            body = {
                "app_id": 'PySonApp-' + self.accountid,
                "call1": num1,
                "call2": num2,
                "show_1": cli1,
                "show_2": cli2
            }

            # Send the request
            r = requests.post(
                url=f'{self.base_url}/make-calls/call/call-back',
                data=dumps(body),
                headers=request_header
            )

            # Check the response and handle accordingly
            if r.status_code == requests.codes.ok:
                response = r.json()
                return response['response']
            else:
                print(r.json())
                r.raise_for_status()
        else:
            raise ValueError('num1 & num2 are mandatory and should be in the international +NUMBER format.')

    # Create a phone number subscription
    def subscription_buynum(self, number: str) -> dict:
        """
        Buy a phone number that is available. Numbers that are available for purchase can be checked from the ``/availablephonenumber`` API endpoint.

        **DOCS**: https://docs.sonetel.com/docs/sonetel-documentation/YXBpOjE2MjQ3MzI4-phone-numbers

        :param number: the phone number to add to your account.
        :return: Dict containing the response in case of success.
        """

        # Prepare the request body
        body = {
            "phnum": number
        }

        # Prepare the request Header
        request_header = {
            "Authorization": "Bearer " + self.token,
            "Content-Type": "application/json"
        }

        # Send the request
        r = requests.post(
            url=f'{self.base_url}/account/{self.accountid}/phonenumbersubscription/',
            data=dumps(body),
            headers=request_header
        )

        # Check the response and handle accordingly
        if r.status_code == requests.codes.ok:
            response = r.json()
            return response['response']
        else:
            r.raise_for_status()

    def subscription_listnums(self, **kwargs) -> list:
        """
        List all the phone numbers present in the account.

        - ``e164only``. Boolean. Only return a list of phone numbers is set to true

        **DOCS**: https://docs.sonetel.com/docs/sonetel-documentation/YXBpOjE2MjQ3MzI4-phone-numbers


        :return: Returns a list containing the information about the numbers assigned to you.
        """

        # Prepare the request Header
        request_header = {
            "Authorization": "Bearer " + self.token,
            "Content-Type": "application/json"
        }

        # Send the request
        r = requests.get(
            url=f'{self.base_url}/account/{self.accountid}/phonenumbersubscription/',
            headers=request_header
        )

        # Check the response and handle accordingly
        if r.status_code == requests.codes.ok:
            response = r.json()
            if response['response'] == 'No entries found':
                return ['No entries found']
            else:
                if 'e164only' in kwargs:
                    # Return only the E164 numbers if e164only = True
                    if kwargs['e164only']:
                        nums = []
                        for entry in response['response']:
                            nums.append(entry['phnum'])
                        return nums
                else:
                    return response['response']
        else:
            r.raise_for_status()

