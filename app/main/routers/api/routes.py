from fastapi import APIRouter
from starlette.responses import PlainTextResponse

router = APIRouter()


@router.get('/helloworld', response_class=PlainTextResponse)
def hello(name: str = 'Stranger'):
    return PlainTextResponse(content=f'Hello {name}', status_code=200)


@router.get('/author', response_class=PlainTextResponse)
def author():
    return PlainTextResponse(content='Mehdi Samadinia', status_code=200)


@router.get('/health', response_class=PlainTextResponse)
def health():
    return PlainTextResponse(content="Ok", status_code=200)
