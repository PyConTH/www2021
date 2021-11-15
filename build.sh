pelican-themes -i theme

# Grab the content from Strapi
make strapi/download

# Convert the hubilo exported excel
make schedule

# Build the site
make publish
