from os import getenv

from dotenv import load_dotenv

from flask import Flask, request, render_template
#import requests

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
        return render_template(
            'issues.html',
            owner=owner,
            repo=name,
        )
    #OWNER = 'sveltejs'
    #REPO = 'kit'

    op = Operation(ghschema.Query)
    print(request.args)
    if 'cursor' in request.args:
        if 'prev' in request.args:
            issues = op.repository(owner=owner, name=name).issues(last=ITEMS_PER_REQUEST, before=request.args['cursor'])
        else:
            issues = op.repository(owner=owner, name=name).issues(first=ITEMS_PER_REQUEST, after=request.args['cursor'])
    else:
        issues = op.repository(owner=owner, name=name).issues(first=ITEMS_PER_REQUEST)

    # Call the endpoint
    headers = {
        'Authorization': f'Bearer {GH_API_TOKEN}',
        'Accept': 'application/vnd.github+json',
    }

    issues.nodes.number()
    issues.nodes.title()
    issues.nodes.url()
    # selection pagination data
    issues.page_info.__fields__('has_next_page','has_previous_page')
    issues.page_info.__fields__(end_cursor=True, start_cursor=True)
    # Debug output of the GraphQL query
    print(issues)
    endpoint = RequestsEndpoint('https://api.github.com/graphql', headers)

    data = endpoint(op)

    # convert to Python objects
    repo = (op + data).repository
    #for issue in repo.issues.nodes:
    #    print(issue)

    #print(repo.issues.page_info)

# REST request--let's not use this now
#    gh_issues_req = requests.get(
#        f'https://api.github.com/repos/{owner}/{name}/issues',
#        headers={
#            'Authorization': f'Bearer {GH_API_TOKEN}',
#            'Accept': 'application/vnd.github+json',
#        },
#    )

    return render_template(
        'issues.html',
        owner=owner,
        repo=name,
        issues=repo.issues.nodes,
        page_info=repo.issues.page_info,
    )
