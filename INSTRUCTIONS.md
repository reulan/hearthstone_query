# Blizzard Challenges
1. Software Engineering (pick whatever language you are most comfortable in) 
    a. Utilize Blizzard Hearthstone API (See: Getting started and API guides) to retrieve card data
        i. For the purposes of this exercise, a proper secret management mechanism is not required. Use of an industry standard solution (Vault, Parameter Store, etc.) can be implied in your documentation.
        ii. This does not need to be a running service hosted somewhere. We will review your submission and discuss your strategies.

    b. Create web application to render requested information from the API into a human readable page
        i. Retrieve details of any 10 cards with the following criteria
            1. Class: Druid OR Warlock
            2. Mana: At least 7
            3. Rarity: Legendary
