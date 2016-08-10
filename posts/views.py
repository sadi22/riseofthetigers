from urllib2 import urlopen
from django.http import Http404,HttpResponse
from django.shortcuts import render, get_object_or_404
from flask import json
from .models import Post, Poll


def index(request):
    try:
        post_list = Post.objects.all().filter(featured_post = 'featured')
        post_list2 = Post.objects.all().filter(featured_post = 'not').filter(category_post__cat_name='BCB').reverse()[0]
        post_cat2 = Post.objects.all().filter(featured_post='not').filter(category_post__cat_name='Dhaka Premier League').reverse()[0]
        post_cat3 = Post.objects.all().filter(featured_post='not').filter(category_post__cat_name='Bangladesh').reverse()[0]
        top_post = Post.objects.all().filter(top_news='top')
        poll = Poll.objects.latest('pub_date')

    except Post.DoesNotExist:
        raise Http404("No MyModel matches the given query.")

    # query = request.GET.get("query")
    # if query:
    #     query_set = Post.objects.all().filter(title__icontains=query)
    #     return render(request, 'posts/main.html', {'query_set':query_set})
    # else:
    #     query_set = None

    breaking_news = "http://caprodseacs03.cloudapp.net/news/popular?limit=5"
    response = urlopen(breaking_news)
    data = json.loads(response.read())
    breaking_news = data['newsArticles']

    url_live = "http://caprodseacs03.cloudapp.net/matches?completedLimit=0&upcomingLimit=0"
    url_complete = "http://caprodseacs03.cloudapp.net/matches?completedLimit=4&inProgressLimit=4&upcomingLimit=0&format=json"
    url_upcomming = "http://caprodseacs03.cloudapp.net/matches?completedLimit=0&inProgressLimit=0&upcomingLimit=6"

# live matches list
    response = urlopen(url_live)
    data = json.loads(response.read())
    live_matches = data['matchList']['matches']

# complte matches list
    response = urlopen(url_complete)
    data = json.loads(response.read())
    complete_matches = data['matchList']['matches']

# upcomming matches list
    response = urlopen(url_upcomming)
    data = json.loads(response.read())
    upcoming_matches = data['matchList']['matches']
    context = {
        'post_list': post_list,
        'post_list2': post_list2,
        'post_cat2':post_cat2,
        'post_cat3': post_cat3,
        'breaking_news': breaking_news,
        'live_matches': live_matches,
        'upcoming_matches': upcoming_matches,
        'complete_matches': complete_matches,
        'poll': poll,
        'top': top_post,
        # 'query_set': query_set,

    }
    return render(request, 'posts/main.html', context)


def score(request, series_id=None, match_id=None):

    breaking_news = "http://caprodseacs03.cloudapp.net/news/popular?limit=5"
    response = urlopen(breaking_news)
    data = json.loads(response.read())
    breaking_news = data['newsArticles']

    team_info = 'http://caprodseacs03.cloudapp.net/matches/%s/%s/detail?format=json' % (series_id, match_id)
    response = urlopen(team_info)
    data = json.loads(response.read())
    match_details = data['matchDetail']

    url = "http://caprodseacs03.cloudapp.net/scorecards/full/%s/%s?format=json" % (series_id, match_id)
    response = urlopen(url)
    data = json.loads(response.read())
    if data:
        scoreCard = data['fullScorecard']['innings']
    else:
        scoreCard = None
    context={
        'breaking_news': breaking_news,
        'match_details': match_details,
        'series_id': series_id,
        'match_id': match_id,
        'score_card': scoreCard,
    }
    print scoreCard
    return render(request, 'posts/score.html', context)

def article(request, slug=None):
    post_detail = get_object_or_404(Post, slug=slug)
    context= {
        'details': post_detail
    }
    return render(request, 'posts/article.html', context)



def fixtures(request):

    breaking_news = "http://caprodseacs03.cloudapp.net/news/popular?limit=5"
    response = urlopen(breaking_news)
    data = json.loads(response.read())
    breaking_news = data['newsArticles']

    url_live = "http://caprodseacs03.cloudapp.net/matches?completedLimit=0&upcomingLimit=0"
    url_complete = "http://caprodseacs03.cloudapp.net/matches?completedLimit=4&inProgressLimit=4&upcomingLimit=0&format=json"
    url_upcomming = "http://caprodseacs03.cloudapp.net/matches?completedLimit=0&inProgressLimit=0&upcomingLimit=6"

    # live matches list
    response = urlopen(url_live)
    data = json.loads(response.read())
    live_matches = data['matchList']['matches']

    # complte matches list
    response = urlopen(url_complete)
    data = json.loads(response.read())
    complete_matches = data['matchList']['matches']

    # upcomming matches list
    response = urlopen(url_upcomming)
    data = json.loads(response.read())
    upcoming_matches = data['matchList']['matches']
    context = {

        'breaking_news': breaking_news,
        'live_matches': live_matches,
        'upcoming_matches': upcoming_matches,
        'complete_matches': complete_matches,

    }

    return render(request, 'posts/fixuters.html', context)


def search(request):
    breaking_news = "http://caprodseacs03.cloudapp.net/news/popular?limit=5"
    response = urlopen(breaking_news)
    data = json.loads(response.read())
    breaking_news = data['newsArticles']
    result = ''

    if request.method == 'POST':
        req = request.POST.get("query")
        result = Post.objects.all().filter(title__icontains=req)

    context = {
        'result': result,
        'breaking_news': breaking_news,
    }
    return render(request, 'posts/result.html', context)


def create_post(request):
    if request.method == 'POST':
        li = []
        post_text = request.POST.get('the_poll')
        poll_id = request.POST.get('poll_id')
        selected_choice = Poll.objects.get(pk=poll_id).choice_set.get(pk=post_text)
        selected_choice.votes += 1
        selected_choice.save()
        result = Poll.objects.get(pk=poll_id).choice_set.all()
        total_poll_votes = sum(c.votes for c in result)
        for c in result:
            perchent= float((c.votes*100)/total_poll_votes)
            c.perchant = perchent
            c.save()
            li.append({'choice': c.choice_text, 'vote': c.votes, 'perchent': c.perchant})

        return HttpResponse(
            json.dumps(li),
            content_type="application/json"
        )

    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


