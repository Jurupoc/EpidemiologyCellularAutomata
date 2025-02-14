import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parâmetros do modelo
GRID_SIZE = 50  # Tamanho da grade
INFECTION_RATE = 0.3  # Probabilidade de infecção
RECOVERY_RATE = 0.1  # Probabilidade de recuperação
INITIAL_INFECTED = 5  # Número inicial de infectados
STEPS = 100  # Número de iterações da simulação

# Estados das células
SUSCEPTIBLE = 0
INFECTED = 1
RECOVERED = 2

# Inicialização da grade
grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)

# Escolher células aleatórias para iniciar a infecção
infected_indices = np.random.choice(GRID_SIZE * GRID_SIZE, INITIAL_INFECTED, replace=False)
for index in infected_indices:
    x, y = divmod(index, GRID_SIZE)
    grid[x, y] = INFECTED


def update(grid):
    new_grid = grid.copy()
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            if grid[x, y] == INFECTED:
                if np.random.rand() < RECOVERY_RATE:
                    new_grid[x, y] = RECOVERED
                else:
                    # Espalhar infecção para vizinhos
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            if (dx != 0 or dy != 0):  # Não incluir a célula atual
                                nx, ny = x + dx, y + dy
                                if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
                                    if grid[nx, ny] == SUSCEPTIBLE and np.random.rand() < INFECTION_RATE:
                                        new_grid[nx, ny] = INFECTED
    return new_grid


# Configuração da animação
fig, ax = plt.subplots()
cmap = plt.get_cmap("viridis", 3)
mat = ax.matshow(grid, cmap=cmap, vmin=0, vmax=2)


def animate(i):
    global grid
    grid = update(grid)
    mat.set_data(grid)
    return [mat]


ani = animation.FuncAnimation(fig, animate, frames=STEPS, interval=200, repeat=False)
plt.colorbar(mat, ticks=[SUSCEPTIBLE, INFECTED, RECOVERED], label="Estado")
plt.title("Simulação Epidemiológica com Autômatos Celulares")
plt.show()
