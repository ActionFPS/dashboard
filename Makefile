.PHONY: \
	build \
	clean \
	test \
	preview \
	pip \

TARGET = .
export GAMES_NDJSON = $(TARGET)/games.ndjson
export PLAYERS_JSON = $(TARGET)/players.json
export PUB_MONITOR_JSON = $(TARGET)/pub-monitor.json
export MONITOR_API_KEY = m778017233-4e4ee163a27dda0f894c5932

build: \
	$(GAMES_NDJSON) \
	$(PUB_MONITOR_JSON) \
	$(PLAYERS_JSON) \

	mkdir -p out
	cp index.html out/index.html
	python test_build.py

$(PUB_MONITOR_JSON):
	curl -X POST -H "Content-Type: application/x-www-form-urlencoded" \
		-H "Cache-Control: no-cache" \
		-d 'api_key=$(MONITOR_API_KEY)&format=json&logs=1' \
		-o $(PUB_MONITOR_JSON) \
		"https://api.uptimerobot.com/v2/getMonitors"

$(GAMES_NDJSON):
	wget -O $(GAMES_NDJSON) 'https://actionfps.com/all/games.ndjson'

$(PLAYERS_JSON):
	wget -O $(PLAYERS_JSON) 'https://actionfps.com/players/?format=json'

test:
	python -m pytest

clean:
	rm -rf out
	rm -rf $(GAMES_NDJSON) $(PUB_MONITOR_JSON)

preview: build
	cd out && python -m SimpleHTTPServer

pip:
	python -m pip install -r requirements.txt
