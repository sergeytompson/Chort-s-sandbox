import logging
import requests

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
    result = requests.get(URL).json()
    data = result.get('results')
    name_data = get_name_data(data)
    name = f'{get_first_name(name_data)} {get_last_name(name_data)}'
    logger.info(f'random name: {name}')
    return name
