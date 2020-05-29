from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from home.models import FeedElement, SearchTag, ImageTags
import requests
import json 
from home.serializers import SearchTagSerializer, FeedElementSerializer
from rest_framework import viewsets

from django.core.exceptions import ObjectDoesNotExist
def api_doc(request):
    return render(request, 'api.html')


def home_feed(request):    
    feed_elements = FeedElement.objects.all().order_by('-views')[:20]
    tags= SearchTag.objects.all().order_by('-frequency')[:4]
    context = {
        'feed_elements' : feed_elements,
        'trendingtags':tags
        }
    return render(request, 'home_feed.html',context)
    
def hsearch(request):
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
    
    #PIXABAY API
    tag=request.GET['query']
    images=[]
    uRL = "https://pixabay.com/api/?key=9779993-a9e224ff337b9580d335e7588&q=" + tag + "&image_type=photo&pretty=true&per_page=200"
    r = requests.get(url = uRL)
    dataP = r.json()
    for i in range(len(dataP["hits"])):
        info={
        	'width':dataP['hits'][i]['imageWidth'],
        	'height':dataP['hits'][i]['imageHeight'],
            'fullimage':dataP['hits'][i]['previewURL'],
            'url':dataP['hits'][i]['previewURL'],
            'title':tag
        }
        images.append(info)    
    
    tags = []
    for s in sr:
        tags.append(s)
        r = requests.get(base_url + '/r/{}/top'.format(s), headers=headers, params=payload)
        js = r.json()

        for i in range(js['data']['dist']):
            if js['data']['children'][i]['data']['thumbnail'] != 'self':
                info={
                      'width':250,
                      'height':250,
                      'fullimage': js['data']['children'][i]['data']['thumbnail'],
                      'url': js['data']['children'][i]['data']['thumbnail'],
                      'title': js['data']['children'][i]['data']['title']
                     }
                images.append(info)
    trendingtags= SearchTag.objects.all().order_by('-frequency')[:4]                
    
    for t in tags:
        try:
            db=SearchTag.objects.get(pk=t)
        except ObjectDoesNotExist as e:
            db=SearchTag(tag=t,frequency=1)
        else:
            db.frequency=db.frequency+1
        finally:
            db.save()

    for image in images:
        try:
            db=FeedElement.objects.get(pk=image['url'])    
        except ObjectDoesNotExist as e:
            
            db=FeedElement(width=image['width'],height=image['height'],imageurl=image['url'],fullimage=image['fullimage'],views=0)
            db.save()
            

        finally:
            image['views']=db.views
            for t in tags:
                try:
                    sub=ImageTags.objects.get(image=db,imgtag=SearchTag.objects.get(pk=t))                
                except ObjectDoesNotExist as e:
                    sub=ImageTags(image=db,imgtag=SearchTag.objects.get(pk=t))
                    sub.save()
                else:
                    pass
    images=sorted(images, key = lambda i: i['views'],reverse=True)
    context={
        'tags':tags,
        'images':images,
        'trendingtags':trendingtags
            }
    
    

            
    return render(request,"searchIndex.html",context)


def update_db(request):
    url = request.GET['url']
    
    try:
        db=FeedElement.objects.get(pk=url)
    except ObjectDoesNotExist as e:
        raise e
    else:
        db.views=db.views+1
        db.save()
    try:
        sub=ImageTags.objects.filter(image=db)
    except ObjectDoesNotExist as e:
        raise e
    trendingtags= SearchTag.objects.all().order_by('-frequency')[:4]
    context={
        'url':db.imageurl,
        'title':sub,
        'trendingtags':trendingtags,
        'views':db.views
    }
    print("$$$"+db.fullimage+"$$$")
    
    return render(request,"postIndex.html",context)


def api(request):
    dataJSON = []
    with open("result.html", "w", encoding='utf-8') as html_page:
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
    with open('hashsearch/templates/response.json', 'w') as f:
        f.write(dJSON)
    return render(request,"response.json")


class tag_list(viewsets.ModelViewSet):
    """
    List all code tags, or create a new tag.
    """
    serializer_class = SearchTagSerializer
    queryset = SearchTag.objects.all() 

class image_list(viewsets.ModelViewSet):
    serializer_class = FeedElementSerializer
    queryset = FeedElement.objects.all() 

    