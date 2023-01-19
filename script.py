import requests

print('\n---------- GAME STARTED ----------\n')
answer = input('Hello!, welcome to the Pokedex. ¿Do you want to ask for a Pokemon? Yes/No\n').lower()

while answer in ['yes','y']:
    try:
        pokemonName = input('\nPlease write a Pokemon name to ask for information:\n').lower()
        request = requests.get('https://pokeapi.co/api/v2/pokemon/' + pokemonName).json()
        
        if type(request) == dict:
            print('\nInformation from ' + pokemonName + ' ...')

            print('- Is type ' + request.get('types')[0].get('type').get('name'))

            print('- Habilities:')
            for ability in request.get('moves'):
                print('  * ' + ability.get('move').get('name'))

            print('- Moves:')
            for move in request.get('moves'):  
                print('  * ' + move.get('move').get('name'))

            print('- It looks this way: ' + request.get('sprites').get('front_default'))

            answer = input('¿Do you want to ask for another Pokemon? Yes/No\n').lower()
    
    except:
        print('\nThe name of the Pokemon is not valid or is not in the database')

print('\nThank you for playing with this Pokedex')
print('\n---------- GAME FINISHED ----------\n')