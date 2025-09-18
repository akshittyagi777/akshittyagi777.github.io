<script>
	import { onMount } from 'svelte';
	
	let mounted = false;
	
	onMount(() => {
		mounted = true;
	});
</script>

<section class="hero">
	<div class="container">
		<div class="hero-content">
			<div class="hero-image" class:animate={mounted}>
				<img src="/images/fp2.jpg" alt="Akshit Tyagi" />
				<div class="image-decoration"></div>
			</div>
			<div class="hero-text" class:animate={mounted}>
				<h1>Akshit Tyagi</h1>
				<p class="subtitle">ML Engineer at Google Research</p>
				<p class="description">
					Creating ML models for healthcare applications. MS CS from UMass Amherst, 
					passionate about Theoretical Machine Learning and NLP.
				</p>
				<div class="hero-actions">
					<a href="/files/cvLatest.pdf" class="btn btn-primary" target="_blank" rel="noopener">
						<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
							<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
							<polyline points="14,2 14,8 20,8"/>
							<line x1="16" y1="13" x2="8" y2="13"/>
							<line x1="16" y1="17" x2="8" y2="17"/>
							<polyline points="10,9 9,9 8,9"/>
						</svg>
						View Resume
					</a>
					<a href="#summary" class="btn btn-outline">Learn More</a>
				</div>
			</div>
		</div>
	</div>
</section>

<style>
	.hero {
		background: linear-gradient(135deg, var(--bg-primary) 0%, var(--bg-secondary) 100%);
		padding: 6rem 0 4rem;
		position: relative;
		overflow: hidden;
	}
	
	.hero::before {
		content: '';
		position: absolute;
		top: 0;
		left: 0;
		right: 0;
		bottom: 0;
		background: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23f3f4f6' fill-opacity='0.4'%3E%3Ccircle cx='30' cy='30' r='1'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
		opacity: 0.5;
	}
	
	.hero-content {
		display: grid;
		grid-template-columns: 300px 1fr;
		gap: 4rem;
		align-items: center;
		position: relative;
		z-index: 1;
	}
	
	.hero-image {
		position: relative;
		opacity: 0;
		transform: translateY(30px);
		transition: all 0.8s ease;
	}
	
	.hero-image.animate {
		opacity: 1;
		transform: translateY(0);
	}
	
	.hero-image img {
		width: 100%;
		height: auto;
		border-radius: var(--radius-lg);
		box-shadow: var(--shadow-lg);
		position: relative;
		z-index: 2;
	}
	
	.image-decoration {
		position: absolute;
		top: 1rem;
		left: 1rem;
		right: -1rem;
		bottom: -1rem;
		background: linear-gradient(45deg, var(--primary), var(--primary-light));
		border-radius: var(--radius-lg);
		z-index: 1;
		opacity: 0.1;
	}
	
	.hero-text {
		opacity: 0;
		transform: translateX(30px);
		transition: all 0.8s ease 0.2s;
	}
	
	.hero-text.animate {
		opacity: 1;
		transform: translateX(0);
	}
	
	.hero-text h1 {
		font-size: 3.5rem;
		font-weight: 700;
		background: linear-gradient(135deg, var(--text-primary), var(--primary));
		-webkit-background-clip: text;
		-webkit-text-fill-color: transparent;
		background-clip: text;
		margin-bottom: 0.5rem;
	}
	
	.subtitle {
		font-size: 1.25rem;
		font-weight: 500;
		color: var(--primary);
		margin-bottom: 1rem;
	}
	
	.description {
		font-size: 1.1rem;
		color: var(--text-secondary);
		margin-bottom: 2rem;
		line-height: 1.7;
	}
	
	.hero-actions {
		display: flex;
		gap: 1rem;
		flex-wrap: wrap;
	}
	
	@media (max-width: 768px) {
		.hero {
			padding: 4rem 0 2rem;
		}
		
		.hero-content {
			grid-template-columns: 1fr;
			text-align: center;
			gap: 2rem;
		}
		
		.hero-image {
			max-width: 250px;
			margin: 0 auto;
		}
		
		.hero-text h1 {
			font-size: 2.5rem;
		}
		
		.hero-actions {
			justify-content: center;
		}
	}
</style>