import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

def modelo_de_linguagem(P_altura, P_peso, P_nivel_atividade, P_objetivo, P_condicao_medica, P_local_treino, P_duracao_treino, P_sexo, P_idade):
    # Criando um dataset simulado baseado nas categorias fornecidas
    dados_treinamento = pd.DataFrame([
        [25, 170, 60, "masculino", "iniciante", "emagrecimento", "saudavel", "academia", 60, "Treino de Força",
        '''começe com um aquecimento,faça uma caminhada de 10 minutos e logo em seguida faça 3 series de polichinelos com duas a cinco repetiçôes.
        agachamentos:3 series de 10-12 repetições.
        flexões:3 series ate a falha.
        Remana com halteres:3 séries de 10-12 repetições.
        prancha:3 séries,segurando por 15 segundos.
        elevação de panturilhas:3 séries de 15-20 repetições.
        faça esse treino 3 vezes por semana,com descanso de 1 dia entre os treinos.,
        ''',"https://exemplo.com"],
        
        [30, 180, 70, "masculino", "intermediario", "ganhar_massa_muscular", "saudavel", "academia", 90, "Treino de Hipertrofia",
        '''dia 1:superior(peito/triceps/ombros)
        supino reto:3 séries de 8-12 repetições.
        treino com halteres:3 séries de 10-15 repetições.
        dia 2:inferior(pernas/panturrilhas)
        agachamento livre:3 séries de 8-12 repetições.
        leg press:3 series de 10-15 repetições.
        panturrilha em pé:3 séries de 15-20 repetições.
        dia 3:costas/biceps
        barra fixa: 3 séries ate a falha.
        remada curvada:3 séries de 8-12 repetições.
        Rosca direita com barra:3 séries de 8-12 repetições.
        Rosca martelo:3 series de 10-15 repetições.
        Observação:Este treino é um exemplo.Ajuste-o de acordo com suas necessidades e objetivos.Se possivel,consulte um profissional de educação fisica para orientação personalizada.,
        ''',"https://exemplo.com"],
        
        [20, 160, 50, "feminino", "sedentario", "emagrecimento", "saudavel", "casa", 30, "Treino Cardio",
        '''aquecimento(5 minutos) caminhada leve no lugar:2 minutos,elevando os joelhos gradualmente.
        rotação de braços e pernas:1 minuto para frente e 1 minuto para tras.
        alongamento suave dos principais grupos musculares.
        treino(3 vezes por semana,com descanço de 1 dia entre os treinos)
        caminhada:20-30 minutos em ritmo moderado.
        polichinelos:3 séries de 15 repetições.
        Observação:Este treino é um exemplo.Ajuste-o de acordo com suas necessidades e objetivos.Se possivel,consulte um profissional de educação fisica para orientação personalizada.,
        ''',"https://exemplo.com"],
        
        [40, 190, 80, "masculino", "avancado", "ganhar_massa_muscular", "saudavel", "academia", 60, "Treino de Força Máxima",
        '''caracteristicas do treino:
        Cargas elevadas:utiliza-se pesos proximos ou iguais a sua 1RM(uma repetição maxima).
        baixas repetições:geralmente 1 a 5 repetições por serie.
        longos periodos de descanço:3 a 5 minutos entre as séries para recuperação completa.
        tecnica impecavel:A forma correta é crucial para evitar lesões e maximizar os resultados.
        TREINO:
        aquecimento:10-15 minutos de cardio leve e alongamentos dinâmicos.
        agachamento livre:3 series de 3-6 repetições com carga maxima.
        supino reto:3 séries de 3-5 repetições com carga maxima.
        levantamento terra:1 serie de 1-3 repetições com carga maxima.
        desenvolvimento com barra:3 series de 3-5 repetições com carga maxima.
        Observação:Este treino é um exemplo.Ajuste-o de acordo com suas necessidades e objetivos.Se possivel,consulte um profissional de educação fisica para orientação personalizada.,
        ''',"https://exemplo.com"],
        
        [35, 175, 65, "feminino", "intermediario", "melhora_na_saude", "saudavel", "parque", 90, "Treino Funcional",
        '''O treino funcional trabalha força,resistência,equilibrio,flexibilidade e coordenação motora.
        Treino:
        Aquecimento: 5-10 minutos de caminhada leve, corrida e alongamentos dinâmicos.
        Agachamentos: 3 séries de 10-12 repetições.Flexões em um banco: 3 séries de quantas repetições conseguir.
        Barra fixa: 3 séries de quantas repetições conseguir.
        Saltos em um banco: 3 séries de 10-12 repetições.
        Observação:Este treino é um exemplo.Ajuste-o de acordo com suas necessidades e objetivos.Se possivel,consulte um profissional de educação fisica para orientação personalizada.,
        ''',"https://exemplo.com"],
        
        [50, 165, 58, "masculino", "iniciante", "condicionamento", "diabetes", "academia", 45, "Treino de Resistência",
        '''Exercícios de longa duração com baixa carga"
        , "O treino de resistência desenvolve um bom Condicionamento Físico, conbinado com o ganho de força e controle glicêmico.
        Treino: 
        Agachamento: 3 séries com duração de 30 segundos com um intervalo de 15 segundos. 
        Flexões: 3 séries até a falha com intervalo de 30 segundos.
            Remadas: 3 séries com elástico ou algum peso compatível, com intervalo de 30 segundos. 
            Prancha e Polichinelo: 3 séries de 30 a 45 segundos com intervalo de 15 segundos.
            Observação:Este treino é um exemplo. Ajuste-o de acordo com suas necessidades e objetivos.Se possivel,consulte um profissional de educação fisica para orientação personalizada.,
            ''',"https://exemplo.com"], 
        
        [60, 170, 70, "feminino", "sedentario", "melhora_na_saude", "problemas_cardiacos", "casa", 50, "Treino de Mobilidade",
        '''Alongamentos e exercícios leves para articulações","o treio de mobilidade é essencial para melhorar a flexibilidade, reduz dores nas articulações e auxilia no em moviemntos do cotidiano.
        Treino: 
        Aquecimento: 5-10 minutos de csminhada no ambiente.
        Alongamento na cadeira: Sente-se e estique as pernas alternando em 3 séries de 10 repetições.
            Mobilidade de ombro: Elevação e rotação dos ombros para frente e para trás, faça 3 séries de 10 repetições.
            Flexão lateral do tronco: Incline-se suavemente para cada lado, realize 3 séries de 10 repetições.
            Mobilidade do quadril: Coloque as mãos na cintura e faça o movimento de rotação do quadril para frente, para trás, para a direita e para a esquerda, realize 3 séries de 10 repetições.
            Observação:Este treino é um exemplo. Ajuste-o de acordo com suas necessidades e objetivos.Se possivel,consulte um profissional de educação fisica para orientação personalizada.,
            ''',"https://exemplo.com"],
        
        [28, 175, 65, "feminino", "intermediario", "outro", "coluna", "academia", 70, "Treino de Core", 
        '''Fortalecimento abdominal e lombar para suporte da coluna.
        Treino:
        Aquecimento: 5 minutos de caminhada leve na esteira.
        Prancha: 3 séries de 30 a 60 segundos(Fortalece o core).
        Ponte: 3 séries de 15 a 20 repetições(Fortalece glúteos e lombar).
        Dead Bug: 3 séries de 10 repetições para cada lado(Fortalece o core e melhora a coordenação).
        Prancha Lateral: 3 séries de 30 segundos(Fortalece o Obliquos e os estabilizadores laterais).
        Observação:Este treino é um exemplo. Ajuste-o de acordo com suas necessidades e objetivos. Se possivel, consulte um profissional de educação fisica para orientação personalizada.,
        ''',"https://exemplo.com" ],
        
        [26, 180, 75, "masculino", "avancado", "condicionamento", "saudavel", "parque", 60, "Treino de condicionamento fisico", 
        '''Treino intervalado de alta intensidade para explosão muscular.
        Treino:
            Aquecimento : Polichinelos por 60 segundos. Rotação de braços por 30 segundos. Agachamento livre 30 repetições.
            Sprints em subida: 30 segundos de sprint máximo, 30 segundos de descanso (repetir 6 vezes). 
            Saltos no banco do parque: 10 repetições, seguido de 30 segundos de descanso (repetir 4 vezes). 
            Flexões: Máximo de repetições possíveis em 30 segundos, seguido de 30 segundos de descanso (repetir 4 vezes).
            Barra fixa: Máximo de repetições possíveis, seguido de 1 minuto de descanso, repetir 3 vezes.
            Observação:Este treino é um exemplo. Ajuste-o de acordo com suas necessidades e objetivos. Se possivel, consulte um profissional de educação fisica para orientação personalizada.,
            ''',"https://exemplo.com"],
        
        [45, 180, 78, "feminino", "avancado", "condicionamento", "saudavel", "academia", 80, "Treino de alta intencidade", 
        '''Plano adaptado às necessidades individuais.

        treino:
            Aquecimento: Pular corda por 3 minutos(descansa 45 segundos). Polichinelos com saltos por 30 segundos(Descansa 30 segundos). Agachamentos livre 15 repetições(descansa 30 segundos).
            Burpees com salto na caixa:3 séries de 10 repetições(Descansa 30 segundos entre as séries e para o próximo exercício). 
            Agachamento com barra (peso desafiador): 3 séries de 12 repetições(Descansa 30 segundos entre as séries e para o próximo exercício). 
            Remada alta: 3 séries de 15 repetições(Descansa 30 segundos entre as séries e para o próximo exercício). 
            Prancha com rotação de quadril: 3 séries de 20 repetições - 10 para cada lado (Descansa 30 segundos entre as séries).
            Sprints na esteira (ou bike): 8 séries de 20 segundos de sprint máximo, 10 segundos de descanso.
            Observação:Este treino é um exemplo. Ajuste-o de acordo com suas necessidades e objetivos. Se possivel, consulte um profissional de educação fisica para orientação personalizada.,
            ''',"https://exemplo.com"],
        
    ],  columns=["Idade", "Altura", "Peso", "Sexo", "Nível Atividade", "Objetivo", "Condição Médica", "Local Treino", "Duração", "Método Treino", "Descrição","link"])

    # Transformando dados categóricos em números
    label_encoders = {}
    for col in ["Sexo", "Nível Atividade", "Objetivo", "Condição Médica", "Local Treino", "Método Treino"]:
        le = LabelEncoder()
        dados_treinamento[col] = le.fit_transform(dados_treinamento[col])
        label_encoders[col] = le

    # Separando os dados de entrada e saída
    X = dados_treinamento.drop(columns=["Método Treino", "Descrição","link"])
    y = dados_treinamento["Método Treino"]


    # Divisão treino/teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Modelo de Machine Learning (Random Forest)
    modelo = RandomForestClassifier(n_estimators=100, random_state=42)
    modelo.fit(X_train, y_train)



    # Função para entrada do usuário
    def entrada_usuario_valida(mensagem, tipo=str, opcoes=None):
        while True:
            valor = input(mensagem).strip()
            if tipo == int:
                try:
                    return int(valor)
                except ValueError:
                    print("Por favor, insira um número válido.")
            elif opcoes:
                valor_lower = valor.lower()
                opcoes_lower = [op.lower() for op in opcoes]
                if valor_lower in opcoes_lower:
                    return opcoes[opcoes_lower.index(valor_lower)]  # Retorna na formatação original
                else:
                    print(f"Opção inválida. Escolha entre: {', '.join(opcoes)}")
            else:
                return valor

    # Coletando dados do usuário
    idade = int(P_idade)
    altura = P_altura
    peso = P_peso
    sexo = P_sexo
    nivel_atividade = P_nivel_atividade
    objetivo = P_objetivo
    condicao_medica = P_condicao_medica
    local_treino = P_local_treino
    duracao_treino = P_duracao_treino

    # Convertendo entrada do usuário para formato do modelo
    entrada_usuario = np.array([
        idade, altura, peso,
        label_encoders["Sexo"].transform([sexo])[0],
        label_encoders["Nível Atividade"].transform([nivel_atividade])[0],
        label_encoders["Objetivo"].transform([objetivo])[0],
        label_encoders["Condição Médica"].transform([condicao_medica])[0],
        label_encoders["Local Treino"].transform([local_treino])[0],
        duracao_treino
    ]).reshape(1, -1)

    # Criando o dicionário para associar as codificações numéricas aos métodos, descrições e links

    descricao_treino = dict(zip(dados_treinamento["Método Treino"], dados_treinamento["Descrição"]))
    link_treino = dict(zip(dados_treinamento["Método Treino"], dados_treinamento["link"]))

    # Função para obter o treino recomendado
    previsao_codificada = modelo.predict(entrada_usuario)[0]

    # Verifique a previsão e use diretamente a chave codificada
    if previsao_codificada in descricao_treino:
        descricao = descricao_treino[previsao_codificada]
        link = link_treino[previsao_codificada]

        # Realize a inversão para o nome do método de treino
        metodo_treino = label_encoders["Método Treino"].inverse_transform([previsao_codificada])[0]

        return [metodo_treino, descricao, link]
    else:
        metodo_treino = "Erro"
        descricao = "O método de treino previsto não foi encontrado nos dados."
        link = ""
        return [metodo_treino, descricao, link]