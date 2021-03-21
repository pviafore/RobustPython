from find_workers import find_workers_available_for_time
import datetime
from typing import List

def get_ratio(*args):
    return 3.0

class Worker:
    pass

open_time = datetime.datetime.now()
workers: list[str] = find_workers_available_for_time(open_time)
numbers: list[int] = []
ratio: float = get_ratio(5,3)

number: int = 0
text: str = "useless"
values: list[float] = [1.2, 3.4, 6.0]
worker: Worker = Worker()
