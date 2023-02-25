import os
import uvicorn

from app.main.config import create_app
from app.main.helper.logger import init_logger

if __name__ == "__main__":
    init_logger()
    PORT = int(os.getenv("DEFAULT_PORT")) if os.getenv("DEFAULT_PORT") else 8080
    uvicorn.run(create_app, host='0.0.0.0', port=PORT)
