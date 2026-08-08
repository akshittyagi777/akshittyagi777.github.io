<script>
	const roles = [
		{
			period: "Jan 2025 - Present",
			title: "Founding Member of Technical Staff",
			company: "Axiom",
			summary: "Multimodal foundation models for cellular phenotyping and drug safety",
			bullets: [
				"Built in silico clinical risk models predicting drug-induced liver injury (DILI) from molecular structure (SMILES) — 0.92 AUC (77% sensitivity, 90% specificity) on FDA DILIrank, matching or outperforming industry-standard 2D and 3D spheroid in vitro assays",
				"Co-designed the underlying 2D multiplexed cytotoxicity assay with biologists and external research labs / CROs, using model interpretability to guide what the assay should measure",
				"Owned the imaging ML stack end to end: deep-learning segmentation and phenotype quantification, multimodal LLMs for mechanism-of-action classification, and pipelines over 10M+ cell images"
			],
			tags: ["Foundation Models", "Drug Safety", "Cell Imaging", "Multimodal LLMs"]
		},
		{
			period: "Jul 2023 - 2024",
			title: "Research Engineer",
			company: "Helm AI",
			summary: "Using deep teaching for foundation models in autonomous vehicles",
			bullets: [
				"Trained and fine-tuned UNets, Latent Diffusion Models and DINO-family models for perception and generative simulation, building physics-informed dash-cam video to augment real-world data",
				"Built deep-teaching methods for semi-supervised learning of self-driving foundation models; optimized the self-driving SDK for custom architectures, improving on-device latency"
			],
			tags: ["Autonomous Vehicles", "Diffusion Models", "DINO", "Semi-supervised"]
		},
		{
			period: "May 2022 - Jul 2023",
			title: "Research Engineer",
			company: "Google DeepMind",
			summary: "Google Health: clinical ML in research collaboration with Stanford Hospital",
			bullets: [
				"Research collaboration with clinicians and researchers at Stanford Hospital on EHR-based patient risk prediction",
				"Built algorithms to infer patient medical condition from longitudinal EHR data using T5 transformers",
				"Ran the resulting models in shadow deployment at Stanford against live clinical data",
				"Surfaced instability in clinical risk-stratification models under distribution shift; published at NeurIPS 22 (ML4H)"
			],
			tags: ["Clinical ML", "EHR", "Transformers", "NeurIPS 22"]
		},
		{
			period: "Nov 2021 - Mar 2022",
			title: "ML Engineer",
			company: "Akasa",
			summary: "Multi-modal, context-aware representations of care-provider / patient interactions from insurance cards and prior medical history",
			bullets: [],
			tags: ["Multi-modal", "Healthcare"]
		},
		{
			period: "Mar - Oct 2021",
			title: "ML Engineer",
			company: "Armorblox",
			summary: "Building and improving email security using NLP",
			bullets: [
				"Built time-series anomaly-detection and out-of-distribution models over composite features from users' email profiles, for account-compromise detection",
				"Applied weak supervision to cut model maintenance under distribution drift"
			],
			tags: ["NLP", "Security", "Anomaly Detection"]
		},
		{
			period: "Jul 2020 - Jan 2021",
			title: "AI Resident",
			company: "X, the moonshot factory",
			summary: "Ultra-low-power TinyML for iyo",
			bullets: [],
			tags: ["TinyML"]
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
