
# Script para generar usuarios

import requests
from .models import User


def generate_request(url, params={}):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()


def get_user(params={}):
    response = generate_request('https://randomuser.me/api', params)
    if response:
        results = response.get('results')[0]
        context = {
            'gender': results.get('gender'),
            'full_name': results.get('name').get('first') + '' + results.get('name').get('last'),
            'email': results.get('email'),
            'age': results.get('dob').get('age'),
            'city': results.get('location').get('city'),
            'country': results.get('location').get('state'),
            'picture': results.get('picture').get('medium'),
        }
        return context

    return ''


def create_user():
    number_of_users = User.objects.all().count()

    if number_of_users < 100:
        results = get_user()

        for _ in range(98):
            User.objects.create(
                gender = results['gender'],
                full_name = results['full_name'],
                email = results['email'],
                age = results['age'],
                city = results['city'],
                country = results['country'],
                picture = results['picture']
            )
