import json


class ConfigReader:
    CONFIG_PATH = "config.json"
    _config = None

    @classmethod
    def get_config(cls):
        if cls._config is None:
            with open(cls.CONFIG_PATH, 'r') as f:
                cls._config = json.load(f)
        return cls._config

    @classmethod
    def get_wait_time(cls):
        return cls.get_config()["default_wait_time"]

    @classmethod
    def get_base_url(cls):
        return cls.get_config()["base_url"]

    @classmethod
    def get_driver_options(cls):
        return cls.get_config().get("driver_options", [])
