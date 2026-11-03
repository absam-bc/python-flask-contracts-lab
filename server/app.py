#!/usr/bin/env python3

from flask import Flask, abort

app = Flask(__name__)

# Available contract information
contracts = [
    {
        "id": 1,
        "contract_information": "This contract is for John and building a shed"
    },
    {
        "id": 2,
        "contract_information": "This contract is for a deck for a buisiness"
    },
    {
        "id": 3,
        "contract_information": "This contract is to confirm ownership of this car"
    }
]

# Registered customers
customers = ["bob", "bill", "john", "sarah"]


# Return contract information if the contract exists
@app.route('/contract/<int:id>')
def contract_info(id):
    for contract in contracts:
        if contract["id"] == id:
            return contract["contract_information"], 200

    abort(404)


# Confirm customer existence without exposing sensitive information
@app.route('/customer/<customer_name>')
def customer_info(customer_name):
    if customer_name in customers:
        return "", 204

    abort(404)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
