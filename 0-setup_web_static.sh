#!/usr/bin/env bash
# sets up the web servers for the deployment of web_static

# Install Nginx if not already installed
if ! command -v nginx &> /dev/null; then
    sudo apt-get -y update
    sudo apt-get -y install nginx
fi

# Create necessary directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file
echo "<html><head></head><body>Holberton School</body></html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership to ubuntu user and group recursively
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
nginx_config_file="/etc/nginx/sites-available/default"
nginx_alias_config="location /hbnb_static { alias /data/web_static/current/; }"
if ! grep -q "$nginx_alias_config" "$nginx_config_file"; then
    sudo sed -i "/^\s*server {/a $nginx_alias_config" "$nginx_config_file"
fi

# Restart Nginx
sudo service nginx restart

exit 0
