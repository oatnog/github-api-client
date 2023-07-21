# Railway Support Engineer Project

"Create a GitHub issues renderer."

The task is to create a web app that displays issues from a given repo.

https://svelte-github-issues-renderer-production.up.railway.app/

## Svelte Tells Me

> To deploy your app, you may need to install an [adapter](https://kit.svelte.dev/docs/adapters) for your target environment.

True on Railway. `adapter-node` works--`pnpm build`, then `node build` as the start command.

Railway needed me to supply the start command (I think it defaults to a `start` script in `package.json`, which is sensible, but is not there for Sveltekit/Vite.)

## Notes

- added @octokit/core. This gets types and code completion, which just hitting the Rest endpoints directly would not. Probably more, too. Why not use the tools if they are there, especially if they are first-party.
- Had to set version of Node, since the default is v16 rather than the current LTS v18. The docs say to use an env var or a `package.json` setting. This makes me think of how developers would specify their toolchain. Perhaps an `.npmrc` file? What is the most common way to specify this? I was using volta. Maybe a nixpack enhancement?
- Otherwise very simple (easier to deploy than the Flask version!)
- I found myself moving back and forth between the command line and the UI to do things like set options and environment vars. Is there a clean way to keep everything in sync--perhaps the cli lets you export a `railway.toml` or similar?

## TODO: future possibilities

- Let the user type in the Github org/owner, and read in all repos to a drop-down select input
- Let the user log in to Github and use THEIR credentials?
- Include different views of issue list
    - cards with summaries/status/assignee, like kanban? (easy to do with Tailwind)
- Infinite scroll instead of prev/next buttons.
    - not hard to roll my own?
    - or could use an existing libray https://github.com/andrelmlins/svelte-infinite-scroll
