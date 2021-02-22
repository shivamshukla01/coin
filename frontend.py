import json
import boto3

def lambda_handler(event, context):
    # TODO implement
   res= [
   {
    "coinUID": 1,
    "coinName": "BTC",
    "imageURL": "http://url",
    "exchanges": []
    },
    {
    "coinUID": 2,
    "coinName": "ETH",
    "imageURL": "http://url",
    "exchanges": []
    },
    {
    "coinUID": 3,
    "coinName": "LTC",
    "imageURL": "http://url",
    "exchanges": []
    },
    {
    "coinUID": 4,
    "coinName": "DOGE",
    "imageURL": "http://url",
    "exchanges": []
    },
    {
    "coinUID": 5,
    "coinName": "TRX",
    "imageURL": "http://url",
    "exchanges": []
    },
    {
    "coinUID": 6,
    "coinName": "ADA",
    "imageURL": "http://url",
    "exchanges": []
    }]
   dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
   table = dynamodb.Table('coin')
   temp= table.scan()
   for i in temp['Items']:
        r = json.loads(i['data'])
        obj= {
        "exchangeUID": 0,
        "updateTimestamp": 1613838827,
        "exchangeName": "none",
        "coinbuyprice": 0.0,
        "coinsellprice": 0.0
        }
        obj["exchangeUID"]=r["exchangeUID"]
        obj["updateTimestamp"]=r["updateTimestamp"]
        obj["exchangeName"]=r["exchangeName"]
        for item in r["coins"]:
            index= item['coinUID']-1
            obj["coinbuyprice"]=item["coinbuyprice"]
            obj["coinsellprice"]=item["coinsellprice"]
            res[index]["exchanges"].append(obj)
   return {
        'statusCode': 200,
        'body': json.dumps(res)
    }
