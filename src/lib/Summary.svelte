<section id="summary" class="section">
	<div class="container">
		<div class="summary-content">
			<h2>Summary</h2>
			<div class="content-grid">
				<div class="main-text prose">
					<p>
						I am an ML Engineer at Google Research working on creating ML models for healthcare applications. 
						I graduated with an MS CS from the College of Information and Computer Sciences 
						<a href="https://www.cics.umass.edu/">(CICS)</a> at <a href="http://www.umass.edu">UMass, Amherst</a>. 
						Before that, I was an undergrad at <a href="http://www.iitd.ac.in/">IIT, Delhi</a>. 
						You can find my resume <a href="/files/cvLatest.pdf">here</a>.
					</p>
					
					<p>
						I am interested broadly in the field of Theoretical Machine Learning and NLP and have worked 
						in projects involving computer vision, natural language processing and reinforcement learning.
					</p>
				</div>
				
				<div class="research-areas">
					<h3>Research Areas</h3>
					<ul class="research-list">
						<li>
							<div class="research-item">
								<div class="research-icon">🧠</div>
								<div>
									<strong>Bayesian Calibration</strong>
									<span>Learning of neural networks</span>
								</div>
							</div>
						</li>
						<li>
							<div class="research-item">
								<div class="research-icon">🏥</div>
								<div>
									<strong>Causal Inference</strong>
									<span>Medical diagnosis on multi-modal data</span>
								</div>
							</div>
						</li>
						<li>
							<div class="research-item">
								<div class="research-icon">💬</div>
								<div>
									<strong>Natural Language Understanding</strong>
									<span>Smart assistants like Alexa</span>
								</div>
							</div>
						</li>
					</ul>
				</div>
			</div>
		</div>
	</div>
</section>

<style>
	.section {
		background: var(--bg-secondary);
	}
	
	.summary-content {
		max-width: 1000px;
		margin: 0 auto;
	}
	
	.content-grid {
		display: grid;
		grid-template-columns: 2fr 1fr;
		gap: 4rem;
		align-items: start;
	}
	
	.main-text {
		font-size: 1.1rem;
		line-height: 1.8;
	}
	
	.research-areas {
		background: var(--bg-primary);
		padding: 2rem;
		border-radius: var(--radius-lg);
		box-shadow: var(--shadow);
		border: 1px solid var(--border);
	}
	
	.research-areas h3 {
		margin-bottom: 1.5rem;
		color: var(--text-primary);
	}
	
	.research-list {
		list-style: none;
		padding: 0;
		margin: 0;
	}
	
	.research-list li {
		margin-bottom: 1.5rem;
	}
	
	.research-list li:last-child {
		margin-bottom: 0;
	}
	
	.research-item {
		display: flex;
		align-items: flex-start;
		gap: 1rem;
	}
	
	.research-icon {
		font-size: 1.5rem;
		flex-shrink: 0;
		background: var(--bg-tertiary);
		width: 3rem;
		height: 3rem;
		border-radius: 50%;
		display: flex;
		align-items: center;
		justify-content: center;
	}
	
	.research-item strong {
		display: block;
		color: var(--text-primary);
		font-weight: 600;
		margin-bottom: 0.25rem;
	}
	
	.research-item span {
		color: var(--text-secondary);
		font-size: 0.9rem;
	}
	
	@media (max-width: 768px) {
		.content-grid {
			grid-template-columns: 1fr;
			gap: 2rem;
		}
		
		.research-areas {
			padding: 1.5rem;
		}
		
		.research-item {
			gap: 0.75rem;
		}
		
		.research-icon {
			width: 2.5rem;
			height: 2.5rem;
			font-size: 1.25rem;
		}
	}
</style>