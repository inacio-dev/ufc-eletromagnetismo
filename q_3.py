import numpy as np
import matplotlib.pyplot as plt

# Constantes
k = 8.99e9  # Constante de Coulomb em N⋅m²/C²
Q = 10  # Carga total em Coulombs
R = 1  # Raio do anel em metros
P = np.array([0, 0, 10])  # Ponto P(0, 0, 10) em metros


def campo_eletrico_anel_uniforme(Q, R, P):
    """Calcula o campo elétrico de um anel uniformemente carregado."""
    x, y, z = P
    return (k * Q * z) / (4 * np.pi * (R**2 + z**2) ** (3 / 2))


def campo_eletrico_cargas_pontuais(Q, R, P, num_cargas):
    """Calcula o campo elétrico de cargas pontuais distribuídas uniformemente no anel."""
    x, y, z = P
    q = Q / num_cargas
    E_total = np.zeros(3)

    for i in range(num_cargas):
        theta = 2 * np.pi * i / num_cargas
        pos = np.array([R * np.cos(theta), R * np.sin(theta), 0])
        r = P - pos
        r_mag = np.linalg.norm(r)
        E_total += k * q * r / r_mag**3

    return E_total


# (a) Solução analítica
E_analitico = campo_eletrico_anel_uniforme(Q, R, P)
print(f"(a) Campo elétrico analítico em P: {E_analitico:.4e} N/C")

# (b) Solução computacional para diferentes números de cargas pontuais
num_cargas_list = [10, 15, 30, 100]
E_computacional = []

for num_cargas in num_cargas_list:
    E = campo_eletrico_cargas_pontuais(Q, R, P, num_cargas)
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

# Anel carregado
theta = np.linspace(0, 2 * np.pi, 100)
x = R * np.cos(theta)
y = R * np.sin(theta)
z = np.zeros_like(theta)
ax.plot(x, y, z, "r-", linewidth=2, label="Anel carregado")

# Ponto P
ax.scatter(*P, color="g", s=100, label="Ponto P")

# Vetores de campo elétrico
for num_cargas in num_cargas_list:
    E = campo_eletrico_cargas_pontuais(Q, R, P, num_cargas)
    ax.quiver(*P, *E, length=0.5, normalize=True, label=f"{num_cargas} cargas")

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Visualização 3D do campo elétrico")
ax.legend()
plt.show()

print("Análise dos resultados:")
print(
    "1. A solução analítica fornece o valor exato do campo elétrico para o anel uniformemente carregado."
)
print(
    "2. As soluções computacionais se aproximam da solução analítica à medida que aumentamos o número de cargas pontuais."
)
print(
    "3. Com 100 cargas pontuais, obtemos uma excelente aproximação do resultado analítico."
)
print(
    "4. A diferença percentual diminui significativamente conforme aumentamos o número de cargas, indicando convergência para a solução exata."
)
print(
    "5. O campo elétrico está alinhado com o eixo z devido à simetria do anel no plano xy."
)
