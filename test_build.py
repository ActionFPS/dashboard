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

def convert_monitor(monitor):
    import datetime
    import json
    for log in monitor['monitors'][0]['logs']:
        if log['type'] == 1:
            yield {'when': datetime.datetime.utcfromtimestamp(log['datetime']).strftime('%Y-%m-%d %H:%M:%S'),
            'duration': str(datetime.timedelta(seconds = log['duration']))}

def build_monitor():
    with open('pub-monitor.json') as f:
        with open('out/monitor.json', 'w') as fg:
            fg.write(json.dumps(list(convert_monitor(json.loads(f.read())))))

if __name__ == '__main__':
    try:
        mkdir('out')
    except:
        pass
    build_json()
    build_players_json()
    build_monitor()

def test_players():
    assert dict(count_players(json.loads('[{"registrationDate": "2015-01-14T11:25:17Z"}]'))) == {'2015-01-01': 1}

def test_monitor():
    text = '{"monitors":[{"logs":[{"type":1,"datetime":1470592446,"duration":858}]}]}'
    assert list(convert_monitor(json.loads(text))) == [
        {'duration': '0:14:18', 'when': '2016-08-07 17:54:06'}
    ]
