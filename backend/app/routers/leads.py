from fastapi import APIRouter, status, HTTPException, Response, Depends, Query

from typing import List, Optional

from sqlalchemy.orm import Session

from app import models, schemas, oauth2, crud

from app.database import get_db

from datetime import datetime

router = APIRouter(
    tags=["Leads"],
    prefix="/leads"
)

lead_crud = crud.CRUDGeneric[models.Lead, schemas.LeadCreate, schemas.LeadOut](models.Lead)


@router.get("/", response_model=List[schemas.LeadOut])
def get_leads(
    db: Session = Depends(get_db),
    skip: int = 0, 
    limit: int = 100, 
    search_fields: Optional[List[str]] = Query(default=None),
    search_term: Optional[str] = Query(default=""),
    current_user: int = Depends(oauth2.get_current_user)
    ):

    leads = lead_crud.get_all(db=db, skip=skip, limit=limit, search_fields=search_fields, search_term=search_term)

    return leads


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.LeadOut)
def create_lead(
    lead: schemas.LeadCreate,
    db: Session = Depends(get_db), 
    current_user: int = Depends(oauth2.get_current_user)
    ):

    new_lead = models.Lead(**lead.dict(), owner_id=current_user.id)

    db.add(new_lead)

    db.commit()

    db.refresh(new_lead)

    return new_lead


@router.get("/{id}", response_model=schemas.LeadOut)
def get_lead(
    id: int, 
    db: Session = Depends(get_db), 
    current_user: int = Depends(oauth2.get_current_user)
    ):

    lead = lead_crud.get(id=id, db=db)

    
    return lead



@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_lead(
    id: int, 
    db: Session = Depends(get_db), 
    current_user: int = Depends(oauth2.get_current_user)
    ):

    try:

        lead_crud.remove(id=id, db=db)

        return {"detail": "Successfully deleted."}
    
    except HTTPException as e:

        raise e


@router.put("/{id}", response_model=schemas.LeadOut)
def update_lead(
    id: int, 
    updated_lead: schemas.LeadCreate, 
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user)
    ):

    try:

        db_run = lead_crud.get(id=id, db=db)

    except HTTPException as e:

        raise e
    
    try:

        updated_lead = lead_crud.update(db=db, db_object=db_run, object_in=updated_lead)
        db_run.updated_at = datetime.utcnow()

        return updated_lead
    
    except Exception as e:

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while updating the lead"
        )