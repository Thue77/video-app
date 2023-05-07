from decouple import Config, RepositoryEnv
from functools import lru_cache

from pathlib import Path
import sys
# source folder
src = Path(__file__).parent.parent
sys.path.append(str(src))

# root of project
root = Path(__file__).parent.parent.parent
sys.path.append(str(root))

# env path
env_path = root / ".env"

def get_config(cloud="azure"):
    """Get configuration from .env file or os.environ"""
    if env_path.exists():
        return Config(RepositoryEnv(env_path))
    from decouple import config
    return config


config = get_config()