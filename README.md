# Tech notes

- Read questions.txt for questions to the product owner
- Requirements (just requests and pytest) can be installed with Poetry( https://python-poetry.org/docs/ ). 
- Once poetry is installed, run `poetry install` from repository root to install requirements
- Run script with `poetry run python -m src.activity_analyzer.cli ge0ffrey`)
- Run test with `poetry run pytest tests/__init__.py`

# What would I do in the future?

Besides any large-scale changes made to accomodate requirements that come from the answers to questions.txt, here are some tweaks I would make with more time:
- Paginate the result from Github to get up to the max of 300 events instead of just the 100 my script gets
- Finish unit tests; I just prioritized testing for one of the functions, but there are a few others that could use it.
- I would look into a wrapper like https://github.com/PyGithub/PyGithub to use instead of raw requests
