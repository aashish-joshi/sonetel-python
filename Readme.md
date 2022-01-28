<br />
<div align="center">
  <a href="https://github.com/aashish-joshi/sonetel-python">
    <img src="https://dl.dropboxusercontent.com/s/hn4o0v378od1aoo/logo_white_background.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Sonetel API</h3>

<p align="center">
    Python package to provide easy access to different Sonetel API endpoints.
    <br />
    <br />
    <a href="https://sonetel.com/en/developer/" target="_blank">Sonetel Developer Home</a>
    .
    <a href="https://sonetel.com/en/developer/api-documentation/" target="_blank">API Documentation</a>
  </p>
</div>

## Getting Started

### Get a Sonetel account

You need an account with Sonetel to use this Python package. Sign up for a free account from <a href="https://app.sonetel.com/register?tag=api-developer&simple=true">sonetel.com</a>.

### How to install?

`pip install sonetel`

### How to use?

Here's a simple example of a script that prints the account ID and current prepaid balance of the user's account.

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

### How to get more information?

Have a look at our <a href="https://docs.sonetel.com">API documentation</a>. Please contact us at dev.support@sonetel.com if you have questions about our API.