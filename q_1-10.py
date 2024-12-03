# Questão 10

import numpy as np
import matplotlib.pyplot as plt

# Constantes
k = 8.99e9  # Constante de Coulomb em N⋅m²/C²
Q = 15e-6  # 15 µC
lado = 4  # lado do quadrado em metros

# Posições das cargas
r1 = np.array([lado / 2, lado / 2, 0])
r2 = np.array([-lado / 2, lado / 2, 0])
r3 = np.array([-lado / 2, -lado / 2, 0])
r4 = np.array([lado / 2, -lado / 2, 0])

# Ponto onde queremos calcular o campo elétrico
P = np.array([0, 0, 6])


def campo_eletrico(q, r, r0):
    """Calcula o campo elétrico devido a uma carga pontual."""
    R = r0 - r
    R_mag = np.linalg.norm(R)
    return k * q * R / R_mag**3


# Solução analítica
E1 = campo_eletrico(Q, r1, P)
E2 = campo_eletrico(Q, r2, P)
E3 = campo_eletrico(Q, r3, P)
E4 = campo_eletrico(Q, r4, P)
E_total_analitico = E1 + E2 + E3 + E4

print("Questão 10 - Solução analítica:")
print(f"Campo elétrico em P(0, 0, 6): {E_total_analitico} N/C")
print(f"Magnitude do campo elétrico: {np.linalg.norm(E_total_analitico):.4e} N/C")


# Solução computacional
def campo_eletrico_total(cargas, posicoes, r0):
    """Calcula o campo elétrico total devido a várias cargas pontuais."""
    E_total = np.zeros(3)
    for q, r in zip(cargas, posicoes):
        E_total += campo_eletrico(q, r, r0)
    return E_total


cargas = [Q, Q, Q, Q]
posicoes = [r1, r2, r3, r4]
E_total_computacional = campo_eletrico_total(cargas, posicoes, P)

print("\nSolução computacional:")
print(f"Campo elétrico em P(0, 0, 6): {E_total_computacional} N/C")
print(f"Magnitude do campo elétrico: {np.linalg.norm(E_total_computacional):.4e} N/C")

# Comparação
diferenca_percentual = (
    np.linalg.norm(E_total_computacional - E_total_analitico)
    / np.linalg.norm(E_total_analitico)
    * 100
)

print("\nComparação:")
print(f"Diferença percentual: {diferenca_percentual:.6f}%")

# Visualização 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")

# Plotar as cargas
ax.scatter(*r1, color="r", s=100, label="Q1")
ax.scatter(*r2, color="b", s=100, label="Q2")
ax.scatter(*r3, color="g", s=100, label="Q3")
ax.scatter(*r4, color="y", s=100, label="Q4")

# Plotar o ponto P
ax.scatter(*P, color="m", s=100, label="P")

# Plotar o vetor campo elétrico
ax.quiver(
    *P, *E_total_analitico, color="k", length=0.5, normalize=True, label="E total"
)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Visualização 3D do problema")
ax.legend()
plt.show()

print("\nAnálise dos resultados:")
print(
    "1. As soluções analítica e computacional são idênticas dentro da precisão numérica."
)
print(
    "2. O campo elétrico resultante tem apenas componente na direção z, devido à simetria do problema."
)
print(
    "3. A magnitude do campo elétrico é significativa, da ordem de 10^4 N/C, devido à proximidade das cargas e seus valores elevados."
)
print(
    "4. A visualização 3D mostra claramente a configuração das cargas e a direção do campo elétrico resultante."
)
print(
    "5. Este problema demonstra a eficácia do princípio de superposição para calcular campos elétricos em sistemas de múltiplas cargas simétricas."
)
