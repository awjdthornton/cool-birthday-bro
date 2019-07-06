import requests
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # This is similar to ones we have done before. Instead of keeping
    # the HTML / template in a separate directory, we just reply with
    # the HTML embedded here.
    return HttpResponse('''
        <h1>Welcome to my home page!</h1>
        <a href="/about-me">About me</a> <br />
        <a href="/github-api-example">See my GitHub contributions</a> <br />
        <a href="/date-trivia">Birthday Trivia</a> <br />
    ''')
    
def date_trivia(request):
	month = input('What is your birth month (i.e. 1 - 12)? ')
	day = input('What is your birth day (i.e. 1 - 31)? ')
	response = requests.get('http://numbersapi.com/' + month + '/' + day + '/date'
	data = response.json()
	print(data)
	return HttpResponse('''
		<h1>Welcome to Birthday Trivia</h1>
		<p>''' + data + '</p> <br />')


def about_me(request):
    # Django comes with a "shortcut" function called "render", that
    # lets us read in HTML template files in separate directories to
    # keep our code better organized.
    context = {
        'name': 'Ash Ketchum',
        'pokemon': 'Pikachu',
    }
    return render(request, 'about_me.html', context)


def github_api_example(request):
    # We can also combine Django with APIs
    response = requests.get('https://api.github.com/users/michaelpb/repos')
    repos = response.json()
    context = {
        'github_repos': repos,
    }
    return render(request, 'github.html', context)

