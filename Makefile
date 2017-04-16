.PHONY: \
	build \
	clean \
	test \
	preview \

build: games.ndjson
	mkdir -p out
	cp index.html out/index.html
	python test_build.py

games.ndjson:
	wget -O games.ndjson 'https://actionfps.com/all/games.ndjson?since=2017'

test:
	python -m pytest

clean:
	rm -r out

preview:
	cd out && python -m SimpleHTTPServer
