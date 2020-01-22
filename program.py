from cosmosdb_sdk import CosmosDB
import uuid
import datetime
import random


def generateData():
    sampleList = ['Big Data Platform', 'IoT Analytics',
                  'Predictive Modelling', 'BI and Datawarehouse', 'Computer Vision', 'NLP']

    partitionKey = random.choice(sampleList)

    return {
        'id': str(uuid.uuid4()),
        'partitionKey': partitionKey,
        'project': 'Project Cosmos SDK',
        'author': 'Jixin Jia',
        'description': 'Python SDK for interacting with Cosmos',
        'version': '1.0',
        'license': 'MIT',
        'date': datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    }


if __name__ == "__main__":

    # (0) Instantiate database & container connection
    cosmosDBName = 'Cosmos_DB'
    containerName = 'Cosmos_Container'
    dbConnection = CosmosDB(cosmosDBName, containerName)
    print('[INFO] Created new Cosmos DB entity {} : {}'.format(
        cosmosDBName, containerName))

    # (1) Insert sample data into the designated container
    dbConnection.create_item(generateData())
    dbConnection.create_item(generateData())
    dbConnection.create_item(generateData())

    # (2) List all existing items in a container
    itemList = dbConnection.list_items()

    print('[INFO] Listing all existing items')
    for item in itemList:
        print(item)

    # (3) Update an existing item using Custom Query (EXAMPLE: update 'version' from '1.0' to '2.0')
    query = 'SELECT * FROM c WHERE c.author = "Jixin Jia"'
    results = dbConnection.query_item(query)

    print('[INFO] Updating data')
    for item in results:
        newData = {
            'id': item['id'],
            'partitionKey': item['partitionKey'],
            'project': item['project'],
            'author': item['author'],
            'description': item['description'],
            'version': '2.0',
            'license': item['license'],
            'date': datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        }
        dbConnection.upsert_item(newData)

    # (4) Delete an existing item with document id
    # document_id = generateData()['id']
    # results = dbConnection.delete_item(document_id)
    # print(results)
