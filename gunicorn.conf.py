import multiprocessing
from os import getenv


bind = f"0.0.0.0:{getenv('PORT')}"
workers = multiprocessing.cpu_count()
threads = multiprocessing.cpu_count() * 2
