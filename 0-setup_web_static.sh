#!/usr/bin/env bash
# configer the server to be ready for deployment
sudo apt-get update
sudo apt-get -y install nginx

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

echo '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>' >/data/web_static/releases/test/index.html

# create a new symbolic link
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Adjust ownership permissions
sudo chown -hR ubuntu:ubuntu /data/

# Add new location block to NGINX configuration

sudo sed -i '11 i \\n\tlocation /hbnb_static {\n\talias /data/web_static/current;\n\t}' /etc/nginx/sites-available/default

# Restart NGINX to apply the changes
sudo service nginx restart
