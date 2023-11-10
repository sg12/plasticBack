import os
from pathlib import Path
from dotenv import load_dotenv


def load_env():
    path = Path(__file__).resolve().parent.parent.parent
    dotenv_path = os.path.join(path, '.env')
    
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)