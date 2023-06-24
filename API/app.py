from src.settings import FlaskConfig
from src.API.entrypoint.api import ApiRest


if __name__ == "__main__":
    app = ApiRest.init_api()
    app.run(host=FlaskConfig.FLASK_HOST, port=FlaskConfig.FLASK_PORT)
    
