import os
import uvicorn
from app.helper.logger import init_logger

if __name__ == "__main__":
    init_logger()
    PORT = int(os.getenv("DEFAULT_PORT")) if os.getenv("DEFAULT_PORT") else 8080
    uvicorn.run('app.config:app', host='0.0.0.0', port=PORT)
