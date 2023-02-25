from fastapi import APIRouter
from starlette.responses import PlainTextResponse

router = APIRouter()


@router.get('/helloworld', response_class=PlainTextResponse)
def hello(name: str = 'Stranger'):
    return f'Hello {name}'


@router.get('/author', response_class=PlainTextResponse)
def author():
    return 'Mehdi Samadinia'


@router.get('/health', response_class=PlainTextResponse)
async def health():
    return PlainTextResponse(content="", status_code=200)
