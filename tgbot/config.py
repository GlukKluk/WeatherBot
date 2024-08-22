from dataclasses import dataclass
from typing import Optional

from environs import Env


@dataclass
class TgBot:
    """
    TgBot configuration class.

    Attributes
    ----------
    token : str
        The token used to connect to the telegram bot.
    admin_ids : list[int]
        List of admin ids, that can control the bot.
    use_redis : bool
        The flag to use redis for storing bot states.
    """

    token: str
    admin_ids: list[int]
    use_redis: bool

    @staticmethod
    def from_env(env: Env):
        """
        Creates the TgBot object from environment variables.
        """
        
        token = env.str("BOT_TOKEN")
        admin_ids = env.list("ADMIN_IDS", subcast=int)
        use_redis = env.bool("USE_REDIS")

        return TgBot(token=token, admin_ids=admin_ids, use_redis=use_redis)


@dataclass
class ApiConfig:
    """
    API configuration class.

    Attributes
    ----------
    url : str
        Url used to interact with the API.
    api_key : str
        The key used to connect to the API.
    method : str
        An API method used to retrieve the required data.
    """

    url: str
    api_key: str
    method: str

    @staticmethod
    def from_env(env: Env):
        """
        Creates the ApiConfig object from environment variables.
        """

        url = env.str("API_URL")
        api_key = env.str("API_KEY")
        method = env.str("API_METHOD")
        
        return ApiConfig(url=url, api_key=api_key, method=method)


@dataclass
class Miscellaneous:
    """
    Miscellaneous configuration class.

    This class holds settings for various other parameters.
    It merely serves as a placeholder for settings that are not part of other categories.

    Attributes
    ----------
    other_params : str, optional
        A string used to hold other various parameters as required (default is None).
    """

    other_params: Optional[str] = None


@dataclass
class Config:
    """
    The main configuration class that integrates all the other configuration classes.

    This class holds the other configuration classes, providing a centralized point of access for all settings.

    Attributes
    ----------
    tg_bot : TgBot
        Holds the settings related to the Telegram Bot.
    api : ApiConfig
        Hold the settings related to the API.
    misc : Miscellaneous
        Holds the values for miscellaneous settings.
    """

    tg_bot: TgBot
    api: ApiConfig
    misc: Miscellaneous


def load_config(path: str) -> Config:
    """
    This function takes an optional file path as input and returns a Config object.
    :param path: The path of env file from where to load the configuration variables.
    It reads environment variables from a .env file if provided, else from the process environment.
    :return: Config object with attributes set as per environment variables.
    """

    # Create an Env object.
    # The Env object will be used to read environment variables.
    env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot.from_env(env),
        api=ApiConfig.from_env(env),
        misc=Miscellaneous(),
    )
