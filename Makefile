.PHONY: \
	build \
	clean \
	test \
	preview \
	pip \

build: games.ndjson players.json
	mkdir -p out
	cp index.html out/index.html
	python test_build.py

games.ndjson:
	wget -O games.ndjson 'https://actionfps.com/all/games.ndjson?since=2017'

players.json:
	wget -O players.json 'https://actionfps.com/players/?format=json'

test:
	python -m pytest

clean:
	rm -rf out
	rm -f games.ndjson

preview: build
	cd out && python -m SimpleHTTPServer

pip:
	python -m pip install -r requirements.txt
