#!/usr/bin/python3
import os
import json

import flask
from flask import Flask

import hsq.api as hsqa
import hsq.dataparse as hsqd

app = Flask(__name__)

"""
Helper functions
"""
def client_setup():
    # Grab secrets
    cid = os.getenv('HSQ_CLIENT_ID')
    cs = os.getenv('HSQ_CLIENT_SECRET')

    # Create API Client and get Token
    hsq_client = hsqa.HearthstoneAPI(cid, cs)
    token_data = hsq_client.create_token()
    token_value = hsq_client.get_token_value(token_data)
    hsq_client.set_token_value(token_value)
    return hsq_client

def retrieve_card_data(hsq_client):
    """Get all Druid and Warlock legendaries over 7 mana."""
    # The HearthstoneAPI.get_cards function already specifically targets en_US localized cards as well as legendary cards
    # this definitely could be expanded so those values can be overridden, but for simplicitys sake it was
    # implemented as needed by this code challenge.
    warlock_data = hsq_client.get_cards(hsqd.get_class_params('warlock'))
    druid_data = hsq_client.get_cards(hsqd.get_class_params('druid'))

    # filter_by_mana function should require  only a card list, and it could be invoked once instead of merging 2 JSON data structs
    # especially if dynamic amount of Hearthstone classes were to be mentioned - this needs work to support a for class in classes
    combined_cards = hsqd.filter_by_mana(warlock_data, 7, "greater") + hsqd.filter_by_mana(druid_data, 7, "greater")
    return combined_cards

"""
Web Application
"""
# Instantiate and initialize Hearthstone API helper
hsq_client = client_setup()
card_list = retrieve_card_data(hsq_client)

# Get 10 random cards based of challenege critera and display them
@app.route('/')
def hearthstone_query():
    card_images = []
    random_cards = hsqd.get_random_cards(card_list)
    for card in random_cards:
        card_images.append(card["image"])
    #return card_names
    return flask.render_template('index.html', card_images=card_images)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
