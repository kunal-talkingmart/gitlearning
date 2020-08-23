import json
#import time
import requests

API_KEY = '9d84aeee1dce84af2be7f3e4c22e62e7'
PASSWORD = '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'
SHOP_NAME = 'talkingmart'
API_VERSION = '2020-07' #change to the API version
shop_url = "https://%s:%s@%s.myshopify.com/admin/api/%s" % (API_KEY, PASSWORD, SHOP_NAME, API_VERSION)

product = """{

products(first: 5, query:"tag:$Lenovo") {
    edges {
      node {
        handle
        id
        description
        tags
      }
    }
  }
} 
  
"""


response = requests.post(shop_url+'/graphql.json', json={'query': product})

#print ("The response code is: %s",response.status_code)
if response.status_code==400:
        raise ValueError('GraphQL error:' + response.text)
answer = json.loads(response.text)
print (answer)
print(response)