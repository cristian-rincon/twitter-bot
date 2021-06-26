
import tweepy
from settings import Config, logger

CONFIG = Config


class TwitterBot():

    def auth(self):
        auth = tweepy.OAuthHandler(
            CONFIG.API_KEY.value, CONFIG.API_SECRET_KEY.value)
        auth.set_access_token(CONFIG.ACCESS_TOKEN.value,
                              CONFIG.ACCESS_TOKEN_SECRET.value)
        api = tweepy.API(auth, wait_on_rate_limit=True,
                         wait_on_rate_limit_notify=True)
        try:
            api.verify_credentials()
            logger.info('Authentication OK')
            return api
        except Exception as e:
            logger.error('Error during authentication', e)
        logger.info('API Created')

    def get_twits(self):
        api = self.auth()
        timeline = api.home_timeline()
        for tweet in timeline:
            print(f'{tweet.user.name} said {tweet.text}')

    def update_status(self, message: str):
        api = self.auth()
        api.update_status(message)


class RetweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        logger.info(f'Processing tweet id {tweet.id}')
        if tweet.in_reply_to_status_id is not None or \
                tweet.user.id == self.me.id:
            # This tweet is a reply or I'm its author so, ignore it
            return
        if not tweet.retweeted:
            # Retweet, since we have not retweeted it yet
            try:
                tweet.retweet()
            except Exception as e:
                logger.error('Error on fav and retweet')
                logger.error(e)

    def on_error(self, status):
        logger.error(status)


def main(keywords: list):
    bot = TwitterBot()
    api = bot.auth()
    # tweets_listener = RetweetListener(api)
    # stream = tweepy.Stream(api.auth, tweets_listener)
    # stream.filter(track=keywords, languages=['en'])
    keywords = keywords.split(',')
    keywords = [f'#{i}' for i in keywords]
    keywords = ''.join(keywords)
    logger.info(f'List of keywords: {keywords}')
    for tweet in tweepy.Cursor(api.search, q=f'{keywords}', rpp=100).items():
        if not tweet.retweeted:
            # Retweet, since we have not retweeted it yet
            try:
                tweet.retweet()
            except Exception as e:
                logger.error('Error on fav and retweet')
                logger.error(e)


if __name__ == '__main__':

    main(CONFIG.WORDS_TO_SEARCH.value)
