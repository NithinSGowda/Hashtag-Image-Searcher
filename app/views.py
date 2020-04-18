from django.shortcuts import render
import requests
from TwitterSearch import *
import json 
base_url = 'https://www.reddit.com/'
data = {'grant_type': 'password', 'username': 'NithinSGowda', 'password': '88888888'}
auth = requests.auth.HTTPBasicAuth('ZkVr8_6b8Kptrg','tYOsakECdbS2iCy9MISm0oO5TYs')
r = requests.post(base_url + 'api/v1/access_token',
                  data=data,
                  headers={'user-agent': 'APP-NAME by REDDIT-USERNAME'},
		  auth=auth)
d = r.json()

# Create your views here.
def home(request):
    return render(request,"index.html")

def ss(request):
    return render(request,"searchpage/searchIndex.html")

def hsearch(request):
    with open("templates/result.html", "w", encoding='utf-8') as html_page:
        html_page.write(" ")
    import requests
    base_url = 'https://www.reddit.com/'
    data = {'grant_type': 'password', 'username': 'NithinSGowda', 'password': '88888888'}
    auth = requests.auth.HTTPBasicAuth('jnff90cGcDjQkw','8_fNWdChFCoE06ZfKgl46TWRaMc')
    r = requests.post(base_url + 'api/v1/access_token',
                    data=data,
                    headers={'user-agent': 'Hashtag Search'},
            auth=auth)
    d = r.json()
    token = 'bearer ' + d['access_token']
    base_url = 'https://oauth.reddit.com'
    headers = {'Authorization': token, 'User-Agent': 'Hashtag Search'}
    response = requests.get(base_url + '/api/v1/me', headers=headers)
    payload = {'q': request.GET['query'], 'limit': 1, 'sort': 'relevance'}
    response = requests.get(base_url + '/subreddits/search', headers=headers, params=payload)
    values = response.json()
    js = response.json()
    sr = []
    for i in range(js['data']['dist']):
        sr.append(js['data']['children'][i]['data']['display_name'])
    print(sr)
    payload = {'t': 'all'}
    imghtml = ''
    for s in sr:
        imghtml += '<h3 style="clear:both">{}</h3><div>'.format(s)
        r = requests.get(base_url + '/r/{}/top'.format(s), headers=headers, params=payload)
        js = r.json()
        for i in range(js['data']['dist']):
            if js['data']['children'][i]['data']['thumbnail'] != 'self':
                imghtml += '<div class="item" style="display: block;"><a href="{}"><img src="{}" alt="{}"></a><div><a href="{}">{}</a></div></div>'.format(
                    js['data']['children'][i]['data']['url'],
                    js['data']['children'][i]['data']['thumbnail'],
                    js['data']['children'][i]['data']['title'],
                    js['data']['children'][i]['data']['url'],
                    js['data']['children'][i]['data']['title'],
                )
    #PIXABAY
    uRL = "https://pixabay.com/api/?key=9779993-a9e224ff337b9580d335e7588&q=" + request.GET['query'] + "&image_type=photo&pretty=true&per_page=200"
    r = requests.get(url = uRL)
    dataP = r.json()
    for i in range(len(dataP["hits"])):
        imghtml += '<div class="item" style="display: block;"><a href="{}"><img src="{}" alt="{}"></a><div><a href="{}">{}</a></div></div>'.format(
                    dataP['hits'][i]['largeImageURL'],
                    dataP['hits'][i]['previewURL'],
                    dataP['hits'][i]['user'],
                    dataP['hits'][i]['largeImageURL'],
                    request.GET['query'],
                )

    #twitter
    # imghtml = ''
    # try:
    #     tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    #     tso.set_keywords(['Dog']) # let's define all words we would like to have a look for
    #     tso.set_language('en') # we want to see German tweets only
    #     tso.set_include_entities(False) # and don't give us all those entity information

    #     # it's about time to create a TwitterSearch object with our secret tokens
    #     ts = TwitterSearch(
    #         consumer_key = 'gCMpUH2ENFFIYqkDooZA6U3YM',
    #         consumer_secret = '7SdGDDuYtVp2WccLJh6gnA5X048DBHHhjhPAtbPJQnA2Mcwz5Q',
    #         access_token = '904541724214624257-5vv8K0dWsONBnkgE0jAiq994yHkdnwz',
    #         access_token_secret = 'LFHSXLXjPapDR7l3mKtoplTR3gp6MtC3QUZIsda90HErY'
    #     )

    #     # this is where the fun actually starts :)
        
    #     for tweet in ts.search_tweets_iterable(tso):
    #         tresult = json.dumps(tweet)
    #         imghtml+=tresult

    # except TwitterSearchException as e: # take care of all those ugly errors if there are some
    #     print(e)
    with open("templates/result.html", "w", encoding='utf-8') as html_page:
        html_page.write(imghtml)
    return render(request,"searchpage/searchIndex.html",{'result': request.GET['query']})
    #return render(request,"searchpage/searchIndex.html",{'result':request.GET['query']})



def api(request):
    dataJSON = []
    with open("templates/result.html", "w", encoding='utf-8') as html_page:
        html_page.write(" ")
    import requests
    base_url = 'https://www.reddit.com/'
    data = {'grant_type': 'password', 'username': 'NithinSGowda', 'password': '88888888'}
    auth = requests.auth.HTTPBasicAuth('jnff90cGcDjQkw','8_fNWdChFCoE06ZfKgl46TWRaMc')
    r = requests.post(base_url + 'api/v1/access_token',
                    data=data,
                    headers={'user-agent': 'Hashtag Search'},
            auth=auth)
    d = r.json()
    token = 'bearer ' + d['access_token']
    base_url = 'https://oauth.reddit.com'
    headers = {'Authorization': token, 'User-Agent': 'Hashtag Search'}
    response = requests.get(base_url + '/api/v1/me', headers=headers)
    payload = {'q': request.GET['q'], 'limit': 1, 'sort': 'relevance'}
    response = requests.get(base_url + '/subreddits/search', headers=headers, params=payload)
    js = response.json()
    sr = []
    for i in range(js['data']['dist']):
        sr.append(js['data']['children'][i]['data']['display_name'])
    print(sr)
    payload = {'t': 'all'}
    for s in sr:
        r = requests.get(base_url + '/r/{}/top'.format(s), headers=headers, params=payload)
        js = r.json()
        for i in range(js['data']['dist']):
            if js['data']['children'][i]['data']['thumbnail'] != 'self':
                dataJSON.append(js['data']['children'][i]['data']['url'])
    #PIXABAY
    uRL = "https://pixabay.com/api/?key=9779993-a9e224ff337b9580d335e7588&q=" + request.GET['q'] + "&image_type=photo&pretty=true&per_page=200"
    r = requests.get(url = uRL)
    dataP = r.json()
    for i in range(len(dataP["hits"])):
        dataJSON.append(dataP['hits'][i]['largeImageURL'])
    dJSON = json.dumps(dataJSON,indent=4)
    with open('templates/response.json', 'w') as f:
        f.write(dJSON)
    return render(request,"response.json")
