## Railway Support Engineer project

"Create a GitHub issues renderer."

The task is to create a web app that displays issues from a given repo.

## Getting Started

To run locally:

Install dependencies with `poetry update`. Put your Github API token in a `.env` file. Then run the app with `poetry run flask run`


## Dependencies

To access the Github API, use a [Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)
Set the environment variable `GH_API_TOKEN`, either in your deployment or in a `.env` file.

Packages and tools are managed with [Poetry](https://python-poetry.org/). 

`poetry update`  in this directory to create a working environment.

For simplicity, use good ole [Flask](https://flask.palletsprojects.com) to get the data and render it into an HTML template.
(Alternatives might be Quart or FastAPI, depending on the other needs of the web app...or Django, if a database is needed.)

For fun, use the [Simple GraphQL Client](https://github.com/profusion/sgqlc) to generate a local Python module based on Github's GraphQL schema. We could just write the GraphQL queries ourselves, and that might be better if other people will want to update the queries later without having to think about Python or the SGQLC. But having the schema for free is nice. 

For clarity, use the code formatter [blue](https://blue.readthedocs.io/en/latest/index.html). Python should be pretty! And easy to understand.

## Future possibilties

- Fancier front-end
    - Drop-down list of repos
    - Preview cards instead of list of titles
- Does any data need to be stored? Connect issues to tasks?
