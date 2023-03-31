from fastapi import FastAPI
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from models import Post
from fastapi import Path, Query
from typing import List

app = FastAPI(
    title='Minha API Cesmac',
    description='Descrição da API',
    version='0.0.1'
)

posts = {
    1: {
        'titulo': 'Post Um'
    },
    2: {
        'titulo': 'Post Dois'
    }
}

@app.get('/posts')
async def get_posts():
    return posts

@app.get('/posts/{post_id}')
async def get_post(
    post_id:int = Path(gt=0, lt=3)):
        try:
            post = posts[post_id]
            return post
        except KeyError:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Post inexistente.')
        
@app.get('/posts', status_code=status.HTTP_201_CREATED, response_model=List[Post])
async def post_curso(post: Post):
    id = len(posts) + 1
    posts[id] = post
    return post


@app.post('/posts', status_code=status.HTTP_201_CREATED)
async def post_curso(post: Post):
    id = len(posts) + 1
    posts[id] = post
    return post

@app.put('/posts/{post_id}')
async def atualiza_post(post_id: int, post: Post):
    if post_id in posts:
        posts[post_id] = post
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Post não existe')
    return post

@app.delete('/posts/{post_id}', status_code=status.HTTP_204_NO_CONTENT)
async def deleta_post(post_id: int):
    if post_id in posts:
        del posts[post_id]
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Não existe POST.")
@app.get('/somar')
def somar(x:int=Query(default=None, gt=0) ,y: int=Query(default=None, gt=0), z:int=Query(default=None, gt=0)):
    return x+y+z

@app.get('/subtrair')
def subtrair(x:int = Query(default=None, gt=0), y:int = Query(default=None, gt=0), z:int = Query(default=None, gt=0)):
    return x-y-z
@app.get('/multiplicar')
def multiplicar(x:int = Query(default=None, gt=0), y:int = Query(default=None, gt=0), z:int = Query(default=None, gt=0)):
    return x*y*z
@app.get('/dividir')
def dividir(x:int = Query(default=None, gt=0), y:int = Query(default=None, gt=0), z:int = Query(default=None, gt=0)):
    return x/y/z

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('app:app', host="0.0.0.0", port=8000, reload=True)