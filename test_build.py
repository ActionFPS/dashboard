import json
from collections import Counter
from os import mkdir

def count_players(j):
    counter = Counter()
    for p in j:
        date = '%s-01' % p['registrationDate'][:7]
        item = {}
        item[date] = 1
        counter.update(item)
    return counter

def count(lines):
    counter = Counter()
    for line in lines:
        date = json.loads(line)['id'][:10]
        item = {}
        item[date] = 1
        counter.update(item)
    return counter

def build_json():
    with open('games.ndjson') as f:
        with open('out/chart.json', 'w') as fg:
            fg.write(json.dumps(dict(count(f))))

def test_it():
    lines = ['{"id":"2017-02-03T04"}']
    assert dict(count(lines)) == {'2017-02-03': 1}

def build_players_json():
    with open('players.json') as f:
        player_counts = count_players(json.loads(f.read()))
        with open('out/players.json', 'w') as fg:
            fg.write(json.dumps(dict(player_counts)))

if __name__ == '__main__':
    try:
        mkdir('out')
    except:
        pass
    build_json()
    build_players_json()

def test_players():
    assert dict(count_players(json.loads('[{"registrationDate": "2015-01-14T11:25:17Z"}]'))) == {'2015-01-01': 1}
