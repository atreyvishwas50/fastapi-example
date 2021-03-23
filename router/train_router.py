from fastapi import APIRouter, Depends, HTTPException
from response_model import train_response_model
from sqlalchemy.orm import Session
from model import models, db_config
from dao import train_dao

router = APIRouter()


def get_db():
    db = db_config.Session()
    try:
        yield db
    finally:
        db.close()


@router.get("/train/actual/{train_id}")
def get_expected_train(train_id: int, db: Session = Depends(get_db)):
    train = train_dao.get_train(db, train_id=train_id)
    if train:
        return train_response_model.Train(name=train.name,
                                          expected_arrival_time=train.expected_arrival_time,
                                          expected_departure_time=train.expected_departure_time)
    else:
        raise HTTPException(status_code=404, detail="Train not found")


@router.post("/train/actual")
def post_actual_train(train: train_response_model.Train, db: Session = Depends(get_db)):
    train_model = models.Train(name=train.name,
                               expected_arrival_time=train.expected_arrival_time,
                               expected_departure_time=train.expected_departure_time)
    train_dao.create_train(db, train_model)
    return {"message": "Train saved successfully"}
