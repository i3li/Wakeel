"""Handle getting and setting configurations."""
import configparser
from pathlib import Path

class Configuration(object):
    """Represents a configuration.

    A configuration has two paths. One for the request folder.
    The other is for the response folder.
    """

    def __init__(self, req_path, res_path):
        self.req_path = req_path if isinstance(req_path, Path) else Path(str(req_path))
        self.res_path = res_path if isinstance(res_path, Path) else Path(str(res_path))

    def __repr__(self):
        return f'Request: {self.req_path} - Response: {self.res_path}'


_DEFAULT_CONFIG_PATH = Path.home().joinpath('.wakeel.ini')
_COMMUNICATION_SECTION = 'Communication Folders'
_REQUEST_OPTION = 'Request'
_RESPONSE_OPTION = 'Response'

def get_config(config_path=_DEFAULT_CONFIG_PATH):
    """Gets the configuration

    Args:
        config_path: The path of the configuration file. Defaults tp $HOME/.wakeel.ini

    Returns:
        Configuration: The configuration object

    """
    config = configparser.ConfigParser()
    if config.read(config_path):
        comm_section = config[_COMMUNICATION_SECTION]
        return Configuration(comm_section[_REQUEST_OPTION], comm_section[_RESPONSE_OPTION])

def set_config(new_config, config_path=_DEFAULT_CONFIG_PATH):
    """Sets a new coonfiguration

    Args:
        new_config (Configuration): The new configuration.
        config_path: The path of the configuration file. Defaults tp $HOME/.wakeel.ini
    """

    config = configparser.ConfigParser()
    config.add_section(_COMMUNICATION_SECTION)
    config[_COMMUNICATION_SECTION][_REQUEST_OPTION] = str(new_config.req_path)
    config[_COMMUNICATION_SECTION][_RESPONSE_OPTION] = str(new_config.res_path)
    if not config_path.exists():
        # TODO: CHECK MODE .touch(0o644) (umask?)
        config_path.touch()
    with config_path.open('w') as fp:
        config.write(fp)


def main():
    print(get_config())
    # config = Configuration(str(Path.home().joinpath('req')), str(Path.home().joinpath('res')))
    # set_config(config)

if __name__ == '__main__':
    main()
