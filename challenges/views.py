from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponsePermanentRedirect
from django.urls import reverse

# Create your views here.
months = ['january','february','march','april','may','june','july','august','september',
          'october','november','december']

monthly_challenges_dict = {i:i for i in months}

def index(request):
    list_items= ''
    months = list(monthly_challenges_dict.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse('month-challenge', args=[])
        list_items += f"<li><a href='{month_path}'>{capitalized_month}</a></li>"
    response_data = f'<ul>{list_items}</ul>'
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    month = list(monthly_challenge_by_number.keys())
    if month>len(months):
        return HttpResponseNotFound('invalid month')
    redirect_month = month[month]
    redirect_path = reverse('month_challenges', args=[redirect_month])
    return HttpResponsePermanentRedirect('/challenges/'+redirect_path)

def monthly_challenges(request, month):
    try:
        challenge_text = monthly_challenges_dict[month-1]
        response_data = f'<>'