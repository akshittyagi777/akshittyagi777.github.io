<svelte:head>
	<title>Akshit Tyagi</title>
	<meta name="description" content="Founding Member of Technical Staff at Axiom, building foundation models for biology, autonomy and healthcare." />
</svelte:head>

<main>
	<div class="container">
		<header>
			<div class="header-content">
				<div class="profile-photo">
					<img src="/images/fp2.jpg" alt="Akshit Tyagi" />
				</div>
				<div class="header-text">
					<h1>Akshit Tyagi</h1>
					<p class="subtitle">Founding Member of Technical Staff @ Axiom</p>
					<p class="tagline">Foundation Models for Biology, Autonomy &amp; Healthcare</p>
				</div>
			</div>
		</header>

		<section class="about">
			<p>
				I am a Founding Member of Technical Staff at Axiom, where I build foundation models for
				biology, autonomy and healthcare — cellular phenotyping and drug discovery in particular.
				I completed my MS in Computer Science at UMass Amherst (CICS) and my undergraduate
				degree at IIT Delhi, where I focused on theoretical machine learning and natural
				language processing.
			</p>

			<p>
				Most recently I have been using high-content microscopy images to learn what toxic
				presentations in cells look like, and using those learned representations to predict toxic
				structures in drug molecules. More broadly, I am interested in multimodal models for
				biology, and in the calibration and robustness of models used for high-stakes decisions.
			</p>
		</section>

		<section class="experience">
			<h2>Experience</h2>
			
			<div class="timeline-item">
				<div class="timeline-header">
					<h3>Founding Member of Technical Staff</h3>
					<span class="company">Axiom</span>
					<span class="period">Jan 2025 - Present</span>
				</div>
				<p>Foundation models for cellular phenotyping and drug discovery.</p>
				<ul>
					<li>Developed segmentation models to detect and quantify structural / morphological changes in cells from high-content microscopy imaging</li>
					<li>Built and scaled data pipelines processing billions of cell images for large-scale model training and inference</li>
					<li>Used cell images to learn representations of toxic presentations in cells, and used those representations to predict toxic structures in drug molecules</li>
					<li>Developing multimodal LLMs to interpret visual changes in cellular morphology and classify drugs by mechanism of action</li>
				</ul>
			</div>

			<div class="timeline-item">
				<div class="timeline-header">
					<h3>Research Engineer</h3>
					<span class="company">Google Health</span>
					<span class="period">2022 - 2024</span>
				</div>
				<p>Built models for EHR data: algorithms to understand a patient's medical condition, models for tabular clinical data, and large language models for doctors' notes.</p>
			</div>

			<div class="timeline-item">
				<div class="timeline-header">
					<h3>MS Computer Science</h3>
					<span class="company">UMass Amherst (CICS)</span>
					<span class="period">2018 - 2020</span>
				</div>
				<p>Specialized in theoretical machine learning and natural language processing. Research focus on Bayesian calibration, optimization algorithms, and neural network architectures.</p>
			</div>

			<div class="timeline-item">
				<div class="timeline-header">
					<h3>Bachelor's Degree</h3>
					<span class="company">IIT Delhi</span>
					<span class="period">2014 - 2018</span>
				</div>
				<p>Undergraduate studies with focus on computer science fundamentals and early research in machine learning applications.</p>
			</div>
		</section>

		<section class="projects">
			<h2>Selected Work</h2>
			
			<div class="project-item">
				<h3>Faster Bayesian Parameter Estimation for Neural Networks</h3>
				<p>Working on accelerating MCMC sampling for Bayesian parameter estimation, building on Bayesian dark knowledge to create more robust estimators while maintaining inference speed.</p>
				<span class="project-type">Research • Bayesian Learning, MCMC</span>
			</div>

			<div class="project-item">
				<h3>Causal Inference for Medical Diagnosis</h3>
				<p>Building hierarchical Bayesian diagnostic models for the MIMIC dataset, formalizing medical diagnosis as a causal inference problem.</p>
				<span class="project-type">Research • Healthcare AI, Causal Inference</span>
			</div>

			<div class="project-item">
				<h3>Natural Language Understanding for Alexa</h3>
				<p>Developed fast intent classification system with early exit strategy for Alexa's voice assistant, published at ICASSP 2020.</p>
				<span class="project-type">Industry • Amazon Alexa, NLP</span>
			</div>

			<div class="project-item">
				<h3>Robust Question Answering</h3>
				<p>Enhanced noise robustness in conversational Q&A models using transformers, working with Alexa's Implicit Memory team on speech recognition challenges.</p>
				<span class="project-type">Industry • Amazon Alexa, Robustness</span>
			</div>
		</section>

		<section class="links">
			<h2>Links</h2>
			<ul>
				<li><a href="/files/cvLatest.pdf" target="_blank">Resume</a></li>
				<li><a href="mailto:akshitt795@gmail.com">Email</a></li>
				<li><a href="https://linkedin.com/in/akshittyagi" target="_blank">LinkedIn</a></li>
				<li><a href="https://github.com/akshittyagi777" target="_blank">GitHub</a></li>
			</ul>
		</section>
	</div>
