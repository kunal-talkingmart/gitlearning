import json
#import time
import requests

API_KEY = '9d84aeee1dce84af2be7f3e4c22e62e7'
PASSWORD = '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'
SHOP_NAME = 'talkingmart'
API_VERSION = '2020-07' #change to the API version
shop_url = "https://%s:%s@%s.myshopify.com/admin/api/%s" % (API_KEY, PASSWORD, SHOP_NAME, API_VERSION)

order="""
mutation draftOrderCreate($input: DraftOrderInput!) {
  draftOrderCreate(input: $input) {
    draftOrder {
      id
    }
    userErrors {
      field
      message
    }
  }
}"""
orderInput = { "input": { "customerId": "gid://shopify/Customer/3878488998053", "lineItems": {"title": "myOrder", "quantity": 1, "originalUnitPrice": 10}, "email": "viveksingh@teleworm.us"}}

orderComplete = """
mutation draftOrderComplete($id: ID!) {
  draftOrderComplete(id: $id) {
    draftOrder {
      id
    }
    userErrors {
      field
      message
    }
  }
}"""
orderCompleteInput =  { "id": "gid://shopify/DraftOrder/648800403621"}



#var8 = { "input": { "customerId": "gid://shopify/Customer/3878488998053", "email": "viveksingh@teleworm.us"}}
#var8 = { "input": {"title": "My custom line item!", "email": "rahulsingh@teleworm.us"}}

response = requests.post(shop_url+'/graphql.json', json={'query': order, 'variables': orderInput})

print ("The response code is: %s",response.status_code)
if response.status_code==400:
        raise ValueError('GraphQL error:' + response.text)
answer = json.loads(response.text)
print (answer)
print(response)

#complete the order- WIP

#response = requests.post(shop_url+'/graphql.json', json={'query': orderComplete, 'variables': orderCompleteInput})

#print ("The response code is: %s",response.status_code)
#if response.st atus_code==400:
#        raise ValueError('GraphQL error:' + response.text)
#answer = json.loads(response.text)
#print (answer)
#print(response)
