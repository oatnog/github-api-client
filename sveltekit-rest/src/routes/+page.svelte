<script lang="ts">
	import type { PageData } from './$types';
	export let data: PageData;

	import {enhance} from '$app/forms';
</script>

<h1>Open Issues</h1>
<!-- <form method="POST" use:enhance>
	<label>
		github.com/
		<input
			name="organization"
			autocomplete="off"
			autocapitalize="off"
			value="sveltejs"
		/>
	</label>
	<select>
		<option>kit</option>
	</select>
</form> -->
<ul>
	{#each data.issues.data as issue}
		<li>{issue.number} <a href={issue.html_url}>{issue.title}</a></li>
	{/each}
</ul>
TODO: Infinite Scroll {data.issues.headers.link}
