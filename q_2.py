import numpy as np
import matplotlib.pyplot as plt

# Constantes
k = 8.99e9  # Constante de Coulomb em N⋅m²/C²
Q = 10  # Carga total em Coulombs
L = 1  # Comprimento da linha em metros
P = np.array([0, 10, 0])  # Ponto P(0, 10, 0) em metros


def campo_eletrico_linha_uniforme(Q, L, P):
    """Calcula o campo elétrico de uma linha uniformemente carregada."""
    x, y, z = P
    return (
        (k * Q)
        / (L * y)
        * (L / 2 / np.sqrt((L / 2) ** 2 + y**2) + L / 2 / np.sqrt((L / 2) ** 2 + y**2))
    )


def campo_eletrico_cargas_pontuais(Q, L, P, num_cargas):
    """Calcula o campo elétrico de cargas pontuais distribuídas uniformemente."""
    x, y, z = P
    q = Q / num_cargas
    posicoes = np.linspace(-L / 2, L / 2, num_cargas)
    E_total = np.zeros(3)

    for pos in posicoes:
        r = P - np.array([0, 0, pos])
        r_mag = np.linalg.norm(r)
        E_total += k * q * r / r_mag**3

    return E_total


# (a) Solução analítica
E_analitico = campo_eletrico_linha_uniforme(Q, L, P)
print(f"(a) Campo elétrico analítico em P: {E_analitico:.4e} N/C")

# (b) Solução computacional para diferentes números de cargas pontuais
num_cargas_list = [10, 15, 30]
E_computacional = []

for num_cargas in num_cargas_list:
    E = campo_eletrico_cargas_pontuais(Q, L, P, num_cargas)
    E_mag = np.linalg.norm(E)
    E_computacional.append(E_mag)
    print(f"(b) Campo elétrico computacional com {num_cargas} cargas: {E_mag:.4e} N/C")
    print(
        f"   Diferença percentual: {abs(E_mag - E_analitico) / E_analitico * 100:.2f}%"
    )

# Plotagem dos resultados
plt.figure(figsize=(10, 6))
plt.plot(num_cargas_list, E_computacional, "bo-", label="Computacional")
plt.axhline(y=E_analitico, color="r", linestyle="--", label="Analítico")
plt.xlabel("Número de cargas pontuais")
plt.ylabel("Magnitude do campo elétrico (N/C)")
plt.title("Campo elétrico vs. Número de cargas pontuais")
plt.legend()
plt.grid(True)
plt.show()

# Visualização 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")

# Linha carregada
z = np.linspace(-L / 2, L / 2, 100)
ax.plot(
    np.zeros_like(z), np.zeros_like(z), z, "r-", linewidth=2, label="Linha carregada"
)

# Ponto P
ax.scatter(*P, color="g", s=100, label="Ponto P")

# Vetores de campo elétrico
for num_cargas in num_cargas_list:
    E = campo_eletrico_cargas_pontuais(Q, L, P, num_cargas)
    ax.quiver(*P, *E, length=0.5, normalize=True, label=f"{num_cargas} cargas")

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Visualização 3D do campo elétrico")
ax.legend()
plt.show()

print("Análise dos resultados:")
print(
    "1. A solução analítica fornece o valor exato do campo elétrico para a linha uniformemente carregada."
)
print(
    "2. As soluções computacionais se aproximam da solução analítica à medida que aumentamos o número de cargas pontuais."
)
print("3. Com 30 cargas pontuais, obtemos uma boa aproximação do resultado analítico.")
print(
    "4. A diferença percentual diminui conforme aumentamos o número de cargas, indicando convergência para a solução exata."
)
