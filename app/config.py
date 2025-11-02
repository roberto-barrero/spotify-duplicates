"""Configuration settings for the Flask application."""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """Base configuration class with common settings."""
    
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = False
    TESTING = False
    
    # Spotify API configuration (to be used later)
    SPOTIFY_CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
    SPOTIFY_CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')


class DevelopmentConfig(Config):
    """Development environment configuration."""
    
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-do-not-use-in-production'


class ProductionConfig(Config):
    """Production environment configuration."""
    
    DEBUG = False
    
    @classmethod
    def init_app(cls, app):
        """Initialize application-specific production settings."""
        # Validate critical settings are configured in production
        if not app.config.get('SECRET_KEY'):
            raise ValueError("SECRET_KEY must be set in production environment")
        if not app.config.get('SPOTIFY_CLIENT_ID') or not app.config.get('SPOTIFY_CLIENT_SECRET'):
            raise ValueError("Spotify credentials must be set in production environment")


class TestingConfig(Config):
    """Testing environment configuration."""
    
    TESTING = True


# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
