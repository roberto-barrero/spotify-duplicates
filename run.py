"""Application entry point."""
from app import create_app
import os

# Get configuration from environment variable or use default
config_name = os.environ.get('FLASK_CONFIG') or 'development'
app = create_app(config_name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
