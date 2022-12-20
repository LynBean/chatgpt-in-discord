
from pathlib import Path
import json
import os
import platform

from ._constants import *

class Config:
    """Config class for saving and loading config.json
    """
    def __init__(self):
        self._init_json: dict = INIT_CONFIG
        self.filePath = os.path.join(self.appPath, 'config.json')

        if not os.path.exists(self.filePath):
            self.create()

    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.filePath}>'

    @property
    def appPath(self) -> str:
        """Returns the path to the application directory
        """
        uname = platform.system()
        if uname == 'Windows':
            return os.path.join(os.getenv('APPDATA'), 'Kim', 'chatgpt-in-discord')
        elif uname == 'Linux':
            return os.path.join(os.getenv('HOME'), '.config', 'kim', 'chatgpt-in-discord')
        elif uname == 'Darwin':
            return os.path.join(os.getenv('HOME'), 'Library', 'Application Support', 'kim', 'chatgpt-in-discord')
        else:
            return os.path.join(os.getcwd(), 'Kim', 'chatgpt-in-discord')

    def create(self) -> None:
        """Creates the config.json file
        """
        if not os.path.exists(self.appPath):
            os.makedirs(self.appPath)

        if not os.path.exists(self.filePath):
            Path(self.filePath).touch(exist_ok=True)
            self.write(self._init_json)

    def load(self) -> dict:
        """Loads the config.json file
        """
        with open(self.filePath, 'r') as f:
            return json.load(f)

    def write(self, data: dict):
        """Writes to the config.json file
        """
        with open(self.filePath, 'w') as f:
            json.dump(data, f, indent=4, sort_keys=False)

class Engine(Config):
    """Engine class for saving and loading engines.json
    """
    def __init__(self):
        super().__init__()
        self.filePath = os.path.join(self.appPath, 'engines.json')
