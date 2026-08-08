<script>
	const groups = [
		{
			label: "Methods",
			items: "LLM fine-tuning & alignment (LoRA, RLHF, DPO), diffusion models, vision foundation models (DINO), segmentation, multimodal modeling"
		},
		{
			label: "Scale & Data",
			items: "Distributed data pipelines at 10M+ image scale (Ray, Spark, Modal)"
		},
		{
			label: "Languages",
			items: "Python, C++, CUDA"
		},
		{
			label: "ML Frameworks",
			items: "PyTorch, Hugging Face (Transformers, Datasets)"
		},
		{
			label: "Infra / MLOps",
			items: "Weights & Biases, MLflow, Docker, GCP, AWS"
		}
	];

	const education = [
		"M.S. Computer Science, UMass Amherst (2020)",
		"B.Tech. Electrical Engineering, IIT Delhi (2018)"
	];

	const service = "Reviewer — NeurIPS, ICML, ICLR, ACL";
</script>

<section id="skills" class="section skills">
	<div class="container">
		<h2>Skills, Education and Service</h2>
		<div class="skills-grid">
			<div class="card skills-card">
				<h3>Technical Skills</h3>
				<dl>
					{#each groups as group}
						<dt>{group.label}</dt>
						<dd>{group.items}</dd>
					{/each}
				</dl>
			</div>
			<div class="card skills-card">
				<h3>Education</h3>
				<ul>
					{#each education as line}
						<li>{line}</li>
					{/each}
				</ul>
				<h3 class="second-heading">Service</h3>
				<p>{service}</p>
			</div>
		</div>
	</div>
</section>

<style>
	.skills {
		background: var(--bg-secondary);
	}

	.skills-grid {
		display: grid;
		grid-template-columns: 2fr 1fr;
		gap: 2rem;
		max-width: 1000px;
		margin: 0 auto;
	}

	.skills-card h3 {
		margin-bottom: 1rem;
		color: var(--text-primary);
	}

	.second-heading {
		margin-top: 1.5rem;
	}

	dl {
		margin: 0;
	}

	dt {
		color: var(--primary);
		font-size: 0.8rem;
		font-weight: 600;
		text-transform: uppercase;
		letter-spacing: 0.06em;
		margin-bottom: 0.25rem;
	}

	dd {
		color: var(--text-secondary);
		line-height: 1.7;
		margin: 0 0 1rem 0;
	}

	dd:last-child {
		margin-bottom: 0;
	}

	ul {
		color: var(--text-secondary);
		line-height: 1.7;
		margin: 0 0 0 1.1rem;
		padding: 0;
	}

	p {
		color: var(--text-secondary);
		line-height: 1.7;
	}

	@media (max-width: 768px) {
		.skills-grid {
			grid-template-columns: 1fr;
		}
	}
</style>
