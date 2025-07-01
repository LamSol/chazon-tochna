import os

class Config:
    # Default settings for the app
    SHOP_NAME = "Chazon Tochna"
    LOGO_PATH = "/static/images/default-logo.jpg"
    CONTACT_EMAIL = "example@clinic.com"
    ADDRESS = "123 Vision Street, EyeCity"
    # Add more as needed

# Optional for future: support for environment-based configs
class DevConfig(Config):
    DEBUG = True

class ProdConfig(Config):
    DEBUG = False
