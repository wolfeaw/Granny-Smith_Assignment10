# main.py
# Name: Connor Thomas
# Email: thoma5cg@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date: 4/10/2025
# Course #/Section: IS4010/002
# Semester/Year: 2nd/4th
# Brief description of the assignment: Execute an API call using a URL
# Brief description of what this module does: Fetches the Pokemon data
# Citations:
# Anything else that's relevant:

from api_package.api_handler import PokemonAPI
def main():
    pokemons = ["igglybuff", "jigglypuff", "wigglytuff"]
    api = PokemonAPI()
    results = []
    for name in pokemons:
        try:
            data = api.get_pokemon_data(name)
            print(f"{data['name'].capitalize()} | Height: {data['height']} | Weight: {data['weight']} | "
                  f"XP: {data['base_experience']} | Types: {', '.join(data['types'])}")
            results.append(data)
        except Exception as e:
            print(f"Error fetching data for {name}: {e}")
    api.save_to_csv(results)
if __name__ == "__main__":
    main()