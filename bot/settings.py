import logging
from enum import Enum

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logger = logging.getLogger(__name__)


class Config(Enum):
    API_KEY = 'WPrQXCxScKn9Xb4mBYzd6g4Ql'
    API_SECRET_KEY = 'WIjHL3qmQJAx0wfPsCRWX4U61CBudvwRhpGQWo2GVutrTmWPbM'
    BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAE2rQwEAAAAAhuOuGr5HTLJdjXvQ4wgiht%2FqVpI%3DwJVPhVqqFSsMfWZmmxpNs5anlxD0SnWP11wfmvY90gRkt37VkD'
    ACCESS_TOKEN = '277730089-Y6VvsUJV0fPgSa3OKq67EmBbk3olXuG5Gyi6EF2r'
    ACCESS_TOKEN_SECRET = '802swwcVse9zA0VIvR8useb8HP1C34YR0sgoFvFbuqAGt'
