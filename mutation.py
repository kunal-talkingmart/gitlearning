import json
#import time
import requests

API_KEY = '9d84aeee1dce84af2be7f3e4c22e62e7'
PASSWORD = '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'
SHOP_NAME = 'talkingmart'
API_VERSION = '2020-07' #change to the API version
shop_url = "https://%s:%s@%s.myshopify.com/admin/api/%s" % (API_KEY, PASSWORD, SHOP_NAME, API_VERSION)


cc = """
mutation customerCreate($input: CustomerInput!) {
  customerCreate(input: $input) {
    customer {
      id
      firstName
    }
    userErrors {
      field
      message
    }
  }
}
"""

var1 = { "input": {"firstName": "vivek","lastName": "singh", "email": "viveksingh@teleworm.us" }}



Copy="""
mutation productCreate($input: ProductInput!) {
        productCreate(input: $input) {
              product {
                id
              }
              userErrors {
              field
              message      
            }
        }
}"""
var2 = { "input": {"title": "Oneplus", "productType": "Snowboard", "vendor": "talkingmart"}}




print ("hi")

response = requests.post(shop_url+'/graphql.json', json={'query': cc, 'variables': var1})
#response = requests.post(shop_url+'/graphql.json', json={'query': Copy, 'variables': var2})

#print ("The response code is: %s",response.status_code)
if response.status_code==400:
        raise ValueError('GraphQL error:' + response.text)
answer = json.loads(response.text)
print (answer)
print(response)
