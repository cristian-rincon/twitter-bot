
import tweepy
from settings import Config, logger

CONFIG = Config


auth = tweepy.OAuthHandler(
    CONFIG.API_KEY.value, CONFIG.API_SECRET_KEY.value)
auth.set_access_token(CONFIG.ACCESS_TOKEN.value,
                      CONFIG.ACCESS_TOKEN_SECRET.value)
api = tweepy.API(auth, wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)


class TwitterBot():

    def auth(self):
        try:
            api.verify_credentials()
            logger.info('Authentication OK')
        except:
            logger.error('Error during authentication')


if __name__ == '__main__':

    tw_bot = TwitterBot()
    tw_bot.auth()
