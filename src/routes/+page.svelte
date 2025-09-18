<script>
	import Hero from '$lib/Hero.svelte';
	import Summary from '$lib/Summary.svelte';
	import Projects from '$lib/Projects.svelte';
	import OtherProjects from '$lib/OtherProjects.svelte';
	import Teaching from '$lib/Teaching.svelte';
</script>

<svelte:head>
	<title>Akshit Tyagi - ML Engineer</title>
	<meta name="description" content="ML Engineer at Google Research working on healthcare applications. MS CS from UMass Amherst." />
</svelte:head>

<main>
	<Hero />
	<Summary />
	<Projects />
	<OtherProjects />
	<Teaching />
</main>

<style>
	main {
		min-height: 100vh;
	}
</style>