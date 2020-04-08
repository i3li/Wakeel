import configuration as cfg
import listeners
import time
from pathlib import Path

_SLEEP_DURATION_SEC = 1


def configuration():
    config = cfg.get_config()
    return config


_LOOKUP_DIRS = [
    Path.home().joinpath('Dropbox'),
    Path.home().joinpath('Google Drive'),
    Path.home().joinpath('One Drive')
]
_DEFAULT_REQ_DIR_NAME = 'WakeelRequests'
_DEFAULT_RES_DIR_NAME = 'WakeelResponses'


def _communication_directories():
    req_dir, res_dir = None, None
    for possible_path in _LOOKUP_DIRS:
        if possible_path.is_dir():
            req_dir = possible_path.joinpath(_DEFAULT_REQ_DIR_NAME)
            res_dir = possible_path.joinpath(_DEFAULT_RES_DIR_NAME)
            if not req_dir.is_dir():
                req_dir.mkdir()
            if not res_dir.is_dir():
                res_dir.mkdir()
    while not req_dir or not res_dir:
        req_dir = Path(input('Please enter the request directory: '))
        res_dir = Path(input('Please enter the response directory: '))
        if not req_dir.is_dir():
            print(f'No such directory: {req_dir}')
            req_dir = None
        if not res_dir.is_dir():
            print(f'No such directory: {res_dir}')
            res_dir = None
    return req_dir, res_dir


def _file_listener_config():
    config = configuration()
    req_path, res_path = None, None
    if config:
        req_path, res_path = config.req_path, config.res_path
    if not config or not req_path.is_dir() or not res_path.is_dir():
        # Search for possible configurations
        new_req_path, new_res_path = _communication_directories()
        cfg.set_config(cfg.Configuration(new_req_path, new_res_path))
        return _file_listener_config()
    return req_path, res_path


def start_file_listener():
    req_path, res_path = _file_listener_config()
    listener = listeners.FileListener(req_path, res_path)
    print(f'Listenin on: {req_path}')
    print(f'Responses are written in: {res_path}')
    listener.start()
    try:
        while True:
            time.sleep(_SLEEP_DURATION_SEC)
    except KeyboardInterrupt:
        listener.stop()


def main():
    start_file_listener()


if __name__ == '__main__':
    main()
