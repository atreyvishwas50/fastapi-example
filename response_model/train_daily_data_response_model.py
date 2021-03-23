from pydantic import BaseModel
import datetime


class TrainDailyData(BaseModel):
    actual_arrival_time: datetime.datetime
    actual_departure_time: datetime.datetime
