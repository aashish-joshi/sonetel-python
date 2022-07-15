########################################################
#   ______                                     _
#  / _____)                        _          | |
# ( (____    ___   ____   _____  _| |_  _____ | |
#  \____ \  / _ \ |  _ \ | ___ |(_   _)| ___ || |
#  _____) )| |_| || | | || ____|  | |_ | ____|| |
# (______/  \___/ |_| |_||_____)   \__)|_____) \_)
########################################################
"""
Sonetel API Wrapper
===================

This is a simple Python wrapper for using Sonetel's public APIs with Python.

Authentication
    >>> from sonetel import api
    >>> s = api.Account(username="foo@example.com",password="not_a_real_password")
    >>> print(s.account_id())
"""

from . import api
