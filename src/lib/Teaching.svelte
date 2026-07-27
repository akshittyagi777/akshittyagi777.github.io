<script>
	const teachingExperience = [
		{
			semester: "Fall Semester 2017",
			role: "Undergrad TA",
			course: "ELL311: Communication Engineering",
			type: "undergrad"
		},
		{
			semester: "Spring Semester 2018",
			role: "Undergrad TA",
			course: "MTL106: Probability and Stochastic Processes",
			type: "undergrad"
		},
		{
			semester: "Spring Semester 2019",
			role: "Grad TA",
			course: "CS683: Artifical Intelligence",
			type: "grad"
		},
		{
			semester: "Fall Semester 2019",
			role: "Grad TA",
			course: "CS589: Machine Learning",
			type: "grad"
		}
	];
</script>

<section class="section teaching">
	<div class="container">
		<div class="teaching-content">
			<h2>Teaching Experience</h2>
			<div class="teaching-grid">
				{#each teachingExperience as experience, index}
					<div class="teaching-item" class:grad={experience.type === 'grad'} style="animation-delay: {index * 0.15}s">
						<div class="teaching-header">
							<span class="role-badge" class:grad-badge={experience.type === 'grad'}>
								{experience.role}
							</span>
							<span class="semester">{experience.semester}</span>
						</div>
						<h4 class="course-title">{experience.course}</h4>
					</div>
				{/each}
			</div>
		</div>
	</div>
</section>

<style>
	.teaching {
		background: var(--bg-tertiary);
	}
	
	.teaching-content {
		max-width: 800px;
		margin: 0 auto;
		text-align: center;
	}
	
	.teaching h2 {
		margin-bottom: 3rem;
	}
	
	.teaching-grid {
		display: grid;
		grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
		gap: 1.5rem;
	}
	
	.teaching-item {
		background: var(--bg-primary);
		padding: 2rem;
		border-radius: var(--radius-lg);
		border: 1px solid var(--border);
		box-shadow: var(--shadow);
		transition: all 0.3s ease;
		opacity: 0;
		animation: fadeInScale 0.6s ease forwards;
		position: relative;
		overflow: hidden;
	}
	
	.teaching-item::before {
		content: '';
		position: absolute;
		top: 0;
		left: 0;
		right: 0;
		height: 4px;
		background: linear-gradient(90deg, #6366f1, #8b5cf6);
		transform: scaleX(0);
		transition: transform 0.3s ease;
	}
	
	.teaching-item.grad::before {
		background: linear-gradient(90deg, var(--primary), var(--primary-light));
	}
	
	.teaching-item:hover::before {
		transform: scaleX(1);
	}
	
	.teaching-item:hover {
		transform: translateY(-4px);
		box-shadow: var(--shadow-lg);
	}
	
	.teaching-header {
		display: flex;
		justify-content: space-between;
		align-items: center;
		margin-bottom: 1rem;
		flex-wrap: wrap;
		gap: 0.5rem;
	}
	
	.role-badge {
		background: linear-gradient(135deg, #6366f1, #8b5cf6);
		color: white;
		padding: 0.5rem 1rem;
		border-radius: 2rem;
		font-size: 0.85rem;
		font-weight: 600;
		text-transform: uppercase;
		letter-spacing: 0.5px;
	}
	
	.grad-badge {
		background: linear-gradient(135deg, var(--primary), var(--primary-light));
	}
	
	.semester {
		color: var(--text-muted);
		font-size: 0.9rem;
		font-weight: 500;
	}
	
	.course-title {
		color: var(--text-primary);
		font-size: 1.1rem;
		font-weight: 600;
		margin: 0;
		line-height: 1.4;
	}
	
	@keyframes fadeInScale {
		from {
			opacity: 0;
			transform: scale(0.9);
		}
		to {
			opacity: 1;
			transform: scale(1);
		}
	}
	
	@media (max-width: 768px) {
		.teaching-grid {
			grid-template-columns: 1fr;
		}
		
		.teaching-item {
			padding: 1.5rem;
		}
		
		.teaching-header {
			flex-direction: column;
			align-items: flex-start;
			gap: 0.75rem;
		}
	}
</style>