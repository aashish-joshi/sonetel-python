<br />
<div align="center">
  <a href="https://github.com/aashish-joshi/sonetel-python">
    <img src="https://dl.dropboxusercontent.com/s/hn4o0v378od1aoo/logo_white_background.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Sonetel API Python Wrapper</h3>

<p align="center">
    A simple Python wrapper for using Sonetel's REST API endpoints.
    <br />
    <br />
    <a href="https://sonetel.com/en/developer/">Sonetel Developer Home</a>
    .
    <a href="https://sonetel.com/en/developer/api-documentation/">API Documentation</a>
    .
    <a href="https://app.sonetel.com/register?tag=api-developer&simple=true">Get Free Account</a>
  </p>
</div>

## Getting Started

To use Sonetel's APIs you first need to sign up for a free account. Get a free account from <a href="https://app.sonetel.com/register?tag=api-developer&simple=true">sonetel.com</a>.

### Installation

Use PIP to install the package.

`pip install sonetel`

## Functions

The following functions are support at the moment. More will be added in the future.

- `account_balance()` - Get the prepaid balance of the account (e.g. '10'). Pass the argument `currency=True` to get the balance with the currency appended (e.g. '10 USD')
- `account_id()` - Returns your Sonetel account ID.
- `account_info()` - Fetch information about your account such as company name, balance, country, timezone, daily limit and so on.
- `account_users()` - Details of all the users in your account.
- `callback()` - Use our Callback API to make a callback call.
- `create_token()` - Create a new access token. A new access token is automatically created when you call the Account resource the first time.
- `get_token()` - Get the access token being used.
- `get_username()` - Returns the email address of the user that was used to create the token.
- `subscription_buynum()` - Purchase a phone number. Requires a phone number to be passed. Use the `/availablephonenumber` API endpoint to see a list of phone numbers available for purchase from a country and area.
- `subscription_listnums()` - See the details of all the phone numbers purchased by you. Pass the parameter `e164only=True` to only get a list of E.164 numbers without any metadata.

## Examples

### 1. Create an access token

```python
import os
from sonetel import api

user = os.environ.get('sonetelUserName')
pswd = os.environ.get('sonetelPassword')

s = api.Account(username=user,password=pswd)

print(s.get_token())
```

### 2. Print your Sonetel account ID and the current prepaid balance. 

```python
import os
from sonetel import api

user = os.environ.get('sonetelUserName')
pswd = os.environ.get('sonetelPassword')

s = api.Account(username=user,password=pswd)

print(f"Your account ID is {s.account_id()} and your prepaid balance is {s.account_balance()}.")
```

### 3. List the phone numbers available in your account

```python
import os
from sonetel import api

user = os.environ.get('sonetelUserName')
pswd = os.environ.get('sonetelPassword')

s = api.Account(username=user,password=pswd)

print(s.subscription_listnums(e164only=True))
```

### 4. Make a callback call

When making a callback call, `num1` is the destination where you will first answer the call before we call `num2`. This can be your mobile number, a SIP address or your Sonetel email address. 

If you set `num1` as your Sonetel email address, then the call will be handled as per your incoming call settings.

```python
import os
from sonetel import api

user = os.environ.get('sonetelUserName')
pswd = os.environ.get('sonetelPassword')

s = api.Account(username=user,password=pswd)

result = s.callback(
    num1="YOUR_NUMBER_OR_ADDRESS",
    num2="NUMBER_TO_CALL",
)
print(result)
```

## Storing your credentials

Please your credentials safe in order to avoid any misuse of your account. For this reason, it isn't recommend to hard code them into scripts.

You can add them to your operating system's environment variables and use Python's `os` module to fetch them.

Assuming the username and password are stored in environment variables named `sonetelUserName` and `sonetelPassword` respectively, here's how you can access them from a script:

```python
import os
from sonetel import api

user = os.environ.get('sonetelUserName')
pswd = os.environ.get('sonetelPassword')

s = api.Account(username=user,password=pswd)

print(s.account_id())
```

## Help

Have a look at the <a href="https://docs.sonetel.com">API documentation</a>.