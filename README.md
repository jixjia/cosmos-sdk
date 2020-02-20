<p align="center">
  <img src="https://jixjiastorage.blob.core.windows.net/blog-resources/cosmos-sdk-for-python/title.jpg">
</p>

## Python SDK for Azure Cosmos DB

This utility is designed to streamline interactign with Azure Cosmos DB using Python. The repo contains following features:

1. Classes for supporting common CRUD operations
2. Sample driver program showcase how to use this SDK

## How-To

1. Provision an Azure Cosmos DB service from [Azure Portal](portal.azure.com)
2. Clone this repo `git clone https://github.com/jixjia/cosmos-sdk.git`
3. Install dependencies with `pip install -r requirements.txt`
4. Add your **Cosmos DB Endpoint** and **Primary Key** to `cosmosdb_credential.py` file under section:

```python
# Cosmos DB config
cosmosdb_config = {
    'ENDPOINT': '<YOUR_COSMOS_ENDPOINT>',
    'PRIMARYKEY': '<YOUR_PRIMARY_KEY>'
}
```

5. Run driver program `python program.py` for a demo of this utility. It will perform followings:
   - Create a new Cosmos database
   - Create a new database collection (also known as container)
   - Add sample data into it
   - Query items using SQL-like syntax (SQL API)
   - Delete selected items

:warning: You will need to have Azure Cosmos DB provisioned in order to run this DEMO program
