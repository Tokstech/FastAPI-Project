from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, users, auth, vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware


# We dont need this command below again because we have alembic
# models.Base.metadata.create_all(bind=engine)

# origins = ["https://www.google.com"]
origins = ["*"]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title": "favourite food", "content": "Rice", "id": 2}]

# def find_post(id):
#     for p in my_posts:
#         if p["id"] == id:
#             return p

# def find_index_post(id):
#     for i, p in enumerate(my_posts):
#         if p['id'] == id:
#             return i

# find_index_post(1)

@app.get("/")
async def root():
  return {"message": "Welcome to my api"}

# @app.get("/sqlalchemy")
# def test_posts(db: Session = Depends(get_db)):

#     posts = db.query(models.Post).all()
#     return {"data": posts}

app.include_router(post.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)





