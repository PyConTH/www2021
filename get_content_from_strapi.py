import requests
from requests.exceptions import HTTPError
import sys

def download_content(resource_name, api_url):
  try:
    print(f'downloading {resource_name} page at {api_url}...')
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

# Add new page name here after you add a new content type on Strapi
page_names = [
  'about',
  'coc-procedure',
  'code-of-conduct',
  'covid-19',
  'diversity-equity-and-inclusion',
  'event',
  'faq',
  'lightning-talks',
  'online',
  'our-sponsors',
  'party',
  'speakers',
  'speakers-advice',
  'speakers-info',
  'sponsor',
  'the-conference',
  'volunteer',
  'workshops',
  'sprints'
]

for p in page_names:
  download_content(p, f'https://pyconth-strapi.herokuapp.com/{p}')
