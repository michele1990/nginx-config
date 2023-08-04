import os

def create_nginx_config(domain, port):
    config_path = f"/etc/nginx/sites-available/{domain}"
    symlink_path = f"/etc/nginx/sites-enabled/{domain}"

    # Remove existing configuration file and symlink if they exist
    if os.path.exists(config_path):
        os.remove(config_path)
        print(f"Removed existing configuration file {config_path}.")

    if os.path.exists(symlink_path):
        os.remove(symlink_path)
        print(f"Removed existing symlink {symlink_path}.")

    config_content = f"""server {{
        listen 80;
        server_name {domain};

        location / {{
            proxy_pass http://localhost:{port};
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection 'upgrade';
            proxy_set_header Host $host;
            proxy_cache_bypass $http_upgrade;
        }}
    }}"""

    # Write the configuration file
    with open(config_path, 'w') as config_file:
        config_file.write(config_content)

    # Create a symbolic link
    os.symlink(config_path, symlink_path)

    # Test the Nginx configuration
    os.system("sudo nginx -t")

    # Reload Nginx
    os.system("sudo nginx -s reload")

    print(f"Configuration for {domain} created and Nginx reloaded.")

if __name__ == "__main__":
    domain = input("Please enter the domain: ")
    port = input("Please enter the port: ")
    create_nginx_config(domain, port)
