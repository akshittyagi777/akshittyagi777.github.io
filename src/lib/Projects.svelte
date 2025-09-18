<script>
	const projects = [
		{
			title: "Faster Bayesian Parameter estimation for Neural nets",
			description: "Currently working on making the process of MCMC sampling for bayesian parameter estimation quicker. Starting off from the work of bayesian dark knowledge, we want to come up with estimators more robust to dataset uncertainty, while keeping the inference time for the estimation process to be the same or better.",
			link: "https://arxiv.org/abs/1506.04416",
			linkText: "bayesian dark knowledge",
			tags: ["Bayesian Learning", "MCMC", "Neural Networks"]
		},
		{
			title: "Causal Inference models for multi-model Medical Diagnosis data",
			description: "Currently working on building hierarchical bayesian diagnostic models for MIMIC dataset. We are working on formalizing the problem as a causal inference problem and investigating the advantages such a formulation can have.",
			link: "https://mimic.physionet.org",
			linkText: "MIMIC dataset",
			tags: ["Causal Inference", "Healthcare", "Bayesian Models"]
		},
		{
			title: "Building models for Noisy Conversational Question Answering",
			description: "Worked with Alexa's Implicit Memory team on finding out the best way to integrate noise robustness in text based Q&A models using transformers and ELMo embeddings. We add noise to the CoQA dataset, creating a noisy version of CoQA. Evaluating models like FlowQA on noisy-CoQA exposes the problems with modern text based NLP models to structured noise coming through speech recognition and ambient noise sources.",
			link: "https://stanfordnlp.github.io/coqa/",
			linkText: "CoQA",
			tags: ["NLP", "Question Answering", "Robustness", "Alexa"]
		},
		{
			title: "Natural Language Understanding through Intent Classification",
			description: "Worked with Alexa's Spoken Language Understanding team on building a fast intent classifier. This will be integrated with the voice assistant as a tool to identify the intent of the utterance spoken by the user in a dialogue form. We were able to build in an early exiting strategy, that can be integrated with LSTMs and affine neural networks, traditionally used for such tasks.",
			link: "https://arxiv.org/abs/1912.01728",
			linkText: "Link to paper",
			tags: ["NLP", "Intent Classification", "Alexa", "ICASSP 2020"]
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
		<h2>Major Projects and Internships</h2>
		<div class="projects-grid">
			{#each projects as project, index}
				<div class="project-card card" style="animation-delay: {index * 0.1}s">
					<div class="project-header">
						<h4>{project.title}</h4>
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
	
	.project-header h4 {
		margin-bottom: 0.75rem;
		color: var(--text-primary);
		line-height: 1.3;
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