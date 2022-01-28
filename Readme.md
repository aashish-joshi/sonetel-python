<br />
<div align="center">
  <a href="https://github.com/aashish-joshi/sonetel-python">
    <img src="https://dl.dropboxusercontent.com/s/hn4o0v378od1aoo/logo_white_background.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Sonetel API</h3>

<p align="center">
    A simple wrapper for using Sonetel's REST API endpoints.
    <br />
    <br />
    <a href="https://sonetel.com/en/developer/" target="_blank">Sonetel Developer Home</a>
    .
    <a href="https://sonetel.com/en/developer/api-documentation/" target="_blank">API Documentation</a>
  </p>
</div>

## Getting Started

### Get a Sonetel account

Sign up for a free account from <a href="https://app.sonetel.com/register?tag=api-developer&simple=true">sonetel.com</a>.

### Installation

`pip install sonetel`

## Usage

### Functions

Here's a list of functions available in different packages.

#### Account
- `account.get_token()` - Get an access token to authenticate API requests. 
- `account.get_accountid()` - Get your Sonetel account ID
- `account.get_balance()` - Get your Sonetel prepaid balance

#### Subscription
- `subscription.buy_number()` - Buy a phone number
- `subscription.list_all_numbers()` - List all phone numbers currently assigned to your account.

### Examples

1. Print your Sonetel account ID and the current prepaid balance.
```python
from sonetel import account

api_base_url = 'https://public-api.sonetel.com'

# get API access token
access_token = account.get_token(
    username = "YOUR_SONETEL_USERNAME",
    password='YOUR_SONETEL_PASSWORD',
    auth_url='https://api.sonetel.com/SonetelAuth/beta/oauth/token')

# Print the Sonetel account ID and current account balance.
account_id = account.get_accountid(
    token=access_token,
    base_url=api_base_url)

balance = account.get_balance(
    token=access_token, 
    currency=True,
    base_url = api_base_url)

print(f"Your account ID is {account_id} and your prepaid balance is {balance}.")
```

2. List the phone numbers available in your account
```python
from sonetel import account, subscription

api_base_url = "https://public-api.sonetel.com"

# get API access token
access_token = account.get_token(
    username = 'YOUR_SONETEL_USERNAME',
    password='YOUR_SONETEL_PASSWORD',
    auth_url='https://api.sonetel.com/SonetelAuth/beta/oauth/token')

# Get Sonetel account ID
account_id = account.get_accountid(
    token=access_token,
    base_url=api_base_url)

# Get the list of phone numbers
numList = subscription.list_all_numbers(
    token=access_token,
    base_url=api_base_url,
    accountid=account_id
)

print(f"Phone number list for account {account_id}:\n")

for entry in numList["response"]:
    print(entry['phnum'])
```

## Help

Have a look at our <a href="https://docs.sonetel.com">API documentation</a>. Please contact us at <a href="mailto:dev.support@sonetel.com">dev.support@sonetel.com</a> if you have questions.