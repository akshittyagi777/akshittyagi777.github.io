<script>
	const projects = [
		{
			org: "Axiom",
			title: "DILI Assay Development & Structure-to-Risk Modeling",
			venue: "Presented at SoT 2025",
			description: "Co-designed the 2D multiplexed cytotoxicity assay with biologists and external labs / CROs — cell-painting imaging plus LDH and MT-Glo readouts across >100,000 molecules profiled in primary human hepatocytes — closing the loop by feeding assay output back through the vision model to surface which phenotypes carry biological signal. Trained models to predict dose-dependent responses for >10 distinct cell stress and death phenotypes directly from SMILES. Fine-tuned a multimodal LLM on cell images together with ADME properties and human exposure data, yielding a clinical DILI risk score benchmarked against 2D HepG2, 2D PHH imaging and 3D spheroid assays.",
			tags: ["Drug Safety", "Multimodal LLMs", "Assay Design", "SMILES"]
		},
		{
			org: "Axiom",
			title: "Cellular Imaging ML Stack",
			description: "Built and operate the imaging stack behind the assay work: microscope-level correction so instrument variation doesn't propagate downstream; a pipeline that auto-ingests and normalises each new batch into a growing 10M+ image corpus, with drift monitoring that alerts the team when incoming data or retrained models move out of tolerance; deep-learning segmentation quantifying vacuoles, cytoplasm, mitochondria and RNA condensates across cell-painting channels, featurized into the risk model to map imaged DILI presentation to risk; and fine-tuned DINO embeddings clustering phenotypes to surface bioactive molecules distinguishable from background perturbation.",
			tags: ["Segmentation", "DINO", "Data Pipelines", "Drift Monitoring"]
		},
		{
			org: "Google DeepMind",
			title: "Clinical Risk Models with Stanford Hospital",
			venue: "NeurIPS 22 (ML4H)",
			description: "Showed that risk-stratification models with near-identical aggregate performance can disagree substantially on individual patients — an instability that undermines clinical trust, and one that has since grown into its own line of research. Built T5-based models over longitudinal EHR data with clinicians at Stanford, studied approaches to improve reliability, and validated in shadow deployment against live clinical data.",
			link: "https://proceedings.mlr.press/v193/lopez-martinez22a.html",
			linkText: "Link to paper",
			tags: ["Clinical ML", "EHR", "Reliability", "NeurIPS 22"]
		},
		{
			org: "Amazon / UMass",
			title: "Fast Intent Classification for Spoken Language Understanding",
			venue: "ICASSP 2020",
			description: "Early work on adaptive-depth inference — a technique now standard in efficient LLM serving and on-device speech systems. Applied a BranchyNet early-exit scheme to intent classification, adding exit points at intermediate stages so simpler utterances egress early rather than running the full network — cutting computational cost without compromising accuracy (~20% reduction in effective model size) on latency-constrained devices.",
			link: "https://arxiv.org/abs/1912.01728",
			linkText: "Link to paper",
			tags: ["NLP", "Efficient Inference", "Alexa", "ICASSP 2020"]
		},
		{
			org: "Amazon / UMass",
			title: "Conversational Question Answering and Noise Robustness",
			venue: "Amazon Research Days 2019",
			description: "Worked with Alexa's Implicit Memory team on noise robustness in conversational Q&A. We added speech-recognition-style noise to CoQA to build a noisy variant, showed that models like FlowQA degrade under that structured noise, and developed noise-robust embeddings through stability training and adversarial noise-domain adaptation.",
			link: "/files/noisyCoqa.pdf",
			linkText: "Link to poster",
			tags: ["NLP", "Question Answering", "Robustness", "Alexa"]
		},
		{
			title: "Faster Bayesian Parameter estimation for Neural nets",
			description: "Worked on making the process of MCMC sampling for bayesian parameter estimation quicker. Starting off from the work of bayesian dark knowledge, we wanted estimators more robust to dataset uncertainty, while keeping the inference time for the estimation process the same or better.",
			tags: ["Bayesian Learning", "MCMC", "Neural Networks"]
		},
		{
			title: "Getting better at Game Playing by transfer of skill",
			description: "Worked on transfer learning in the context of game playing. Transfer Learning has been used to learn policies from 10 of the 11 Atari games and use these as policy initiliasers for the last game. A generative model is fit for the simulations of the first ten and then fine-tuned by Joint Training and Feature Extraction for the eleventh game.",
			tags: ["Reinforcement Learning", "Transfer Learning", "Atari Games"]
		},
		{
			title: "WordVector Based Moderation Pipeline for Amazon Marketplace",
			description: "We developed an end-to-end distributed pipeline for scoring the risk factor of a specific advertisment campaign on the Amazon Marketplace. This uses the text description of the ad and the associated photograph. Using these two, we developed a feature extractor to encode the risk of the advertisement and then use an ensemble of regressors to give the majority score of the advertisment.",
			tags: ["Computer Vision", "NLP", "Amazon", "Moderation"]
		},
		{
			title: "Minimax Bot for playing the game of Tak",
			description: "The created bot uses Minimax to search over all the possible set of game states, and selects the best ones using a utility function. The utility function has been trained by seeing which features affect the quality of gameplay the most.",
			link: "https://github.com/akshittyagi/TakBot",
			linkText: "GitHub",
			tags: ["Game AI", "Minimax", "Python"]
		},
		{
			title: "Using Genetic Algorithms for approximately solving the Traveling Salesman Problem",
			description: "A specific tour of the travelling salesman was modelled as a gene for the Genetic Algorithm(GA). This gene was then mutated using two different crossover techniques: CX and PMX; and both the types of offsprings were included in the final population for the next generation.",
			link: "https://github.com/akshittyagi/tsp",
			linkText: "GitHub",
			tags: ["Genetic Algorithms", "Optimization", "TSP"]
		},
		{
			title: "Local Search Algorithms with Parallelization",
			description: "Implemented a set of Local Search algorithms including: HillClimibingWithRandomRestarts, HillClimbingwithTabu, BeamSearch, BeamSearchWithTabu and BeamSearchWithRandomRestarts. This is used to search for the global maxima for the cost of a resource allocation problem.",
			link: "https://github.com/akshittyagi/TowerAllocationusingAI",
			linkText: "GitHub",
			tags: ["Search Algorithms", "Parallelization", "Optimization"]
		},
		{
			title: "Echo State Networks for Stock Prediction",
			description: "We use an Echo State Network or a reservoir RNN for capturing the movement of a specific stock. The echo state network takes in the input as the stock price of the previous day, the learned state of the echo state network and outputs the predicted value of the index on the current day.",
			link: "https://github.com/akshittyagi/StockPred",
			linkText: "GitHub",
			tags: ["RNN", "Financial Modeling", "Time Series"]
		}
	];
