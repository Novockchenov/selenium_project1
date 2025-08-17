import json
from pathlib import Path

class ConfigReader:
    _config = None

    @classmethod
    def get_config(cls):
        if cls._config is None:
            config_path = Path(__file__).parent.parent / "config.json"
            with open(config_path, 'r') as f:
                cls._config = json.load(f)
        return cls._config

    @classmethod
    def get_wait_time(cls):
        return cls.get_config()["default_wait_time"]

    @classmethod
    def get_base_url(cls):
        return cls.get_config()["base_url"]