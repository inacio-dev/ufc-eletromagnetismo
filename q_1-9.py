# Questão 9

import numpy as np
from scipy import integrate


def carga_linha(x):
    """Densidade linear de carga para o item (a)."""
    return 12 * x**2 * 1e-3  # mC/m para C/m


def carga_superficie(z):
    """Densidade superficial de carga para o item (b)."""
    return z**2 * 1e-9  # nC/m^2 para C/m^2


def carga_volume(r, theta):
    """Densidade volumétrica de carga para o item (c)."""
    return r * np.sin(theta)  # C/m^3


# Item (a)
def integrand_a(x):
    return carga_linha(x)


Q_a_analitico, _ = integrate.quad(integrand_a, 0, 5)

print("Questão 9 - Item (a):")
print(f"Carga total na linha (analítico): {Q_a_analitico:.6e} C")


# Solução computacional para (a)
def Q_a_computacional(n):
    x = np.linspace(0, 5, n)
    dx = 5 / (n - 1)
    return np.sum(carga_linha(x) * dx)


for n in [100, 1000, 10000]:
    Q_a_comp = Q_a_computacional(n)
    erro_a = abs(Q_a_comp - Q_a_analitico) / Q_a_analitico * 100
    print(f"Carga total (computacional, n={n}): {Q_a_comp:.6e} C, Erro: {erro_a:.6f}%")


# Item (b)
def integrand_b(z, phi):
    return carga_superficie(z) * 3  # raio do cilindro = 3m


Q_b_analitico, _ = integrate.dblquad(
    integrand_b, 0, 2 * np.pi, lambda phi: 0, lambda phi: 4
)

print("\nQuestão 9 - Item (b):")
print(f"Carga total na superfície cilíndrica (analítico): {Q_b_analitico:.6e} C")


# Solução computacional para (b)
def Q_b_computacional(n):
    z = np.linspace(0, 4, n)
    phi = np.linspace(0, 2 * np.pi, n)
    Z, PHI = np.meshgrid(z, phi)
    dz = 4 / (n - 1)
    dphi = 2 * np.pi / (n - 1)
    return np.sum(carga_superficie(Z) * 3 * dz * dphi)


for n in [100, 1000, 10000]:
    Q_b_comp = Q_b_computacional(n)
    erro_b = abs(Q_b_comp - Q_b_analitico) / Q_b_analitico * 100
    print(
        f"Carga total (computacional, n={n}x{n}): {Q_b_comp:.6e} C, Erro: {erro_b:.6f}%"
    )


# Item (c)
def integrand_c(r, theta, phi):
    return carga_volume(r, theta) * r**2 * np.sin(theta)


Q_c_analitico, _ = integrate.tplquad(integrand_c, 0, 2 * np.pi, 0, np.pi, 0, 4)

print("\nQuestão 9 - Item (c):")
print(f"Carga total no volume esférico (analítico): {Q_c_analitico:.6e} C")


# Solução computacional para (c)
def Q_c_computacional(n):
    r = np.linspace(0, 4, n)
    theta = np.linspace(0, np.pi, n)
    phi = np.linspace(0, 2 * np.pi, n)
    R, THETA, PHI = np.meshgrid(r, theta, phi)
    dr = 4 / (n - 1)
    dtheta = np.pi / (n - 1)
    dphi = 2 * np.pi / (n - 1)
    return np.sum(carga_volume(R, THETA) * R**2 * np.sin(THETA) * dr * dtheta * dphi)


for n in [50, 100, 200]:
    Q_c_comp = Q_c_computacional(n)
    erro_c = abs(Q_c_comp - Q_c_analitico) / Q_c_analitico * 100
    print(
        f"Carga total (computacional, n={n}x{n}x{n}): {Q_c_comp:.6e} C, Erro: {erro_c:.6f}%"
    )

print("\nAnálise dos resultados:")
print(
    "1. Para todos os itens, as soluções computacionais convergem para as soluções analíticas à medida que aumentamos o número de pontos."
)
print("2. O item (a) converge mais rapidamente devido à sua natureza unidimensional.")
print(
    "3. O item (b) requer mais pontos para uma precisão comparável devido à integração bidimensional."
)
print(
    "4. O item (c) é o mais computacionalmente intensivo devido à integração tridimensional, mas ainda assim converge para a solução analítica."
)
print(
    "5. Este problema demonstra a eficácia dos métodos computacionais para calcular cargas totais em diferentes geometrias e dimensões."
)
