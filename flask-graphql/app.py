from os import getenv

from dotenv import load_dotenv

from flask import Flask, request, render_template

# Used to hit the Rest Api directly.
# Instead, we're now using sgqlc to hit the GraphQL Api
# import requests

from sgqlc.operation import Operation
from sgqlc.endpoint.requests import RequestsEndpoint

from ghschema import ghschema

load_dotenv()
ITEMS_PER_REQUEST = 30

app = Flask(__name__)


@app.route('/', defaults={'owner': 'sveltejs', 'name': 'kit'})
@app.route('/<owner>/<name>')
def gh_issues(owner, name):
    GH_API_TOKEN = getenv('GH_API_TOKEN')
    if not GH_API_TOKEN:
        print('No Github API token')
        return f'<h1>Unable to access Github {owner}/{name}. No GH API token.</h1>'

    op = Operation(ghschema.Query)
    if 'cursor' in request.args:
        if 'prev' in request.args:
            # is there a smarter way to tell that the user wants to go back?
            issues = op.repository(owner=owner, name=name).issues(
                last=ITEMS_PER_REQUEST, before=request.args['cursor']
            )
        else:
            issues = op.repository(owner=owner, name=name).issues(
                first=ITEMS_PER_REQUEST, after=request.args['cursor']
            )
    else:
        issues = op.repository(owner=owner, name=name).issues(
            first=ITEMS_PER_REQUEST
        )

    issues.nodes.number()
    issues.nodes.title()
    issues.nodes.url()
    # selection pagination data
    issues.page_info.__fields__('has_next_page', 'has_previous_page')
    issues.page_info.__fields__(end_cursor=True, start_cursor=True)
    """
    Debug output of the GraphQL query should look something like
    issues(last: 30, before: "Y3Vyc29yOnYyOpHOMOLJJg==") {
        nodes {
            number
            title
            url
        }
        pageInfo {
            hasNextPage
            hasPreviousPage
            endCursor
            startCursor
        }
    }
    """
    print(issues)

    # Call the endpoint
    headers = {
        'Authorization': f'Bearer {GH_API_TOKEN}',
        'Accept': 'application/vnd.github+json',
    }

    try:
        endpoint = RequestsEndpoint('https://api.github.com/graphql', headers)
        data = endpoint(op)

        # convert to Python objects
        repo = (op + data).repository

        return render_template(
            'issues.html',
            owner=owner,
            repo=name,
            issues=repo.issues.nodes,
            page_info=repo.issues.page_info,
        )
    except:
        return f'<h1>Unable to access Github {owner}/{name}: {[error["message"] for error in data["errors"]]}</h1>'

    # Rest Api (earlier iteration. Now using GraphQL)
    #    gh_issues_req = requests.get(
    #        f'https://api.github.com/repos/{owner}/{name}/issues',
    #        headers={
    #            'Authorization': f'Bearer {GH_API_TOKEN}',
    #            'Accept': 'application/vnd.github+json',
    #        },
    #    )
