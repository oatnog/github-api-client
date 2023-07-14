from flask import Flask, render_template
import requests
from os import getenv


app = Flask(__name__)

@app.route('/')
def gh_issues():
    GH_API_TOKEN = getenv('GH_API_TOKEN')
    OWNER = 'sveltejs'
    REPO = 'kit'
    gh_issues_req = requests.get(
        f'https://api.github.com/repos/{OWNER}/{REPO}/issues',
        headers={
            'Authorization': f'Bearer {GH_API_TOKEN}',
            'Accept': 'application/vnd.github+json',
        }
    )
    
    print(gh_issues_req)
    
    return render_template('issues.html', owner=OWNER,  repo=REPO, issues=gh_issues_req.json())
