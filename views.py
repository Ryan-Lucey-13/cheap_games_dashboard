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
    
    results_list = games_data

    bar_chart = pygal.HorizontalBar()
    bar_chart.title = "Savings Breakdown Per Game"
    bar_chart.add('IE', 19.5)
    bar_chart.add('Firefox', 36.6)
    bar_chart.add('Chrome', 36.3)
    bar_chart.add('Safari', 4.5)
    bar_chart.add('Opera', 2.3)

    chart_svg = bar_chart.render_data_uri()
    
    context = {
        'rendered_chart_svg': chart_svg
    }

    return render(request,'pricing.html', context)

def game_ratings(request):
    response = requests.get('https://www.cheapshark.com/api/1.0/deals?storeID=1&upperPrice=25')
    games_data = response.json()
    
    results_list = games_data
    
    context = {
        'ratings_results': results_list
    }

    return render(request,'ratings.html', context)
    

