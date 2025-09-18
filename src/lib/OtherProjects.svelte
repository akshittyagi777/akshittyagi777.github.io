<script>
	const otherProjects = [
		{
			title: "Sparse Matrix Vector Multiplication",
			description: "Built a parallelised module for multiplying a sparse matrix with a dense vector. This use case is commmonly seen in Deep Learning libraries with vector calculus dictating many of the matrices in use to be sparse. The Matrix was represented as a Compressed Sparse Row(CSR), and the calculations were henceforth parallelised for the dot product. Using CUDA allowed for device level and global level data and functionality separation.",
			link: "https://github.com/akshittyagi/sparseMatVecMul",
			linkText: "GitHub"
		},
		{
			title: "Physics Engine for a Simulator Game",
			description: "Built a C# application for the universal Windows environment. We designed a PhysX Engine from scratch for a space simulator with gravity and multi-partilce interactions. This was packaged as a game and won the Runners Up at Microsoft's Code.Fun.Do hackathon. Choosing to develop a customised PhysX Engine over Unity gave us more speed and resulted in a smoother user experience.",
			link: "https://github.com/akshittyagi/beynew",
			linkText: "GitHub"
		},
		{
			title: "Android application for Moodle",
			description: "We developed an android app for the learning management system used at IIT Delhi- Moodle. This was done as an assignment as proof-of-concept for porting the moodle system to a mobile-friendly environment. web2py was used for the server-side handling of the users and their registration and modification of data.",
			link: "https://github.com/akshittyagi/MoodlePlus",
			linkText: "GitHub"
		}
	];
</script>

<section class="section other-projects">
	<div class="container">
		<h2>Other Projects and Apps</h2>
		<div class="projects-list">
			{#each otherProjects as project, index}
				<div class="project-item" style="animation-delay: {index * 0.2}s">
					<div class="project-content">
						<h4>{project.title}</h4>
						<p>{project.description}</p>
						<div class="project-links">
							{#if project.link}
								<a href={project.link} class="project-link" target="_blank" rel="noopener">
									<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
										<path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/>
									</svg>
									{project.linkText}
								</a>
							{/if}
						</div>
					</div>
					<div class="project-decoration"></div>
				</div>
			{/each}
		</div>
	</div>
</section>

<style>
	.other-projects {
		background: var(--bg-primary);
	}
	
	.projects-list {
		max-width: 800px;
		margin: 0 auto;
	}
	
	.project-item {
		position: relative;
		padding: 2rem;
		margin-bottom: 2rem;
		background: var(--bg-secondary);
		border-radius: var(--radius-lg);
		border: 1px solid var(--border);
		transition: all 0.3s ease;
		opacity: 0;
		animation: slideInLeft 0.6s ease forwards;
		overflow: hidden;
	}
	
	.project-item:last-child {
		margin-bottom: 0;
	}
	
	.project-item:hover {
		transform: translateX(8px);
		box-shadow: var(--shadow-md);
	}
	
	.project-decoration {
		position: absolute;
		top: 0;
		left: 0;
		width: 4px;
		height: 100%;
		background: linear-gradient(180deg, var(--primary), var(--primary-light));
		transform: scaleY(0);
		transform-origin: bottom;
		transition: transform 0.3s ease;
	}
	
	.project-item:hover .project-decoration {
		transform: scaleY(1);
	}
	
	.project-content h4 {
		color: var(--text-primary);
		margin-bottom: 1rem;
		font-size: 1.25rem;
	}
	
	.project-content p {
		color: var(--text-secondary);
		line-height: 1.7;
		margin-bottom: 1.5rem;
	}
	
	.project-links {
		display: flex;
		gap: 1rem;
		flex-wrap: wrap;
	}
	
	.project-link {
		display: inline-flex;
		align-items: center;
		gap: 0.5rem;
		color: var(--primary);
		font-weight: 500;
		text-decoration: none;
		transition: all 0.2s ease;
		padding: 0.5rem 1rem;
		border: 1px solid var(--primary);
		border-radius: var(--radius);
		background: transparent;
	}
	
	.project-link:hover {
		background: var(--primary);
		color: white;
		transform: translateY(-2px);
	}
	
	
	@keyframes slideInLeft {
		from {
			opacity: 0;
			transform: translateX(-30px);
		}
		to {
			opacity: 1;
			transform: translateX(0);
		}
	}
	
	@media (max-width: 768px) {
		.project-item {
			padding: 1.5rem;
		}
		
		.project-item:hover {
			transform: translateX(4px);
		}
	}
</style>