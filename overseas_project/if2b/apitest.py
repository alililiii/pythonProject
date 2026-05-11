import time
import concurrent.futures
import requests


def send_request(url, data):

    start_time = time.time()

    response = requests.post(url, data)

    end_time = time.time()

    return end_time - start_time


url = ''

times = []



