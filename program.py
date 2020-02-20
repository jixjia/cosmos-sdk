'''
Author:         Jixin Jia (Gin)
Date:           20-Jan-2020
Version:        1.0

This utility is designed to streamline interactign with Azure Cosmos DB using Python. 
It contains following features:

(1) Classes for supporting common CRUD operations
(2) Sample driver program showcasing how to use this SDK
'''

from cosmosdb_sdk import CosmosDB
import uuid
import json
import datetime
import random
import colorama
from colorama import Style, Fore

colorama.init()
print(colorama.ansi.clear_screen())  # Clear terminal outputs


def generateData():
    category_list = ['Big Data Analytics', 'IoT Edge',
                     'Predictive Modelling', 'BI and Data Visualization',
                     'Image Processing (CV)', 'NLP', 'Deep Learning']

    category = random.choice(category_list)

    return {
        'id': str(uuid.uuid4()),
        'partitionKey': category,
        'project': 'Project Cosmos SDK',
        'author': 'Jixin Jia',
        'description': 'Python SDK for Azure Cosmos DB',
        'version': '1.0',
        'license': 'MIT',
        'view_count': random.randint(1, 30),
        'timestamp': datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    }


if __name__ == "__main__":

    # DEMO

    # (1) Instantiate database & container connection
    cosmosDBName = 'Demo_DB'
    containerName = 'Demo_Container'
    print(Fore.CYAN + '[INFO] Instantiating the Cosmos DB entity {} : {}'.format(
        cosmosDBName, containerName) + Style.RESET_ALL)

    dbConnection = CosmosDB(cosmosDBName, containerName)

    # (2) Insert sample data into the Database container
    print(Fore.CYAN +
          '[INFO] Adding some sample data into Cosmos DB container' + Style.RESET_ALL)

    for i in range(15):
        dbConnection.create_item(generateData())

    # (3) List all existing items in a container
    print(Fore.CYAN + '[INFO] Listing all existing items' + Style.RESET_ALL)

    itemList = dbConnection.list_items()
    for item in itemList:
        print(json.dumps(item, indent=2, sort_keys=True))

    # (4) Update selected item's property using custom query
    # For example, select items who's category is 'Deep Learning' and
    # update their version to '2.0'
    print(Fore.CYAN + '[INFO] Updating selected items' + Style.RESET_ALL)

    query = 'SELECT * FROM c WHERE c.partitionKey = "Deep Learning" and c.view_count > 20'
    results = dbConnection.query_item(query)

    for item in results:
        newData = {
            'id': item['id'],
            'partitionKey': item['partitionKey'],
            'project': item['project'],
            'author': item['author'],
            'description': item['description'],
            'version': '2.0',
            'license': item['license'],
            'view_count': item['view_count'],
            'timestamp': datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        }
        dbConnection.upsert_item(newData)

    # (5) Delete selected items
    # For example, remove items who's view count is less than 10
    print(Fore.CYAN + '[INFO] Deleting selected items' + Style.RESET_ALL)

    query = 'SELECT * FROM c WHERE c.view_count < 10'
    results = dbConnection.query_item(query)

    for item in results:
        document_id = item['id']
        output = dbConnection.delete_item(document_id)
