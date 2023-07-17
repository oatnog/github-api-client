import { GH_API_TOKEN, GH_API_TYPE } from '$env/static/private';
import { Octokit } from '@octokit/core';
import { restEndpointMethods, } from '@octokit/plugin-rest-endpoint-methods';
import type { Api } from '@octokit/plugin-rest-endpoint-methods/dist-types/types';

let octokit: Octokit & Api;
let issues; 
if (GH_API_TYPE === "rest") {
  const MyOctokit = Octokit.plugin(restEndpointMethods);
  octokit = new MyOctokit({auth: GH_API_TOKEN});

    const iterator = octokit.paginate.iterators(octokit.rest.issues.listForRepo,
      {
    owner: 'sveltejs',
    repo : 'kit',
})

}

const { lastIssues } = await octokit.graphql(
  `
    query lastIssues($owner: String!, $repo: String!, $num: Int = 3) {
      repository(owner: $owner, name: $repo) {
        issues(last: $num) {
          edges {
            node {
              title
            }
          }
        }
      }
    }
  `,
  {
    owner: "octokit",
    repo: "graphql.js",
  },
);

/* const  firstIssues: {
  organization: { repository: 
    { issues: {
        edges: {
          node: {
            id: any,
            title: any,
            url: any,
          }
        }
      }
    }
  }
}  = await octokit.graphql(
    `
    query firstIssues($org: String!, repo: String!){ 
        organization(login: $org) { 
          repository(name: $repo) {
            issues (last:10){
              edges {
                node {
                  id
                  title
                  url
                }
              }
            }
          }
        }
      }
    `,
    {
        org: "sveltejs",
        repo: "kit",
    }    
) */


//console.log(issues.headers['link'])

// console.log(firstIssues)

export async function load ({ params }) {
  return {
    issues: issues /* await octokit.rest.issues.listForRepo({
      owner: 'sveltejs',
      repo : 'kit',
  }) */
  }
}
