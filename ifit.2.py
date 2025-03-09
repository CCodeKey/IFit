
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# Dados de treinamento ajustados (15 exemplos para 15 categorias)
dados_treinamento = np.array([
    [25, 170, 60, 2, 3, 0, 0, 1, 60],
    [30, 180, 70, 2, 4, 1, 2, 3, 90],
    [20, 160, 50, 1, 2, 0, 0, 1, 30],
    [40, 190, 80, 2, 5, 0, 1, 4, 60],
    [35, 175, 65, 1, 3, 1, 4, 1, 90],
    [28, 165, 58, 2, 2, 2, 1, 4, 45],
    [22, 170, 55, 1, 3, 0, 2, 2, 50],
    [38, 185, 85, 2, 4, 1, 3, 1, 70],
    [26, 175, 67, 1, 2, 3, 5, 2, 40],
    [45, 180, 78, 2, 5, 4, 6, 2, 80],
    [32, 168, 60, 1, 3, 1, 7, 1, 60],
    [29, 175, 73, 2, 4, 2, 2, 4, 90],
    [50, 178, 80, 2, 5, 3, 3, 1, 75],
    [24, 165, 54, 1, 1, 0, 8, 3, 30],
    [36, 182, 77, 2, 4, 4, 1, 2, 85]
])

# Criando etiquetas de treinamento (0 a 14)
etiquetas_treinamento = np.arange(15)  

# Divisão dos dados em treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(
    dados_treinamento, etiquetas_treinamento, test_size=0.2, random_state=42
)

# Normalização dos dados
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Criação e treinamento do modelo
modelo = LogisticRegression(max_iter=1000)
modelo.fit(X_train, y_train)

# Avaliação do modelo
y_pred = modelo.predict(X_test)
acuracia = accuracy_score(y_test, y_pred)
print(f"Acurácia do modelo: {acuracia:.2f}")

# Coleta de dados do usuário com validação
def entrada_usuario_valida(mensagem, tipo=int, minimo=None, maximo=None):
    while True:
        try:
            valor = tipo(input(mensagem))
            if minimo is not None and valor < minimo:
                raise ValueError(f"Digite um valor maior ou igual a {minimo}.")
            if maximo is not None and valor > maximo:
                raise ValueError(f"Digite um valor menor ou igual a {maximo}.")
            return valor
        except ValueError as e:
            print(f"Entrada inválida: {e}")

idade = entrada_usuario_valida("Digite sua idade: ", int, 10, 100)
altura = entrada_usuario_valida("Digite sua altura (em cm): ", int, 100, 250)
peso = entrada_usuario_valida("Digite seu peso (em kg): ", int, 30, 200)
sexo = entrada_usuario_valida("Digite seu sexo (1 = Masculino, 2 = Feminino): ", int, 1, 2) - 1
nivel_atividade = entrada_usuario_valida("Digite seu nível de atividade física (1 a 5): ", int, 1, 5)
objetivo = entrada_usuario_valida("Digite seu objetivo (0 a 4): ", int, 0, 4)
condicoes_medicas = entrada_usuario_valida("Digite suas condições médicas (0 a 8): ", int, 0, 8)
local_treino = entrada_usuario_valida("Digite seu local de treino (1 a 4): ", int, 1, 4) - 1
duracao_treino = entrada_usuario_valida("Digite a duração do seu treino (em minutos): ", int, 10, 180)

# Normalização da entrada do usuário
entrada_usuario = scaler.transform([[idade, altura, peso, sexo, nivel_atividade, objetivo, condicoes_medicas, local_treino, duracao_treino]])

# Previsão do método de treino
def prever_metodo_treino():
    previsao = modelo.predict(entrada_usuario)
    return min(max(previsao[0], 0), 14)  # Garante que esteja entre 0 e 14

# Métodos de treino organizados
metodos_treino = {
    0: "Treino de força para iniciantes: exercícios básicos para musculatura.",
    1: "Treino de força para intermediários: carga moderada e progressão.",
    2: "Treino de força para avançados: cargas altas e técnicas avançadas.",
    3: "Treino de condicionamento físico para iniciantes: caminhadas e aeróbicos leves.",
    4: "Treino de condicionamento físico para intermediários: corridas curtas, circuitos funcionais.",
    5: "Treino de condicionamento físico para avançados: treinos intervalados intensos.",
    6: "Treino de resistência para iniciantes: exercícios básicos de resistência muscular.",
    7: "Treino de resistência para intermediários: aumento gradual da carga e tempo sob tensão.",
    8: "Treino de resistência para avançados: treinos com alta repetição e baixa recuperação.",
    9: "Treino de flexibilidade e mobilidade: melhora da amplitude de movimento.",
    10: "Treino de equilíbrio e coordenação: foco na estabilidade corporal.",
    11: "Treino funcional de alta intensidade: mistura de resistência, força e cardio.",
    12: "Treino de calistenia: fortalecimento com exercícios de peso corporal.",
    13: "Treino de ioga e pilates: fortalecimento, alongamento e equilíbrio mental.",
    14: "Treino personalizado com acompanhamento profissional."
}

# Exibição do resultado
metodo_treino = prever_metodo_treino()
print(f"\nO método de treino ideal para você é:\n{metodos_treino[metodo_treino]}")