# File Name : api_handler.py
# Student Name: Drew Wolfe
# email:  wolfeaw@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date:   4/10/2025
# Course #/Section:  IS4010-002
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  Uses an API to display data and writes it to a CSV file
# Brief Description of what this module does: Uses the API to fetch data
# Citations: Module 11, JSON.pptx
# Anything else that's relevant:

import json
import requests

class Pokemon():
    def get_posts():
        url = 'https://pokeapi.co/api/v2/pokemon/jigglypuff'
        try:
            response = requests.get(url)

        if response.status_code == 200:
            posts = response.json()
            return posts
        else:
            print('Error:', response.status_code)
            return None
        except requests.exceptions.RequestException as e:
        print('Error:', e)
            return None