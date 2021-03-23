from sqlalchemy.orm import Session
from model import models


def get_train(db: Session, train_id: int):
    return db.query(models.Train).filter(models.Train.id == train_id).first()


def create_train(db: Session, train: models.Train):
    db.add(train)
    db.commit()
    db.refresh(train)
