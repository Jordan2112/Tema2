class BasicConfig:
    USER_DB='postgres'
    PASS_DB='Jordan123'
    URL_DB='localhost'
    NAME_DB='flask_clase'
    FULL_URL_BD=f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'
    SQLALCHEMY_DATABASE_URI = FULL_URL_BD
    SQLALCHEMY_TRACK_NOTIFICATIONS=False
    SECRET_KEY = "llave secreta"