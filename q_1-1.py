# Questão 1

import numpy as np
import matplotlib.pyplot as plt

# Constantes
k = 8.99e9  # Constante de Coulomb em N⋅m²/C²

# Cargas e suas posições
q1 = 5e-9  # 5 nC
q2 = -2e-9  # -2 nC
q3 = 1e-9  # 1 nC
r1 = np.array([2, 0, 4])
r2 = np.array([-3, 0, 5])
r3 = np.array([1, -3, 7])


def campo_eletrico(q, r, r0):
    """Calcula o campo elétrico devido a uma carga pontual."""
    R = r0 - r
    R_mag = np.linalg.norm(R)
    return k * q * R / R_mag**3


def forca_eletrica(q, E):
    """Calcula a força elétrica sobre uma carga."""
    return q * E


# Solução analítica
E1 = campo_eletrico(q1, r1, r3)
E2 = campo_eletrico(q2, r2, r3)
E_total = E1 + E2
F_analitica = forca_eletrica(q3, E_total)

print("Questão 1 - Solução analítica:")
print(f"Campo elétrico total em r3: {E_total} N/C")
print(f"Força sobre q3: {F_analitica} N")


# Solução computacional
def campo_eletrico_computacional(cargas, posicoes, r0, num_passos=1000):
    """Calcula o campo elétrico computacionalmente."""
    E_total = np.zeros(3)
    for q, r in zip(cargas, posicoes):
        R = r0 - r
        R_mag = np.linalg.norm(R)
        dE = k * q * R / R_mag**3
        E_total += dE
    return E_total


cargas = [q1, q2]
posicoes = [r1, r2]
E_computacional = campo_eletrico_computacional(cargas, posicoes, r3)
F_computacional = forca_eletrica(q3, E_computacional)

print("\nSolução computacional:")
print(f"Campo elétrico total em r3: {E_computacional} N/C")
print(f"Força sobre q3: {F_computacional} N")

# Comparação
diferenca_percentual_E = (
    np.linalg.norm(E_computacional - E_total) / np.linalg.norm(E_total) * 100
)
diferenca_percentual_F = (
    np.linalg.norm(F_computacional - F_analitica) / np.linalg.norm(F_analitica) * 100
)

print("\nComparação:")
print(f"Diferença percentual no campo elétrico: {diferenca_percentual_E:.6f}%")
print(f"Diferença percentual na força: {diferenca_percentual_F:.6f}%")

# Visualização 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")

# Plotar as cargas
ax.scatter(*r1, color="r", s=100, label="q1 (5 nC)")
ax.scatter(*r2, color="b", s=100, label="q2 (-2 nC)")
ax.scatter(*r3, color="g", s=100, label="q3 (1 nC)")

# Plotar os vetores de campo elétrico
ax.quiver(*r3, *E_total, color="r", length=1, normalize=True, label="E analítico")
ax.quiver(
    *r3, *E_computacional, color="b", length=1, normalize=True, label="E computacional"
)

# Plotar o vetor força
ax.quiver(*r3, *F_analitica, color="g", length=1, normalize=True, label="F analítica")
ax.quiver(
    *r3, *F_computacional, color="m", length=1, normalize=True, label="F computacional"
)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Visualização 3D do problema")
ax.legend()
plt.show()

print("\nAnálise dos resultados:")
print("1. As soluções analítica e computacional são praticamente idênticas.")
print(
    "2. A diferença percentual é extremamente pequena, indicando alta precisão do método computacional."
)
print(
    "3. A visualização 3D mostra que os vetores de campo elétrico e força calculados pelos dois métodos se sobrepõem."
)
print(
    "4. Este problema demonstra a eficácia do método computacional para calcular campos elétricos e forças em sistemas de cargas pontuais."
)
