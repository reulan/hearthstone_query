# hearthstone_query                                                                                                                                               
This is a simple web application that queries the Battle.net API and retrieves the following things:
Cards matching:
- Class: Druid OR Warlock
- Mana: At least 7
- Rarity: Legendary

Endpoints are reachable at (was pretty straightforward for me to Dockerize + host since my personal infra exists):
[hsq.reulan.com/](https://hsq.reulan.com/)

On page refresh, 10 cards will be selected matching the criteria above.

*Bonus:*
Display results sorted by card ID in a human readable table that includes:
- Card image
- Name
- Type
- Rarity
- Set
- Class

## Installation
```
pip3 install flask
pip3 install requests
pip3 install requests_oauthlib
```

## Configuration
### Secrets
To run locally env vars are used for secrets. When running live Kubernetes secrets are loaded into the application.
```
export HSQ_CLIENT_ID=""
export HSQ_CLIENT_SECRET=""
```

In Kubernetes secrets are read from a Kubernetes Secret resource.

For production, I am comfortable using Google Secret Manager or Vault.

### Flask
```
export FLASK_APP="app.py"
```

## Running
### Locally
```
flask run
```

### Docker
```
docker run :latest
```

## Deployment
This is deployed to my personal infrastucture using a Makefile (which uses Docker + Terraform under the hood).

- Build Docker image which sets up OS to serves web application on port 5000.
- Created kubernetes YAML specs for a Deployment and an Ingress to run the container and expose port 5000 (TLS Terminated)
- Convert YAML -> HCL via `k2tf`
- `terraform apply` to deploy to the k8s cluster.

## TODO
- Make this much more flexible (able to filter all attributes instead of just mana/class/rarity)
- Implement actual logging instead of print statements.

## Resources Used
[Hearthstone GameData API](https://develop.battle.net/documentation/hearthstone/game-data-apis)
[Flask Documentation](https://flask.palletsprojects.com/en/1.1.x/)
[Requests Documentation](https://requests.readthedocs.io/en/master/)
[Hearthstone Card List - Warlock Legendaries](https://playhearthstone.com/en-us/cards?class=warlock&rarity=legendary&set=wild)
