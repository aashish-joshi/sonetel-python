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

## Usage

### Functions

Here's a list of functions available in different packages.

#### Account

- `account.token()` - Get an access token to authenticate API requests. Can be used to refresh an existing access token as well.
- `account.get_account()` - Get information about your Sonetel account such as the account ID, prepaid balance, etc
- `account.get_balance()` - Get your Sonetel prepaid balance.
- `account.get_all_users` - Get a list of all users in your Sonetel account.

#### Subscription
- `subscription.buy_number()` - Buy a phone number
- `subscription.list_all_numbers()` - List all phone numbers currently assigned to your account.

### Examples

1. Print your Sonetel account ID and the current prepaid balance.
```python
from sonetel import account

# get API access token
token = account.token(
    username = "YOUR_SONETEL_USERNAME",
    password = "YOUR_SONETEL_PASSWORD")

# Print the Sonetel account ID and current account balance.
account_id = account.get_account(
    token=token["access_token"],
    return_only_accountid=True)

balance = account.get_balance(
    token=token["access_token"], 
    currency=True)

print(f"Your account ID is {account_id} and your prepaid balance is {balance}.")
```

2. List the phone numbers available in your account
```python
from sonetel import account, subscription

# get API access token
token = account.token(
    username = "YOUR_SONETEL_USERNAME",
    password = "YOUR_SONETEL_PASSWORD")

# Get Sonetel account ID
account_id = account.get_account(
    token=token["access_token"],
    return_only_accountid=True)

# Get the list of phone numbers
numList = subscription.list_all_numbers(
    token=token["access_token"],
    accountid=account_id)

print(f"Phone number list for account {account_id}:\n")

for entry in numList:
    print(entry["phnum"])
```

### Storing your credentials

**IMPORTANT** It is critical that you keep your Sonetel login credentials safe in order to avoid any misuse of your account.

For this reason, we don't recommend hard coding them into scripts. You can add them to your operating system's environment variables and use Python's OS module to fetch the details.

Assuming the username and password are stored in environment variables named `sonetelUserName` and `sonetelPassword` respectively, here's how you can access them from a script:

```python
import os
from sonetel import account

user = os.environ.get('sonetelUserName')
pswd = os.environ.get('sonetelPassword')

token = account.token(
    username = user,
    password=pswd)
```

## Help

Have a look at our <a href="https://docs.sonetel.com">API documentation</a>. Please contact us at <a href="mailto:dev.support@sonetel.com">dev.support@sonetel.com</a> if you have questions.