from flask import Flask
from app.facades.facade import facade
from dotenv import load_dotenv

webservice = Flask("OPEI 2023 Webservice")
webservice.register_blueprint(facade)

if __name__ == "__main__":
    if load_dotenv() is False:
        raise(Exception(".env file not found"))
    webservice.run(host="0.0.0.0")
