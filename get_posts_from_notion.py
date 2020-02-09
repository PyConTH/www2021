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
    if not post.type == 'page':
        print("Skipping", post)
        continue

    # Handle Frontmatter
    text = f"""---
title: {post.title}
date: {post.created}
summary: {post.summary}
slug: {post.slug}
lang: {post.language}
---
"""
    # Handle Title
    text = text + '\n\n' + '# ' + post.title + '\n\n'
    for content in post.children:
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
        # Handles Images
        elif content.type == 'image':
            text = text + '![' + content.id + '](' + content.source + ')\n\n'
        # Handles Bullets
        elif content.type == 'bulleted_list':
            text = text + '* ' + content.title + '\n'
        # Handles Dividers
        elif content.type == 'divider':
            text = text + '---' + '\n\n'
        # Handles Basic Text, Links, Single Line Code
        elif content.type == 'text':
            text = text + content.title + '\n\n'
        else:
            print("Ignoring unknown block", content)


        title = post.title.replace(' ', '-')
        title = title.replace(',', '')
        title = title.replace(':', '')
        title = title.replace(';', '')
        title = title.lower()

    with open('./content/blog/' + title + '.md', 'w') as post:
        post.write(text)
        print('Wrote A New Page')
        print(text)
