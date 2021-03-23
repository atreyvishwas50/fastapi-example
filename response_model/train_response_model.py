from pydantic import BaseModel
import datetime


class Train(BaseModel):
    name: str
    expected_arrival_time: datetime.datetime
    expected_departure_time: datetime.datetime
