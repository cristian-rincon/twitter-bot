import os
import logging
from enum import Enum

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')
logger = logging.getLogger('Bot Logger')


SAMPLE_WORDS = ['DevOps', 'GCP', 'Kubernetes',
                'CloudOps', 'GitOps', 'Jupyter Notebooks', 'Artificial Intelligence']


class Config(Enum):
    API_KEY = os.getenv('API_KEY')
    API_SECRET_KEY = os.getenv('API_SECRET_KEY')
    ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
    ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
    WORDS_TO_SEARCH = os.getenv('WORDS_TO_SEARCH', SAMPLE_WORDS)