</main>

<style>
	:global(body) {
		font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
		line-height: 1.6;
		color: #333;
		background: #fff;
		margin: 0;
		padding: 0;
	}

	:global(*) {
		box-sizing: border-box;
	}

	main {
		min-height: 100vh;
		padding: 2rem 1rem;
	}

	.container {
		max-width: 700px;
		margin: 0 auto;
	}

	header {
		margin-bottom: 3rem;
	}

	.header-content {
		display: flex;
		align-items: center;
		gap: 2rem;
	}

	.profile-photo {
		flex-shrink: 0;
	}

	.profile-photo img {
		width: 120px;
		height: 120px;
		border-radius: 50%;
		object-fit: cover;
		object-position: 50% 30%;
		border: 3px solid #f0f0f0;
	}

	.header-text {
		flex: 1;
	}

	h1 {
		font-size: 2.5rem;
		font-weight: 600;
		margin: 0 0 0.5rem 0;
		color: #000;
	}

	.subtitle {
		font-size: 1.1rem;
		color: #666;
		margin: 0 0 0.25rem 0;
	}

	.tagline {
		font-size: 0.95rem;
		color: #888;
		margin: 0 0 1rem 0;
	}

	section {
		margin-bottom: 3rem;
	}

	h2 {
		font-size: 1.3rem;
		font-weight: 600;
		margin: 0 0 1.5rem 0;
		color: #000;
	}

	h3 {
		font-size: 1.1rem;
		font-weight: 600;
		margin: 0;
		color: #000;
	}

	.about p {
		margin-bottom: 1.5rem;
		color: #333;
	}

	.timeline-item {
		margin-bottom: 2.5rem;
	}

	.timeline-header {
		margin-bottom: 0.8rem;
	}

	.company {
		color: #666;
		font-weight: 500;
		margin: 0 1rem;
	}

	.period {
		color: #999;
		font-size: 0.9rem;
	}

	.timeline-item p {
		color: #555;
		margin: 0;
	}

	.timeline-item ul {
		color: #555;
		margin: 0.6rem 0 0 1.1rem;
		padding: 0;
	}

	.timeline-item li {
		margin-bottom: 0.4rem;
	}

	.links ul {
		list-style: none;
		padding: 0;
		margin: 0;
	}

	.links li {
		margin-bottom: 0.8rem;
	}

	.links a {
		color: #0066cc;
		text-decoration: none;
		font-weight: 500;
	}

	.links a:hover {
		text-decoration: underline;
	}

	.project-item {
		margin-bottom: 2.5rem;
		padding-bottom: 2rem;
		border-bottom: 1px solid #eee;
	}

	.project-item:last-child {
		border-bottom: none;
		padding-bottom: 0;
	}

	.project-item h3 {
		margin-bottom: 0.8rem;
	}

	.project-item p {
		color: #555;
		margin-bottom: 0.8rem;
	}

	.project-type {
		color: #999;
		font-size: 0.9rem;
		font-style: italic;
	}

	@media (max-width: 600px) {
		main {
			padding: 1.5rem 1rem;
		}

		.header-content {
			flex-direction: column;
			text-align: center;
			gap: 1.5rem;
		}

		.profile-photo img {
			width: 100px;
			height: 100px;
		}

		h1 {
			font-size: 2rem;
		}

		.timeline-header {
			flex-direction: column;
			align-items: flex-start;
		}

		.company {
			margin: 0;
		}
	}
</style>