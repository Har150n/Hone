import boto3, json, jsonpickle as jp

client = boto3.resource('dynamodb', region_name='us-east-2')
tableName = 'Hone_Game_States'
table = client.Table(tableName)

#returns a game object from the Dynamo Database given a userid
#if there exists no game object, -1 is returned
def retrieveGame(userId):
    response = table.get_item(
        Key={
            'userId': userId
        }
    )

    #ERROR CHECK RESPONSE
    #check if anything was retrieved
    if 'Item' not in response:
        return -1
    else:
        #   dictionary of game object items
        gameData = response['Item']
        return gameData

#Input: (Game obj) game, (str) userId
#Output: returns the newly created game
def newGame(game):
    #error checking
    response = table.put_item(
        TableName=tableName,
        Item=game.toDict()
    )
    print(response)
    return game
    pass



