
<p align="center">
  <img src="https://jixjiastorage.blob.core.windows.net/blog-resources/cosmos-sdk-for-python/title.jpg">
</p>

## Python SDK for Azure Cosmos DB
This utility is designed to streamline interactign with Azure Cosmos DB using Python. The repo contains following features:

1. Classes for supporting common CRUD operations
2. Sample driver program showcase how to use this SDK


## How-To

1. `git clone` this repo
2. Install dependencies executing `pip install -r requirements.txt`
3. Add your *Cosmos DB Endpoint* and *Primary Key* to `cosmosdb_credential.py` file
4. Run driver program `python program.py` to see this utility in action. It perform the followings:
    - create a new Cosmos database 
    - create a new entity and container 
    - add several several sample data into it
    - query the container using SQL API
    - delete designated items
