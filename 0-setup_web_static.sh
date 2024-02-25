#!/usr/bin/env bash
# configer the server to be ready for deployment
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/{releases,shared}
sudo mkdir -p /data/web_static/releases/test/

sudo touch /data/web_static/releases/test/index.html

# Create a basic HTML file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html >/dev/null

# Remove existing symbolic link and create a new one
sudo rm -f /data/web_static/current
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Adjust ownership permissions
sudo chown -hR ubuntu:ubuntu /data/

# Add new location block to NGINX configuration

sudo sed -i '11 i \\n\tlocation /hbnb_static {\n\talias /data/web_static/current;\n\t}' /etc/nginx/sites-available/default

# Restart NGINX to apply the changes
sudo systemctl restart nginx
