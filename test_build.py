import json
from collections import Counter
from os import mkdir

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
        try:
            mkdir('out')
        except:
            pass
        with open('out/chart.json', 'w') as fg:
            fg.write(json.dumps(dict(count(f))))

def test_it():
    lines = ['{"id":"2017-02-03T04"}']
    assert dict(count(lines)) == {'2017-02-03': 1}

if __name__ == '__main__':
    build_json()
