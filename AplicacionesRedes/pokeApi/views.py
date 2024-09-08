# poke_api/views.py
from django.shortcuts import render
import requests

def inicio(request):
    return render(request, 'pokeApi/inicio.html')

def pokemon_search(request):
    pokemon_data = None
    if 'name' in request.GET:
        pokemon_name = request.GET['name'].lower()
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}', timeout=5)  # Timeout de 5 segundos
        if response.status_code == 200:
            pokemon_data = response.json()
            print(pokemon_data)

    return render(request, 'pokeApi/buscarPoke.html', {'pokemon_data': pokemon_data})
