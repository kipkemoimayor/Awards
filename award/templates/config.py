import os
class Config:
    # https://newsapi.org/v2/top-headlines?country=us&apiKey=2c90171bfd444518bc4ebda2e5895ba0
    NEWS_API_BASE_URL="https://newsapi.org/v2/{}?country=us&apiKey={}"
    NEWS_BASE_URL="https://newsapi.org/v2/{}?language=en&apiKey={}"#sources api
    NEWS_ARTICLE_API="https://newsapi.org/v2/top-headlines?sources={}&apiKey={}"
    NEWS_API_KEY=os.environ.get("NEWS_API_KEY")
    SECRET_KEY=os.environ.get("SECRET_KEY")


class ProdConfig(Config):
    pass
class DevConfig(Config):
    DEBUG=True

config_options={
"development":DevConfig,
"production":ProdConfig
}
