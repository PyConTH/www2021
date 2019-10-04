# Setup the theme
if [ -d www2020-elegant ]
then 
    cd www2020-elegant 
    git pull
    cd ..
else
    git clone https://github.com/PyConTH/www2020-elegant.git
fi

pelican-themes -i www2020-elegant

# Grab the content from Notion
python get_posts_from_notion.py

# Build the site
make html
