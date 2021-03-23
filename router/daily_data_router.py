from fastapi import APIRouter, Depends, HTTPException
from response_model import train_daily_data_response_model
from sqlalchemy.orm import Session
from model import models, db_config
from dao import train_daily_data_dao, train_dao

router = APIRouter()


def get_db():
    db = db_config.Session()
    try:
        yield db
    finally:
        db.close()


@router.get("/train/expected/{train_id}")
def get_actual_train(train_id: int, db: Session = Depends(get_db)):
    train_daily_data = train_daily_data_dao.get_train(db=db, train_daily_data_id=train_id)
    if train_daily_data is not None:
        return train_daily_data_response_model.TrainDailyData(actual_arrival_time=train_daily_data.actual_arrival_time,
                                                              actual_departure_time=train_daily_data.actual_departure_time)
    else:
        return HTTPException(status_code=404, detail="Train not found")


@router.post("/train/expected/{train_id}")
def post_expected_train(train_id: int, train: train_daily_data_response_model.TrainDailyData,
                        db: Session = Depends(get_db)):
    check = train_dao.get_train(db=db, train_id=train_id)
    if check is None:
        return {"message": "There is no train with the given ID"}
    else:
        train_daily_data = models.TrainDailyData(id=train_id,
                                                 actual_arrival_time=train.actual_arrival_time,
                                                 actual_departure_time=train.actual_departure_time)
        train_daily_data_dao.create_train(db=db, train=train_daily_data)
        return {"message": "Train saved successfully"}
