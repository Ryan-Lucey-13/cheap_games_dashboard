import requests
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # This is similar to ones we have done before. Instead of keeping
    # the HTML / template in a separate directory, we just reply with
    # the HTML embedded here.
    return HttpResponse('''
        <h1>Welcome to my home page!</h1>
        <a href="/cities">Cities</a> <br />
        <a href="/companies">Companies</a> <br />
    ''')


def city_bikes(request):
    response = requests.get('http://api.citybik.es/v2/networks')
    bikes_data = response.json()
    
    results_list = bikes_data['networks']
    
    context = {
        'city_results': results_list
    }

    return render(request,'cities.html', context)


def bike_companies(request):
    # We can also combine Django with APIs
    response = requests.get('http://api.citybik.es/v2/networks')
    bikes_data = response.json()
    
    results_list = bikes_data['networks']
    
    company_list = []
    for result in results_list:
        if 'company' in result and result['company']:
            company = result['company'][0]
            if company not in company_list:
                company_list.append(company)

    context = {
        'company_results': company_list
    }
    
    return render(request,'companies.html', context)

