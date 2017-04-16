# ActionFPS dashboard

> Show general summaries of ActionFPS, stuff that does not belong in a "live" environment.

This dashboard runs on [Travis](https://travis-ci.org/ActionFPS/dashboard) either once a day or when it's updated in master branch.

See live: https://actionfps.github.io/dashboard/

# Local run
With [pip](https://en.wikipedia.org/wiki/Pip_(package_manager)) and Python 2.7 installed:

Run `make pip preview` and then go to http://localhost:8000

# Usage

We're using [Google Charts](https://developers.google.com/chart/) and Python for this.

This is supposed to make contributions to ActionFPS easier, as a testing ground if you like.

Pages are hosted using [GitHub Pages](https://pages.github.com/) and built on Travis CI.

The script downloads historical games, and then can do a batch processing on them.

You MAY use another language than Python, so long as it runs and you've documented it!
