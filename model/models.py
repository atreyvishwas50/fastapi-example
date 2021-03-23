from sqlalchemy import Column, Integer, DateTime, ForeignKey, String
from . import db_config


class Train(db_config.Base):
    __tablename__ = "train"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    expected_arrival_time = Column(DateTime)
    expected_departure_time = Column(DateTime)


class TrainDailyData(db_config.Base):
    __tablename__ = "train_daily_data"

    id = Column(Integer, ForeignKey("train.id"), primary_key=True)
    actual_arrival_time = Column(DateTime)
    actual_departure_time = Column(DateTime)
