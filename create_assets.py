import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

# Architecture diagram
fig, ax = plt.subplots(figsize=(10, 5.6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')

def box(x, y, w, h, text):
    patch = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.05,rounding_size=0.08", linewidth=1.4, facecolor='white')
    ax.add_patch(patch)
    ax.text(x+w/2, y+h/2, text, ha='center', va='center', fontsize=11, wrap=True)

def arrow(x1,y1,x2,y2):
    ax.add_patch(FancyArrowPatch((x1,y1), (x2,y2), arrowstyle='->', mutation_scale=14, linewidth=1.2))

box(0.4, 2.4, 1.7, 1.0, "Usuário\nNavegador")
box(2.7, 2.4, 1.8, 1.0, "Front-end\nStreamlit")
box(5.1, 2.4, 1.7, 1.0, "API\nFastAPI")
box(7.4, 2.4, 1.8, 1.0, "Broker\nRedis")
for i, y in enumerate([4.4, 3.2, 2.0, 0.8], start=1):
    box(7.5, y, 1.7, 0.65, f"Worker {i}\nCelery")

arrow(2.1, 2.9, 2.7, 2.9)
arrow(4.5, 2.9, 5.1, 2.9)
arrow(6.8, 2.9, 7.4, 2.9)
for y in [4.72, 3.52, 2.32, 1.12]:
    arrow(8.3, 3.4, 8.3, y)
ax.text(5, 5.6, "Arquitetura da aplicação distribuída", ha='center', fontsize=14, weight='bold')
ax.text(5, 0.25, "A carga é dividida em chunks independentes e processada pelos workers em containers isolados.", ha='center', fontsize=10)
plt.tight_layout()
plt.savefig('/mnt/data/cloud_montecarlo_distribuido/docs/arquitetura.png', dpi=200, bbox_inches='tight')
plt.close()

workers = [1, 2, 4, 8]
times = [4.359, 2.410, 1.691, 2.166]
fig, ax = plt.subplots(figsize=(8, 4.5))
ax.bar([str(w) for w in workers], times)
ax.set_xlabel('Quantidade de workers')
ax.set_ylabel('Tempo de execução (segundos)')
ax.set_title('Comparação de performance - 12.000.000 iterações')
for i, v in enumerate(times):
    ax.text(i, v + 0.05, f'{v:.3f}s', ha='center', fontsize=10)
plt.tight_layout()
plt.savefig('/mnt/data/cloud_montecarlo_distribuido/docs/performance.png', dpi=200, bbox_inches='tight')
plt.close()
