<script>
	import Hero from '$lib/Hero.svelte';
	import Summary from '$lib/Summary.svelte';
	import Experience from '$lib/Experience.svelte';
	import Projects from '$lib/Projects.svelte';
	import OtherProjects from '$lib/OtherProjects.svelte';
	import Teaching from '$lib/Teaching.svelte';
</script>

<svelte:head>
	<title>Akshit Tyagi - Founding MTS @ Axiom</title>
	<meta name="description" content="Founding Member of Technical Staff at Axiom, working on foundation models for biology, autonomy and healthcare. MS CS from UMass Amherst, BTech from IIT Delhi." />
</svelte:head>

<main>
	<Hero />
	<Summary />
	<Experience />
	<Projects />
	<OtherProjects />
	<Teaching />
</main>

<style>
	main {
		min-height: 100vh;
	}
</style>