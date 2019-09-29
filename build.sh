# Setup the theme
git clone https://github.com/PyConTH/www2020-elegant.git
pelican-themes -i www2020-elegant

# Grab the content from Notion
python get_posts_from_notion.py

# Build the site
make html
