import requests
from requests.exceptions import HTTPError
import sys

def download_content(resource_name, api_url):
  try:
    print(f'downloading {resource_name} page...')
    resp = requests.get(api_url)
    resp.raise_for_status()

    page = resp.json()
    file_en = open(f'./content/pages/{resource_name}-en.md', 'w')
    file_en.write(page['markdown_content_en'])
    file_en.close()
    if page['markdown_content_th']:
      file_th = open(f'./content/pages/{resource_name}-th.md', 'w')
      file_th.write(page['markdown_content_th'])
      file_th.close()
  except HTTPError as http_err: 
    print(f'HTTP error: {http_err}')

if (len(sys.argv) == 3):
  resource_name=str(sys.argv[1])
  api_url=str(sys.argv[2])
  download_content(resource_name, api_url)
else:
  print('invalid args try: python3 get_content_from_strapy.py <page-name> <strapi-api-endpoint-url>')
