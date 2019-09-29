''' Script to grab posts from Notion pages
'''

# Modified from https://medium.com/@tfaieta/how-i-use-notion-as-my-cms-for-my-gatsby-site-c449cc9a4687

import os
import datetime
from notion.client import NotionClient

CLIENT = NotionClient(token_v2=os.environ["NOTION_TOKEN"])
BLOG_HOME = CLIENT.get_block(os.environ["NOTION_BLOG_POSTS_PAGE"])

# Main Loop
for post in BLOG_HOME.children:
    # Handle Frontmatter
    text = """---
title: %s
date: "%s"
description: ""
---""" % (post.title, datetime.datetime.now())
    # Handle Title
    text = text + '\\n\\n' + '# ' + post.title + '\\n\\n'
    for content in post.children:
        # Handles H1
        if content.type == 'header':
            text = text + '# ' + content.title + '\\n\\n'
        # Handles H2
        if content.type == 'sub_header':
            text = text + '## ' + content.title + '\\n\\n'
        # Handles H3
        if content.type == 'sub_sub_header':
            text = text + '### ' + content.title + '\\n\\n'
        # Handles Code Blocks
        if content.type == 'code':
            text = text + '```\\n' + content.title + '\\n```\\n'
        # Handles Images
        if content.type == 'image':
            text = text + '![' + content.id + '](' + content.source + ')\\n\\n'
        # Handles Bullets
        if content.type == 'bulleted_list':
            text = text + '* ' + content.title + '\\n'
        # Handles Dividers
        if content.type == 'divider':
            text = text + '---' + '\\n'
        # Handles Basic Text, Links, Single Line Code
        if content.type == 'text':
            text = text + content.title + '\\n'

    title = post.title.replace(' ', '-')
    title = title.replace(',', '')
    title = title.replace(':', '')
    title = title.replace(';', '')
    title = title.lower()

    with open('../content/blog/' + title + '.md', 'w') as post:
        post.write(text)
        print('Wrote A New Page')
        print(text)
