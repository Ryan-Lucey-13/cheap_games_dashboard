import requests
import pygal
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # This is similar to ones we have done before. Instead of keeping
    # the HTML / template in a separate directory, we just reply with
    # the HTML embedded here.
    return HttpResponse('''
        <h1>Welcome to my home page!</h1>
        <a href="/table">Games</a> <br />
        <a href="/pricing">Prices</a> <br />
        <a href="/ratings">Ratings</a> <br />
    ''')

    '''
    def game_info(request):
        search_type = request.GET['stype']
        search_query = request.GET['searchterm']

        context = {
            'results_count': 0,
            'search_message': None,
            'search_term': search_query,
            'search_type': search_type,
        }

        if search_type == 'pricesearch'
            context['search_message'] = 'Max Price Range'
            context['results_count'] = 0

            url = 'https://www.cheapshark.com/api/1.0/deals?storeID=1&upperPrice='
            url += search_query
            response = requests.get(url)
            games_data = response.json()  
            results_list = games_data
        else:
            
    '''

def game_info(request):
    response = requests.get('https://www.cheapshark.com/api/1.0/deals?storeID=1&upperPrice=25')
    games_data = response.json()
        
    results_list = games_data

    context = {
        'games_results': results_list
    }

    return render(request,'table.html', context)


def game_discount(request):
    response = requests.get('https://www.cheapshark.com/api/1.0/deals?storeID=1&upperPrice=25')
    games_data = response.json()
    
    bar_chart = pygal.HorizontalBar()
    bar_chart.title = "Savings Breakdown Per Game"
    for game in games_data:
        value = game['releaseDate']
        label = game['title']
        bar_chart.add(label, value)
    '''
    Stacked Bar Chart Code
    for game in games_data:
        value_1 = int(game['salePrice'])
        value_2 = int(game['normalPrice']) - value_1
        label = game['title']
        bar_chart.add(label, value)
    '''
    chart_svg = bar_chart.render_data_uri()
    
    context = {
        'rendered_chart_svg': chart_svg
    }

    return render(request,'pricing.html', context)

def game_ratings(request):
    response = requests.get('https://www.cheapshark.com/api/1.0/deals?storeID=1&upperPrice=25')
    games_data = response.json()
    
    results_list = games_data
    
    
    for game in results_list:
        if game['title'] == "Sid Meiers Civilization VI":
            label = "Sid Meiers Civilization VI"
            meta_rating = 20 #game['metacriticScore']
            steam_rating = 10 #game['steamRatingPercent']
            deal_rating = 15 #game['dealRating'] * 10
    
    bar_chart = pygal.Bar()
    bar_chart.title = 'Game Ratings (out of 100)'
    bar_chart.x_labels = 'MetaCritic Rating', 'Steam Rating', 'Deal Rating'
    bar_chart.add(label, [meta_rating, steam_rating, deal_rating])
    chart_svg = bar_chart.render_data_uri()
    
    context = {
        'rendered_chart_svg': chart_svg
    }

    return render(request,'ratings.html', context)
    

