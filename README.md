# Managing Contracts - Flask Lab

## Overview

A Flask application that manages contract and customer information while protecting sensitive customer data.

## Features

- Retrieve contract information.
- Check whether a customer exists without exposing personal information.
- Return appropriate HTTP response codes.

## API Routes

| Method | Endpoint | Success | Failure |
|---|---|---|---|
| GET | /contract/<id> | 200 with contract information | 404 |
| GET | /customer/<customer_name> | 204 with empty body | 404 |

## Example Responses

### Contract found

GET /contract/1

Returns: This contract is for John and building a shed

### Customer found

GET /customer/bob

Returns 204 No Content with an empty response body.

## Installation

Run: pipenv install

## Run the Application

Run: pipenv run python server/app.py

The application runs on port 5555.

## Run Tests

Run: pipenv run pytest -v

## Technologies

- Python 3.8
- Flask
- Pytest

## Author

Abdulsalam
