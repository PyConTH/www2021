import requests
import sys

def download_content(api_url, filename, resource_name):
  print(f'downloading {resource_name} page...')
  page = requests.get(api_url).json()
  file = open(f'./content/pages/{filename}.md', 'w')
  file.write(page['markdown_content'])
  file.close()
  print('done')

# DEV mode does not need to provide args
URL="http://localhost:1337"
if (len(str(sys.argv)) == 1):
  URL=str(sys.argv[0])

page_metas = [
  {"url": f'{URL}/sponsors/1', "filename": "sponsor", "resource_name": "sponsor"},
  {"url": f'{URL}/abouts/1', "filename": "about-th", "resource_name": "about"}
]

for meta in page_metas:
  download_content(meta["url"], meta["filename"], meta["resource_name"])
