import boto3

client = boto3.resource('dynamodb', region_name='us-east-2')
tableName = 'Hone_Users'
table = client.Table(tableName)

#returns a game object from the Dynamo Database given a userid
#if there exists no game object, -1 is returned
def get_user_by_email(email):
    response = table.get_item(
        Key={
            'email': email
        }
    )

    #ERROR CHECK RESPONSE
    #check if anything was retrieved
    if 'Item' not in response:
        return -1
    else:
        #   dictionary of game object items
        userData = response['Item']
        return userData

#Input: (Game obj) game, (str) userId
#Output: returns the newly created game
def newUser(user):
    #error checking
    response = table.put_item(
        TableName=tableName,
        Item=user.toDict()
    )
    return user




