from fastapi import status, HTTPException, Response, Depends, APIRouter

from sqlalchemy.orm import Session

from .. import models, schemas, utils, oauth2
from ..database import get_db

router = APIRouter(
    tags=["Users"],
    prefix="/users"
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.SignUpOut)
async def create_user(user: schemas.CreateUser, db: Session = Depends(get_db)):

    hashed_password = utils.hash(user.password)

    user.password = hashed_password

    new_user = models.User(**user.dict())

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    access_token = oauth2.create_access_token(
        data = {"user_id": new_user.id}
    )

    return schemas.SignUpOut(user=user, token=schemas.Token(access_token=access_token, token_type="bearer"))



@router.get("/me", response_model=schemas.UserBase)
def get_user(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    # user = db.query(models.User).filter(models.User.id == id).first()

    # if not user:

    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
    #                         detail=f"User with id: {id} does not exist")
    
    return current_user