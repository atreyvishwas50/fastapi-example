from sqlalchemy.orm import Session
from model import models


def get_train(db: Session, train_daily_data_id: int):
    return db.query(models.TrainDailyData).filter(models.TrainDailyData.id == train_daily_data_id).first()


def create_train(db: Session, train: models.TrainDailyData):
    db.add(train)
    db.commit()
    db.refresh(train)
