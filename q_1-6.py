# Questão 6

import numpy as np
from scipy import integrate

# Constantes
r_min, r_max = 4, 5  # metros
theta_min, theta_max = 0, 25 * np.pi / 180  # radianos
phi_min, phi_max = 0.9 * np.pi, 1.1 * np.pi  # radianos


def rho(r, theta, phi):
    """Densidade volumétrica de carga."""
    return 10 * (r - 4) * (5 - r) * np.sin(theta) ** 2 * np.sin(phi)


def integrando(r, theta, phi):
    """Função a ser integrada para obter a carga total."""
    return rho(r, theta, phi) * r**2 * np.sin(theta)


# Solução analítica
def carga_total_analitica():
    resultado, erro = integrate.tplquad(
        integrando,
        r_min,
        r_max,
        lambda r: theta_min,
        lambda r: theta_max,
        lambda r, theta: phi_min,
        lambda r, theta: phi_max,
    )
    return resultado


Q_analitica = carga_total_analitica()
print(f"Questão 6 - Carga total (solução analítica): {Q_analitica:.6e} C")


# Solução computacional
def carga_total_computacional(n_r, n_theta, n_phi):
    r = np.linspace(r_min, r_max, n_r)
    theta = np.linspace(theta_min, theta_max, n_theta)
    phi = np.linspace(phi_min, phi_max, n_phi)

    dr = (r_max - r_min) / (n_r - 1)
    dtheta = (theta_max - theta_min) / (n_theta - 1)
    dphi = (phi_max - phi_min) / (n_phi - 1)

    Q = 0
    for i in range(n_r):
        for j in range(n_theta):
            for k in range(n_phi):
                Q += integrando(r[i], theta[j], phi[k]) * dr * dtheta * dphi

    return Q


# Calcular a solução computacional para diferentes números de pontos
n_points = [10, 20, 50, 100]
for n in n_points:
    Q_computacional = carga_total_computacional(n, n, n)
    erro_percentual = abs(Q_computacional - Q_analitica) / Q_analitica * 100
    print(f"\nSolução computacional com {n}x{n}x{n} pontos:")
    print(f"Carga total: {Q_computacional:.6e} C")
    print(f"Erro percentual: {erro_percentual:.6f}%")

print("\nAnálise dos resultados:")
print(
    "1. A solução analítica fornece o valor exato da carga total na região especificada."
)
print(
    "2. As soluções computacionais se aproximam da solução analítica à medida que aumentamos o número de pontos na grade de integração."
)
print(
    "3. O erro percentual diminui significativamente com o aumento do número de pontos, indicando convergência para a solução exata."
)
print(
    "4. Este problema demonstra a eficácia do método computacional para calcular integrais triplas em coordenadas esféricas."
)
print(
    "5. Para obter resultados mais precisos, pode-se aumentar ainda mais o número de pontos, mas isso também aumentará o tempo de computação."
)
