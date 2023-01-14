from fastapi import APIRouter

router = APIRouter()


@router.get('/hello')
def hello(name: str = 'Stranger'):
    return f'Hello {name}'


@router.get('/author')
def author():
    return 'Mehdi Samadinia'
