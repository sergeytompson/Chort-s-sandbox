import logging

import requests

from requests.adapters import HTTPAdapter, Retry

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

URL = 'https://randomuser.me/api/?nat=us&randomapi'


def get_name_data(_data: dict) -> dict:
    indx = 0
    key = 'name'
    return _data[indx][key]


def get_first_name(_data: dict) -> str:
    key = 'first'
    return _data.get(key, None)


def get_last_name(_data: dict) -> str:
    key = 'last'
    return _data.get(key, None)


def get_names(count: int = 50) -> str:
    for _ in range(count):
        yield get_name()


def get_name() -> str:
    session = requests.Session()
    retries = Retry(total=10, backoff_factor=0.1, status_forcelist=[500, 502, 503, 504])
    session.mount('https://', HTTPAdapter(max_retries=retries))
    result = session.get(URL, timeout=5).json()
    data = result.get('results')
    name_data = get_name_data(data)
    name = f'{get_first_name(name_data)} {get_last_name(name_data)}'
    logger.info(f'random name: {name}')
    return name
