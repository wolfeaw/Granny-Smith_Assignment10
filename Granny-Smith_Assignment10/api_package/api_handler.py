# File Name : api_handler.py
# Student Name: Drew Wolfe
# email:  wolfeaw@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date:   4/10/2025
# Course #/Section:   4010-002
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  Uses API URL to pull data from somewhere
# Brief Description of what this module does. Uses Pokemon API specifically to grab information about Pokemon
# Citations: JSON-1.pptx, https://www.geeksforgeeks.org/saving-a-pandas-dataframe-as-a-csv/, https://pokeapi.co/
# Anything else that's relevant:


import requests
import json
import csv

class PokemonAPI:
   
    def __init__(self, base_url="https://pokeapi.co/api/v2/pokemon/"):
        """
        Initializes the PokemonAPI class with the specified API endpoint
        @param base_url String: The base URL for the PokeAPI endpoint
        """
        self.base_url = base_url

    def get_pokemon_data(self, name):
        """
        Fetches Pokemon data by name
        @param name String: The name of the Pokemon
        @returns dict: name, height, weight, base_experience, and types
        """
        url = self.base_url + name.lower()
        response = requests.get(url)

        if response.status_code != 200:
            raise Exception(f"API request failed with status code {response.status_code}")
        data = response.json()
        return {
            "name": data["name"],
            "height": data["height"],
            "weight": data["weight"],
            "base_experience": data["base_experience"],
            "types": [t["type"]["name"] for t in data["types"]],
        }

    def save_to_csv(self, pokemon_list, filename="pokemon_data.csv"):
        """
        Writes a list of Pokemon data dictionaries to a CSV file
        @param pokemon_list List: A list of dictionaries, each representing Pokemon data
        @param filename String: The name of the CSV file to write to. Defaults to 'pokemon_data.csv'
        @returns None: Writes data to CSV and does not return a value
        """
        with open(filename, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "height", "weight", "base_experience", "types"])
            writer.writeheader()
            for poke in pokemon_list:
                writer.writerow({
                    "name": poke["name"],
                    "height": poke["height"],
                    "weight": poke["weight"],
                    "base_experience": poke["base_experience"],
                    "types": ", ".join(poke["types"])
                })
