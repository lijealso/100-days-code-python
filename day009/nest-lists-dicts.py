
# Nesting

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

for key in capitals:
    print('The capital of ' + key + ' is: ' + capitals[key])

# nesting a list in a dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# nesting a dictionary in a dictionary

travel_log2 = { 'France': {'cities_visited': ['Paris', 'Lille', 'Dijon'],'total_visits' : 12},
         'Germany': {'cities_visited': ['Berlin', 'Hamburg', 'Stuttgart'], 'total_visits' : 13}
}

# nesting dictionary in a list

travel_log3 = [
    {
        'country' : 'France',
        'cities_visited': ['Paris', 'Lille', 'Dijon'],
        'total_visits' : 12
    },
    {
        'country' : 'Germany',
        'cities_visited': ['Berlin', 'Hamburg', 'Stuttgart'],
        'total_visits' : 13
    },
]