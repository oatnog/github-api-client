<script lang="ts">
	import type { PageData } from './$types';
	export let data: PageData;
</script>

<h1>Welcome to SvelteKit</h1>
<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>

<ul>
	{#each data.issues.data as issue}
		<li><a href={issue.html_url}>{issue.title}</a></li>
	{/each}
</ul>
{data.issues.headers.link}
