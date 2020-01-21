import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

import settings
from views import api


def create_app():
    fast_app = FastAPI()
    fast_app.mount('/api', api)
    fast_app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )
    return fast_app


app = create_app()

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=9191, debug=settings.DEBUG, reload=settings.DEBUG)
