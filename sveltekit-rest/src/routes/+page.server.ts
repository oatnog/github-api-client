import { GH_API_TOKEN } from '$env/static/private';
import { Octokit } from '@octokit/core';

const octokit = new Octokit({ auth: GH_API_TOKEN });

const issues = await octokit.request('GET /repos/{owner}/{repo}/issues', {
	owner: 'sveltejs',
	repo: 'kit'
});

//console.log(issues.headers['link'])

// console.log(firstIssues)

export async function load({ params }) {
	return {
		issues: issues /* await octokit.rest.issues.listForRepo({
      owner: 'sveltejs',
      repo : 'kit',
  }) */
	};
}