</script>

<section class="section">
	<div class="container">
		<h2>Major Projects</h2>
		<div class="projects-grid">
			{#each projects as project, index}
				<div class="project-card card" style="animation-delay: {index * 0.1}s">
					<div class="project-header">
						{#if project.org}
							<span class="project-org">{project.org}</span>
						{/if}
						<h4>{project.title}</h4>
						{#if project.venue}
							<p class="project-venue">{project.venue}</p>
						{/if}
						<div class="project-tags">
							{#each project.tags as tag}
								<span class="tag">{tag}</span>
							{/each}
						</div>
					</div>
					<p class="project-description">{project.description}</p>
					{#if project.link}
						<a href={project.link} class="project-link" target="_blank" rel="noopener">
							<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
								<path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/>
								<polyline points="15,3 21,3 21,9"/>
								<line x1="10" y1="14" x2="21" y2="3"/>
							</svg>
							{project.linkText}
						</a>
					{/if}
				</div>
			{/each}
		</div>
	</div>
</section>

<style>
	.projects-grid {
		display: grid;
		grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
		gap: 2rem;
	}

	.project-card {
		opacity: 0;
		animation: fadeInUp 0.6s ease forwards;
		position: relative;
		overflow: hidden;
	}

	.project-card::before {
		content: '';
		position: absolute;
		top: 0;
		left: 0;
		right: 0;
		height: 4px;
		background: linear-gradient(90deg, var(--primary), var(--primary-light));
		opacity: 0;
		transition: opacity 0.3s ease;
	}

	.project-card:hover::before {
		opacity: 1;
	}

	.project-header {
		margin-bottom: 1rem;
	}

	.project-org {
		display: block;
		color: var(--primary);
		font-size: 0.8rem;
		font-weight: 600;
		text-transform: uppercase;
		letter-spacing: 0.06em;
		margin-bottom: 0.35rem;
	}

	.project-header h4 {
		margin-bottom: 0.35rem;
		color: var(--text-primary);
		line-height: 1.3;
	}

	.project-venue {
		color: var(--text-muted);
		font-size: 0.9rem;
		font-style: italic;
		margin-bottom: 0.75rem;
	}

	.project-tags {
		display: flex;
		flex-wrap: wrap;
		gap: 0.5rem;
		margin-bottom: 1rem;
	}

	.tag {
		background: var(--bg-tertiary);
		color: var(--text-secondary);
		padding: 0.25rem 0.75rem;
		border-radius: 1rem;
		font-size: 0.8rem;
		font-weight: 500;
	}

	.project-description {
		color: var(--text-secondary);
		line-height: 1.7;
		margin-bottom: 1.5rem;
	}

	.project-link {
		display: inline-flex;
		align-items: center;
		gap: 0.5rem;
		color: var(--primary);
		font-weight: 500;
		text-decoration: none;
		transition: all 0.2s ease;
	}

	.project-link:hover {
		color: var(--primary-light);
		transform: translateX(2px);
	}

	@keyframes fadeInUp {
		from {
			opacity: 0;
			transform: translateY(30px);
		}
		to {
			opacity: 1;
			transform: translateY(0);
		}
	}

	@media (max-width: 768px) {
		.projects-grid {
			grid-template-columns: 1fr;
			gap: 1.5rem;
		}
	}
</style>
