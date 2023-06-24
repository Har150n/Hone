import boto3
import json

client = boto3.client('dynamodb', region_name='us-east-2')
tableName = 'Hone_Game_States'

#returns a game object from the Dynamo Database given a userid
#if there exists no game object, -1 is returned
def retrieveGame(userId):
    response = client.get_item(
        TableName=tableName,
        Key={
            'userId': {'N': userId}
        }
    )

    #ERROR CHECK RESPONSE
    #check if anything was retrieved
    if 'Item' not in response:
        return -1
    else:
        #return deserialized game object
        pass

#inserts a new Game State item into the db
def newGame(game, userId):
    print('new game created')
    pass



