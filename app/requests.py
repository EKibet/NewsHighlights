import urllib.request,json
from .models import Source

#defining the API keys
api_key = None
base_url = None
article_url = None

def configure_request(app):
    global api_key,base_url,article_url,topheadline_url,everything_url,search_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config["SOURCE_API_BASE_URL"]


