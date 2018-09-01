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
    article_url = app.config['ARTICLES_BASE_URL']


def get_source(category):
    '''
    Function that gets the json response to our url request
    '''
    get_newsource_url = base_url.format(category,api_key)


    with urllib.request.urlopen(get_newsource_url) as url:
        get_newsource_data = url.read()
        get_newsource_response = json.loads(get_newsource_data)

        newsource_results = None

        if get_newsource_response['sources']:
            newsource_results_list = get_newsource_response['sources']
            newsource_results = process_results(newsource_results_list)

    return newsource_results


