<script>
	const roles = [
		{
			period: "Jan 2025 - Present",
			title: "Founding Member of Technical Staff",
			company: "Axiom",
			summary: "Foundation models for cellular phenotyping and drug discovery",
			bullets: [
				"Developed segmentation models to detect and quantify structural / morphological changes in cells from high-content microscopy imaging",
				"Built and scaled data pipelines processing billions of cell images for large-scale model training and inference",
				"Learned representations of toxic cellular presentations directly from microscopy images, and used them to predict toxic structures in drug molecules",
				"Developing multimodal LLMs to interpret visual changes in cellular morphology and classify drugs by mechanism of action"
			],
			tags: ["Foundation Models", "Microscopy", "Toxicity Prediction", "Multimodal LLMs"]
		},
		{
			period: "May 2022 - Dec 2024",
			title: "Research Engineer",
			company: "Google Health",
			summary: "Building models for EHR data",
			bullets: [
				"Built algorithms to understand the medical condition of a patient based on EHR data",
				"Trained ML models to understand tabular data and large language models for doctors' notes"
			],
			tags: ["Healthcare", "EHR", "LLMs"]
		},
		{
			period: "Nov 2021 - Mar 2022",
			title: "ML Engineer",
			company: "Akasa",
			summary: "Building multi-modal models for hospital-patient interaction data",
			bullets: [
				"Built a context-aware representation for care-provider and patient interactions",
				"Representation includes health insurance cards and previous medical history of the patient"
			],
			tags: ["Multi-modal", "Healthcare"]
		},
		{
			period: "Mar - Oct 2021",
			title: "ML Engineer",
			company: "Armorblox",
			summary: "Building and improving email security using NLP",
			bullets: [
				"Time-series based anomaly detection models for account compromise detection",
				"Out-of-distribution detection on composite features built upon users' email profiles",
				"Weak supervision to reduce model maintenance as distribution drift occurs"
			],
			tags: ["NLP", "Security", "Anomaly Detection"]
		},
		{
			period: "Jul 2020 - Jan 2021",
			title: "AI Resident",
			company: "X, the moonshot factory",
			summary: "Worked on ultra low power TinyML as part of a stealth mode project",
			bullets: [],
			tags: ["TinyML"]
		},
		{
			period: "May - Aug 2019",
			title: "Applied Science Intern",
			company: "Alexa AI",
			summary: "Implicit Memory at Alexa Brain",
			bullets: [
				"Conversational question answering in the context of agents like Alexa",
				"Noise-robust embeddings through stability training and adversarial noise-domain adaptation"
			],
			tags: ["NLP", "Question Answering", "Robustness"]
		}
	];
</script>

<section id="experience" class="section">
	<div class="container">
		<h2>Work Experience</h2>
		<div class="timeline">
			{#each roles as role, index}
				<div class="role card" style="animation-delay: {index * 0.1}s">
					<div class="role-meta">
						<span class="period">{role.period}</span>
					</div>
					<div class="role-body">
						<h4><strong>{role.title}</strong> at {role.company}</h4>
						<p class="role-summary">{role.summary}</p>
						{#if role.bullets.length}
							<ul class="role-bullets">
								{#each role.bullets as bullet}
									<li>{bullet}</li>
								{/each}
							</ul>
						{/if}
						<div class="role-tags">
							{#each role.tags as tag}
								<span class="tag">{tag}</span>
							{/each}
						</div>
					</div>
				</div>
			{/each}
		</div>
	</div>
</section>

<style>
	.timeline {
		display: flex;
		flex-direction: column;
		gap: 1.5rem;
		max-width: 1000px;
		margin: 0 auto;
	}

	.role {
		display: grid;
		grid-template-columns: 180px 1fr;
		gap: 2rem;
		opacity: 0;
		animation: fadeInUp 0.6s ease forwards;
	}

	.period {
		color: var(--text-muted);
		font-size: 0.9rem;
		font-weight: 500;
		text-transform: uppercase;
		letter-spacing: 0.05em;
	}

	.role-body {
		border-left: 2px solid var(--border);
		padding-left: 1.5rem;
	}

	.role-body h4 {
		color: var(--text-primary);
		margin-bottom: 0.25rem;
		line-height: 1.3;
	}

	.role-summary {
		color: var(--text-secondary);
		font-style: italic;
		margin-bottom: 0.75rem;
	}

	.role-bullets {
		color: var(--text-secondary);
		line-height: 1.7;
		margin: 0 0 1rem 1.1rem;
	}

	.role-bullets li {
		margin-bottom: 0.35rem;
	}

	.role-tags {
		display: flex;
		flex-wrap: wrap;
		gap: 0.5rem;
	}

	.tag {
		background: var(--bg-tertiary);
		color: var(--text-secondary);
		padding: 0.25rem 0.75rem;
		border-radius: 1rem;
		font-size: 0.8rem;
		font-weight: 500;
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
		.role {
			grid-template-columns: 1fr;
			gap: 0.75rem;
		}

		.role-body {
			border-left: none;
			padding-left: 0;
		}
	}
</style>
