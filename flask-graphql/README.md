## Railway Support Engineer project

"Create a GitHub issues renderer."

The task is to create a web app that displays issues from a given repo.

## Getting Started

To run locally:

Install dependencies with `poetry update`. Put your Github API token in a `.env` file. Then run the app with `poetry run flask run`

View results at http://127.0.0.1:5000. Another org and repo can be specified like this:
railwayapp/nixpacks

## Dependencies

To access the Github API, use a [Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)
Set the environment variable `GH_API_TOKEN`, either in your deployment or in a `.env` file.

Packages and tools are managed with [Poetry](https://python-poetry.org/). 

`poetry update`  in this directory to create a working environment.

For simplicity, use good ole [Flask](https://flask.palletsprojects.com) to get the data and render it into an HTML template.
(Alternatives might be Quart or FastAPI, depending on the other needs of the web app...or Django, or a Flask plugin, if a database is needed.)

For fun, use the [Simple GraphQL Client](https://github.com/profusion/sgqlc) to generate a local Python module based on Github's GraphQL schema. We could just write the GraphQL queries ourselves, and that might be better if other people will want to update the queries later without having to think about Python or the SGQLC. But having the schema for free is nice. 

For clarity, use the code formatter [blue](https://blue.readthedocs.io/en/latest/index.html). Python should be pretty! And easy to understand.

## Future possibilties

- Fancier front-end
    - Drop-down list of repos
    - Preview cards instead of list of titles
    - Descending vs ascending order
    - Search/filter?
- Choice to select closed issues too? 
- Does any data need to be stored? Connect issues to tasks?

## Stumbling blocks

- Deploying to Railway: Poetry wanted to create a packages based on this line in `pyproject.toml` : `packages = [{include = "flask_graphql"}]`

Solution was to either remove that line or add `--no-root` to Dockerfile's `poetry install` line. Is there a way to overrride the nixpack builder to do this too?

- Eventually got nixpacks and deployment working by
    - exporting Poetry config to `requirements.txt` file
    - [overrode default nixpack Python version](https://nixpacks.com/docs/providers/python#setup) with `runtime.txt` file, from 3.10 to 3.11.
    - adding a PORT variable. Could this be detected? Default 5000?
    - adding [custom Start Command](https://docs.railway.app/deploy/deployments#start-command) to railway.toml, running gunicorn. This also deals with assumptions that the entrypoint is named `main.py`
    - Having different requirements for local dev (blue) vs prod (gunicorn) is a good use case for a more advanced package manager than pip, so it would be great if those were working smoothly. [Rye](https://rye-up.com/)?

- Secrets management requires creating a third-party account, per https://docs.railway.app/deploy/integrations#secrets-management

How many developers will skip this step?

On the other hand, the service they indicate is free and very easy to use.
