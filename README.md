# Nginx Configuration Automation Script

This repository contains a Python script to automate the process of setting up an Nginx configuration for a given domain and port. It is designed to simplify the deployment process for web applications, allowing for quick and easy setup.

## Features

- Automatically generates an Nginx configuration file based on user input.
- Creates a symbolic link in the `sites-enabled` directory.
- Tests the Nginx configuration for syntax errors.
- Reloads Nginx to apply the new configuration.

## Requirements

- Python 3.x
- Nginx
- sudo privileges to write to system directories and reload Nginx.

## Usage

1. Clone this repository to your local machine or server.
2. Run the script using the following command:

   \`\`\`bash
   sudo python3 nginx_config.py
   \`\`\`

3. Follow the prompts to enter your domain and port.

## Limitations

- This script is intended for simple configurations and may not cover all use cases.
- It does not handle SSL configuration. If HTTPS is required, additional manual configuration may be needed.
- Make sure to backup any existing configurations before running the script.

## Contributing

If you would like to contribute or have any issues or requests, please feel free to open an issue or pull request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
