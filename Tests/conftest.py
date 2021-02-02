import pytest
from configparser import ConfigParser


@pytest.fixture
def param():
    config = ConfigParser()
    conf = "C:\\Users\\Eli\Desktop\\Project\\BondIT\\Tests\\config.ini"
    config.read(conf)

    data = {
        "BaseURI": config["API"]["BaseURI"],
        "universe_Resource": config["API"]["universe_Resource"],
        "username": config["API"]["user_name"],
        "password": config["API"]["password"],
        "universe_batch": config["API"]["universe_batch"]
    }
    return data


@pytest.fixture(params=["165e00968ddeea"])
def job_id(request):
    return request.param


@pytest.fixture(params=["134"])
def external_universe_id(request):
    return request.param
