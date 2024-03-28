from typing import Type, TypeVar, Generic, List, Optional

from sqlalchemy import or_
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound

from fastapi import HTTPException, status, Response

from pydantic import BaseModel



# Define type variables for SQLAlchemy model and Pydantic schemas
ModelType = TypeVar("ModelType")
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

class CRUDGeneric(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):

    def __init__(self, model: Type[ModelType]):
        
        self.model = model

    def get(self, id: int, db: Session) -> ModelType:

        try:
            
            result = db.query(self.model).filter(self.model.id == id).one()
            
            return result
        
        except NoResultFound:

            raise HTTPException(status_code=404, detail=f"{self.model.__name__} not found")
        

    def get_all(self, db: Session, skip: int = 0, limit: int = 100, search_fields: Optional[List[str]] = None, search_term: Optional[str] = "") -> List[ModelType]:

        query = db.query(self.model)

        if search_term and search_fields:
            
            search_conditions = []

            for field in search_fields:

                search_conditions.append(getattr(self.model, field).ilike(f'%{search_term}%'))

            query = query.filter(or_(*search_conditions))

        results = query.offset(skip).limit(limit).all()

        return results
    
    def create(self, db: Session, *, object_in: CreateSchemaType) -> ModelType:

        object_in_data = object_in.dict()

        db_object = self.model(**object_in_data)

        db.add(db_object)

        db.commit()

        db.refresh(db_object)

        return db_object
    
    def update(self, db: Session, *, db_object: ModelType, object_in: UpdateSchemaType | dict[str, any]) -> ModelType:
        
        object_data = db_object.__dict__

        if isinstance(object_in, dict):

            update_data = object_in

        else:

            update_data = object_in.dict(exclude_unset=True)
        
        for field in object_data:

            if field in update_data:

                setattr(db_object, field, update_data[field])
        
        db.add(db_object)

        db.commit()

        db.refresh(db_object)

        return db_object

    def remove(self, db: Session, *, id: int) -> ModelType:
        
        object_del = db.get(self.model, id)
        
        if not object_del:

            raise HTTPException(status_code=404, detail=f"{self.model.__name__} not found")
        
        db.delete(object_del)
        
        db.commit()
        
        return Response(status_code=status.HTTP_204_NO_CONTENT)
