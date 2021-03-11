#!/usr/bin/python3
import json
import os
import requests
import sys

from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

class HearthstoneAPI():
    """Hearthstone API class"""

    def __init__(self, client_id, client_secret):
        """Querying the Hearthstone GameData API"""
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = None # if sending access_token param
        self.token_header = None # if sending Auth Bearer header
        self.region = "us"
        self.token_url = "https://{reg}.battle.net/oauth/token".format(reg=self.region)
        self.api_url = "https://{reg}.api.blizzard.com".format(reg=self.region)
        self.game = "hearthstone"

    def _url(self, endpoint):
        """Returns an URL endpoint"""
        api_url = ('{api}/{g}/{ep}').format(api=self.api_url, reg=self.region, g=self.game, ep=endpoint)
        return api_url

    def _parameters(self, parameters):
        """Returns a dictionary of parameters."""
        if 'region' not in parameters.keys():
            parameters[':region'] = self.region
        return parameters

    '''
    Authentication
    '''
    def create_token(self):
        client = BackendApplicationClient(client_id=self.client_id)
        oauth = OAuth2Session(client=client)
        token_data = oauth.fetch_token(token_url=self.token_url,
                                    client_id=self.client_id,
                                    client_secret=self.client_secret)
        return token_data

    # If token needs to be accessed directly.
    def get_token_value(self, token):
        token = dict(token)
        return token['access_token']

    def set_token_value(self, token_value):
        self.access_token = token_value
        formatted_header = {"Authorization": "Bearer {token}".format(token=token_value)}
        self.token_header = formatted_header

    '''
    GameData API
    '''
    def get_endpoint_data(self, endpoint, params):
        """Boilerplate to handle various types of endpoints"""
        _url = self._url(endpoint)
        _headers = self.token_header
        _params = self._parameters(params)

        if self.token_header == None:
            print("Please authenticate HearthstoneAPI class before invoking API calls.")
            sys.exit(1)

        #print("Querying: {url}\nHeaders: {headers}\nParams: {params}".format(url=_url, headers=_headers, params=_params))

        response = requests.get(_url, headers=_headers, params=_params)
        json_data = response.json()
        return json_data

    def get_cards(self, params):
        """Get Hearthstone cards!!!"""
        endpoint = 'cards'
        return self.get_endpoint_data(endpoint, params)
