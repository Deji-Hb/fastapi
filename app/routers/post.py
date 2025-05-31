from fastapi import Depends, FastAPI, Response, status, HTTPException, APIRouter
from .. import schemas, models, oauth2
from sqlalchemy import func
from sqlalchemy.orm import Session
from ..database import engine, get_db
from typing import List, Optional

router = APIRouter(prefix="/posts", tags=["Posts"])

# these are path operations
# we have to use list since we're dealing with multiple posts
@router.get("/", response_model=list[schemas.PostOut])
def get_posts(
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
    Limit: int = 10,
    skip: int = 0,
    search: Optional[str] = "",
):
    # cursor.execute("""SELECT * FROM posts""")
    # posts = cursor.fetchall()
    # posts = (
    #     db.query(models.Post)
    #     .filter(models.Post.title.contains(search))
    #     .limit(Limit)
    #     .offset(skip)
    #     .all()
    # )
    ## outer join is the default join on postgresql but inner join is the default on sqlalchemy
    posts = (
        db.query(models.Post, func.count(models.Vote.post_id).label("votes"))
        .join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True)
        .group_by(models.Post.id)
        .filter(models.Post.title.contains(search))
        .limit(Limit)
        .offset(skip)
        .all()
    )
    #yt solution to the response_model bug
    #results = list(map(lambda x: x._mapping, results))
    return posts


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=schemas.PostRequest
)
# to access a resource that requires you to be logged in you nedd to use the oauth dependency
def create_posts(
    post: schemas.PostCreate,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    # cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s ) RETURNING * """,
    # (post.title, post.content, post.published))
    # new_post = cursor.fetchone()
    # conn.commit()
    # unpacking the variables in the models file e.g title. Instead of typing every variable in the models.Post()
    new_post = models.Post(owner_id=current_user.id, **post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


# the id is a path parameter
@router.get("/{id}", response_model=schemas.PostOut)
# this will validate and convert the path parameter to an int directly
# the reason we validate as int is so the input in id from user isn't a str
# we convert to str back because the sql query is in string format
# incase of a weird issue, a comma in front of str(id) should fix it
def get_post(
    id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    # cursor.execute(f"""SELECT * FROM posts WHERE id = %s""", (str(id)))
    # post = cursor.fetchone()
    # .all() will look through all the posts even after finding the required post
    # post = db.query(models.Post).filter(models.Post.id == id).first()
    post = (
        db.query(models.Post, func.count(models.Vote.post_id).label("votes"))
        .join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True)
        .group_by(models.Post.id).first()
    )
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} was not found",
        )
    return post


# to delete a post
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(
    id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    # cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", ((str(id))))
    # deleted_post = cursor.fetchone()
    # #to make changes directly to the database we use conn.commit()
    # conn.commit()
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id of {id} does not exist",
        )
    if current_user.id != post.owner_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authoruzed to perform requested action",
        )
    post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model=schemas.PostRequest)
def update_post(
    id: int,
    upd_post: schemas.PostCreate,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    # cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""",
    # (post.title, post.content, post.published, str(id)))
    # updated_post = cursor.fetchone()
    # conn.commit()
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id of {id} does not exist",
        )
    # post.title = upd_post.title
    # post.content = upd_post.content
    if current_user.id != post.owner_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authoruzed to perform requested action",
        )
    post_query.update(upd_post.model_dump(), synchronize_session=False)
    db.commit()
    return post_query.first()


#
