pelican-themes -i theme

# Grab the content from Notion
python get_posts_from_notion.py

# Build the site
make publish
