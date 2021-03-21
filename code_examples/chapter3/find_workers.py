import datetime
import random
from typing import List

class WorkerDatabase:
    def get_all_workers(self) -> list[str]:
        return []

def get_emergency_workers():
    return []

def is_available(name: str):
    return True

worker_database = WorkerDatabase()
OWNER = 'Pat'

def schedule(worker, open_time):
    pass


def schedule_restaurant_open(open_time: datetime.datetime, 
                             workers_needed: int):
    workers = find_workers_available_for_time(open_time)
    # use random.sample to pick X available workers
    # where X is the number of workers needed.
    for worker in random.sample(workers, workers_needed):
        schedule(worker, open_time)


def find_workers_available_for_time(open_time: datetime.datetime):
    workers = worker_database.get_all_workers()
    available_workers = [worker for worker in workers
                         if is_available(worker)]
    if available_workers:
        return available_workers

    # fall back to workers who listed they are available in
    # in an emergency
    emergency_workers = [worker for worker in get_emergency_workers()
                         if is_available(worker)]

    if emergency_workers:
        return emergency_workers

    # Schedule the owner to open, they will find someone else
    return [OWNER]

assert find_workers_available_for_time(datetime.datetime.now()) == ["Pat"]
