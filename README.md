# Python SDK for Azure Cosmos DB

This repository contains the followings:

1. Object classess for performing common CRUD operations
2. A sample driver program that uses this SDK

# Installation

1. Clone this repo
2. Fetch azure-cosmosdb sdk 3.3.1 `pip install -r requirements.txt`
3. Add your Cosmos DB Endpoint and Primary Key to `cosmosdb_credential.py` file
4. Run the example driver program `python program.py`. 
  - This will create a new Cosmos DB entity and a container with several sample items
