''' Script to grab posts from Notion pages
'''

# Modified from https://medium.com/@tfaieta/how-i-use-notion-as-my-cms-for-my-gatsby-site-c449cc9a4687

import os
import datetime
from notion.client import NotionClient

CLIENT = NotionClient(token_v2=os.environ["NOTION_TOKEN"])
NOTION_BLOG_POSTS = CLIENT.get_block(os.environ["NOTION_BLOG_POSTS"])
NOTION_PAGES = CLIENT.get_block(os.environ["NOTION_PAGES"])

def get_pages(table, outdir):
    # Main Loop
    for page in table.collection.get_rows():
        print(page)
        if not page.type == 'page':
            print("Skipping", page)
            continue

        # Handle Frontmatter
        text = """---
title: %s
date: %s
summary: %s
slug: %s
lang: %s
---
""" % (page.title, page.created, page.summary, page.slug, page.language)
        # Handle Title
        text = text + '\n\n' + '# ' + page.title + '\n\n'
        for content in page.children:
            # Handles H1
            if content.type == 'header':
                text = text + '# ' + content.title + '\n\n'
            # Handles H2
            elif content.type == 'sub_header':
                text = text + '## ' + content.title + '\n\n'
            # Handles H3
            elif content.type == 'sub_sub_header':
                text = text + '### ' + content.title + '\n\n'
            # Handles Code Blocks
            elif content.type == 'code':
                text = text + '```\n' + content.title + '\n```\n\n'
            # Handles callouts
            elif content.type == 'callout':
                text = text + '> ' + content.title + '\n\n'
            # Handles Images
            elif content.type == 'image':
                text = text + '![' + content.id + '](' + content.source + ')\n\n'
            # Handles lists
            elif content.type == 'bulleted_list':
                text = text + '* ' + content.title + '\n'
            elif content.type == 'numbered_list':
                text = text + '1. ' + content.title + '\n'
            # Handles Dividers
            elif content.type == 'divider':
                text = text + '---' + '\n\n'
            # Handles Basic Text, Links, Single Line Code
            elif content.type == 'text':
                text = text + content.title + '\n\n'
            else:
                print("Ignoring unknown block type", content.type, content)

        with open('./content/%s/%s%s.md' % (outdir, page.slug, '-%s'%page.language if page.language else ''), 'w') as page:
            page.write(text)
            print('Wrote A New Page')


get_pages(NOTION_PAGES, 'pages')
get_pages(NOTION_BLOG_POSTS, 'blog')
