# Questão 12

import numpy as np
import matplotlib.pyplot as plt

# Constantes
k = 8.99e9  # Constante de Coulomb em N⋅m²/C²
Q = -1e-8  # Carga em Coulombs


def campo_eletrico(x, y, z):
    """
    Calcula o campo elétrico devido a uma carga pontual na origem.

    Parâmetros:
    x, y, z: Coordenadas do ponto onde o campo é calculado (em metros)

    Retorna:
    Vetor do campo elétrico (Ex, Ey, Ez) em N/C
    """
    r = np.array([x, y, z])
    r_mag = np.linalg.norm(r)
    return k * Q * r / r_mag**3


# Expressão simbólica para o campo elétrico
print("Questão 12 - Expressão para o campo elétrico:")
print("E = (k * Q / (x^2 + y^2 + z^2)^(3/2)) * [x, y, z]")
print(f"Onde k = {k:.2e} N⋅m²/C² e Q = {Q:.0e} C")

# Calcular o campo elétrico no ponto P(1, 1, 2)
P = np.array([1, 1, 2])
E_P = campo_eletrico(*P)

print("\nCampo elétrico no ponto P(1, 1, 2) m:")
print(f"E = {E_P} N/C")
print(f"Magnitude do campo elétrico: {np.linalg.norm(E_P):.4e} N/C")

# Visualização 3D
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection="3d")

# Criar uma grade de pontos
x = y = z = np.linspace(-3, 3, 10)
X, Y, Z = np.meshgrid(x, y, z)

# Calcular o campo elétrico em cada ponto da grade
Ex, Ey, Ez = campo_eletrico(X, Y, Z)
E_mag = np.sqrt(Ex**2 + Ey**2 + Ez**2)

# Normalizar os vetores para visualização
Ex_norm = Ex / E_mag
Ey_norm = Ey / E_mag
Ez_norm = Ez / E_mag

# Plotar os vetores de campo elétrico
ax.quiver(
    X, Y, Z, Ex_norm, Ey_norm, Ez_norm, length=0.5, normalize=True, color="b", alpha=0.6
)

# Plotar a carga na origem
ax.scatter(0, 0, 0, color="r", s=100, label="Carga Q")

# Plotar o ponto P
ax.scatter(*P, color="g", s=100, label="Ponto P(1,1,2)")

# Plotar o vetor de campo elétrico em P
ax.quiver(*P, *E_P, color="m", length=0.5, normalize=True, label="E em P")

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Visualização 3D do campo elétrico")
ax.legend()

plt.show()

print("\nAnálise dos resultados:")
print(
    "1. A expressão do campo elétrico mostra que ele varia com o inverso do quadrado da distância da carga."
)
print(
    "2. O campo elétrico aponta radialmente para fora da carga (já que Q é negativo)."
)
print(
    "3. No ponto P(1, 1, 2), o campo elétrico tem componentes em todas as três direções devido à posição assimétrica de P em relação à origem."
)
print(
    "4. A magnitude do campo elétrico em P é significativa devido à proximidade da carga."
)
print(
    "5. A visualização 3D mostra claramente como o campo elétrico se distribui no espaço ao redor da carga pontual."
)
print(
    "6. Os vetores de campo elétrico apontam radialmente para fora da carga em todas as direções, ilustrando a natureza central do campo elétrico de uma carga pontual."
)
