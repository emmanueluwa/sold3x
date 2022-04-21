import requests

ebay_sold_items_url = 'https://www.ebay.co.uk/'


print('Status Code', response.status_code)
response = requests.get(ebay_sold_items_url.encode('utf-8'))

#view as a html file
# with open('items.html', 'w', encoding='utf-8') as f:
#   f.write(response.text)
