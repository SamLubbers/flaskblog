from .default import Config

class TestingConfig(Config):
    TESTING = True

    SQLALCHEMY_DATABASE_URI = f"{SQLALCHEMY_DATABASE_URI}-test"