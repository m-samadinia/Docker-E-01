import os
import uvicorn

if __name__ == "__main__":
    PORT = int(os.getenv("DEFAULT_PORT")) if os.getenv("DEFAULT_PORT") else 8080
    uvicorn.run('app.config:app', host='0.0.0.0', port=PORT, reload=True)
