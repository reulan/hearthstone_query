#!/usr/bin/python3
"""
dataparse.py

b. Create web application to render requested information from the API into a human readable page
    i. Retrieve details of any 10 cards with the following criteria
        1. Class: Druid OR Warlock
        2. Mana: At least 7
        3. Rarity: Legendary
"""

import json
import random

def get_class_params(class_name):
    """Get all legendary cards for specified class."""

    class_params = {
        "locale": "en_US",
        "set": "",
        "class": class_name,
        "manaCost": "",
        "attack": "",
        "health": "",
        "collectible": "",
        "rarity": "legendary",
        "type": "",
        "minionType": "",
        "keyword": "",
        "gameMode": "",
    }
    #print(json.dumps(class_params, indent=4))
    return class_params

def filter_by_mana(card_data, search_mana_cost, operator):
    """Get all cards inclusive based of mana cost."""
    filtered_cards = []

    for card in card_data['cards']:
        card_mana_cost = card['manaCost']
        if operator == "greater":
            if card_mana_cost >= search_mana_cost:
                filtered_cards.append(card)
                print("[greater] Added card {0} with manaCost {1}.".format(card["name"], card["manaCost"]))
        elif operator == "lesser":
            if card_mana_cost <= search_mana_cost:
                filtered_cards.append(card)
                print("[lesser] Added card {0} with manaCost {1}.".format(card["name"], card["manaCost"]))
    return filtered_cards

def get_random_cards(cards, amount=10):
    """Will return x random cards based off the amount specified."""
    if len(cards) < amount:
        print("There are not enough cards to display {a} cards. Displaying {l} cards instead.".format(a=amount, l=len(cards)))
        return cards
    else:
        print("Selecting {a} cards from card list of {l}.".format(a=amount, l=len(cards)))
        return random.sample(cards, amount)
