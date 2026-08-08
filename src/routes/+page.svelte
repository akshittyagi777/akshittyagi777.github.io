<script>
	import Hero from '$lib/Hero.svelte';
	import Summary from '$lib/Summary.svelte';
	import Experience from '$lib/Experience.svelte';
	import Projects from '$lib/Projects.svelte';
	import OtherProjects from '$lib/OtherProjects.svelte';
	import Skills from '$lib/Skills.svelte';
	import Teaching from '$lib/Teaching.svelte';
</script>

<svelte:head>
	<title>Akshit Tyagi - Founding MTS @ Axiom</title>
	<meta name="description" content="Founding Member of Technical Staff at Axiom, building multimodal foundation models for cellular phenotyping and drug safety. Previously Helm AI and Google DeepMind. MS CS from UMass Amherst, BTech from IIT Delhi." />
</svelte:head>

<main>
	<Hero />
	<Summary />
	<Experience />
	<Projects />
	<Skills />
	<OtherProjects />
	<Teaching />
</main>

<style>
	main {
		min-height: 100vh;
	}
</style>