# game_data.py

historia = {
    # --- CENA INICIAL ---
    "inicio": {
        "texto": "Ano de 2061. A Terra está devastada após um vírus misterioso dizimar a humanidade. Você é um cientista sobrevivente, com memórias fragmentadas. Você acorda em um laboratório destruído. Sua cabeça lateja e pedaços da memória começam a voltar. O que você faz?",
        "imagem": "cena1_lab.png", 
        "opcoes": [
            {"texto": "Vasculha o laboratório em busca de pistas", "proxima_cena": "cena2a"},
            {"texto": "Sai imediatamente e procura seu antigo parceiro", "proxima_cena": "cena2b"}
        ]
    },

    # --- RAMO A: VASCULHAR O LABORATÓRIO ---
    "cena2a": {
        "texto": "Você encontra registros dos seus últimos experimentos, um estranho rádio comunicador e coordenadas de uma instalação militar. Você...",
        "imagem": "cena2a.png",
        "opcoes": [
            {"texto": "Seguir as coordenadas para a instalação militar", "proxima_cena": "cena3a"},
            {"texto": "Tentar contato com sobreviventes pelo rádio", "proxima_cena": "cena3b"}
        ]
    },

    # --- RAMO A.1: INSTALAÇÃO MILITAR ---
    "cena3a": {
        "texto": "A instalação está fortemente vigiada por drones do governo. Você...",
        "imagem": "cena3a.png",
        "opcoes": [
            {"texto": "Tentar se infiltrar furtivamente", "proxima_cena": "cena_infiltracao"},
            {"texto": "Recuar e procurar outro caminho", "proxima_cena": "final_neutro_captura"}
        ]
    },

    "cena_infiltracao": {
        "texto": "Você consegue entrar e ativa um alarme para chamar atenção dos guardas... Seu antigo parceiro aparece de repente, ele estava escondido ali. Ele oferece uma chance de usar a máquina do tempo que vocês trabalhavam juntos, porém instavel. Você aceita?",
        "imagem": "cena_infiltracao.png",
        "opcoes": [
            {"texto": "Sim, tentar mudar o passado", "proxima_cena": "final_ruim_passado"},
            {"texto": "Não, focar em criar a cura no presente", "proxima_cena": "final_bom_vacina_presente"}
        ]
    },

    # --- RAMO A.2: RÁDIO SOBREVIVENTES ---
    "cena3b": {
        "texto": "Você consegue sinal na rádio e recebe uma resposta. Uma comunidade secreta de sobreviventes te convida. Você...",
        "imagem": "cena3b.png",
        "opcoes": [
            {"texto": "Aceitar o convite e seguir para a comunidade", "proxima_cena": "final_bom_comunidade"},
            {"texto": "Desconfiar e decidir investigar mais este local...", "proxima_cena": "final_ruim_armadilha"}
        ]
    },

    # --- RAMO B: PROCURAR PARCEIRO ---
    "cena2b": {
        "texto": "Você parte em busca de seu antigo parceiro. Após horas, o encontra isolado, cercado de escombros estranhos. Ele revela que aperfeiçoou uma máquina do tempo instável. Você...",
        "imagem": "parceiro_maquina.png",
        "opcoes": [
            {"texto": "Concordar em usar a máquina (Impedir o vírus)", "proxima_cena": "cena_viagem_2020"},
            {"texto": "Sugerir trabalhar juntos na vacina no presente", "proxima_cena": "cena_trabalho_vacina"}
        ]
    },

    "cena_viagem_2020": {
        "texto": "Vocês ativam a máquina e viajam para 2020. Você encontra o laboratório onde tudo começou. O que fazer?",
        "imagem": "laboratorio_2020.png",
        "opcoes": [
            {"texto": "Destruir o laboratório imediatamente! Assim o virus nunca existirá", "proxima_cena": "final_bom_mudancas_historicas"},
            {"texto": "Roubar os dados e buscar outra solução", "proxima_cena": "final_excelente_governo"}
        ]
    },

    "cena_trabalho_vacina": {
        "texto": "Vocês começam a trabalhar na vacina. De repente, são atacados por agentes do governo que querem silenciá-los. Você...",
        "imagem": "ataque_agentes.png",
        "opcoes": [
            {"texto": "Lutar contra eles", "proxima_cena": "final_ruim_luta"},
            {"texto": "Fugir e tentar salvar os dados", "proxima_cena": "final_bom_resistencia"}
        ]
    },

    # ==========================================
    #                 FINAIS
    # ==========================================

    # Finais do Ramo A.1
    "final_ruim_passado": {
        "texto": "Vocês ativam a máquina... mas algo dá errado. Você é lançado para um futuro ainda pior, onde a humanidade já não existe. A tentativa de mudar o passado falhou e piorou tudo.",
        "imagem": "final_ruim_passado.png",
        "opcoes": [
            {"texto": ">","proxima_cena": "mission_failed"}
            ]
        #MISSION FAILED
    },

    "final_bom_vacina_presente": {
        "texto": "Vocês combinam esforços e usam os dados recuperados da base militar para sintetizar uma vacina. Após semanas de trabalho, conseguem imunizar um pequeno grupo. FINAL BOM: Um novo começo para a humanidade.",
        "imagem": "final_bom_vacina.png",
        "opcoes": [] # Lista vazia = Fim de Jogo
    },

    "final_neutro_captura": {
        "texto": "Ao tentar fugir, você é capturado pelos drones do governo. Eles te levam para um centro de interrogatório. Você sobrevive, mas perde sua liberdade.",
        "imagem": "final_neutro_preso.png",
        "opcoes": [
            {"texto": ">", "proxima_cena": "mission_failed"}
            ]
        #MISSION FAILED

    },

    # Finais do Ramo A.2
    "final_bom_comunidade": {
        "texto": "Chegando lá, você descobre que eles estão trabalhando em uma cura coletiva. Com sua ajuda, aceleram o processo e salvam centenas de pessoas. Uma chance real de reconstruir a civilização.",
        "imagem": "final_bom_comunidade.png",
        "opcoes": []
    },

    "final_ruim_armadilha": {
        "texto": "Você descobre que este local era uma armadilha dos soldados do governo. Você é capturado e nunca mais ouvido. A busca pela verdade te custou a liberdade.",
        "imagem": "final_ruim_armadilha.png",
        "opcoes": [{"texto": ">", "proxima_cena": "mission_failed"}]
         #MISSION FAILED
    },

    # Finais do Ramo B
    "final_bom_mudancas_historicas": {
        "texto": "A explosão impede o surgimento do vírus, mas.....",
        "imagem": "final_incerto.png",
        "opcoes": [{"texto": ">", "proxima_cena": "final_incerto1"}]
    },

    "final_incerto1": {
        "texto": ".........",
        "imagem": "final_incerto.png",
        "opcoes": [{"texto": ">", "proxima_cena": "final_incerto2"}]
    },

    "final_incerto2": {
        "texto": ".........",
        "imagem": "final_incerto.png",
        "opcoes": []
    },

    "final_excelente_governo": {
        "texto": "Você descobre que o vírus não foi um acidente, mas sim uma arma. Ao retornar, traz dados suficientes para expor e derrubar o governo autoritário. Você não só salva a humanidade, como também liberta as pessoas da opressão.",
        "imagem": "final_excelente_midia.png",
        "opcoes": [{"texto": ">", "proxima_cena": "final_excelente_governo1"}]
    },

    "final_excelente_governo1": {
        "texto": ".........",
        "imagem": "final_excelente_governo1.png",
        "opcoes": [{"texto": ">", "proxima_cena": "final_excelente_governo2"}]
    },

    "final_excelente_governo2": {
        "texto": ".........",
        "imagem": "final_excelente_governo2.png",
        "opcoes": []
    },

    "final_ruim_luta": {
        "texto": "A luta é intensa, mas vocês são capturados. Os dados são destruídos. O governo vence, e a esperança morre com vocês.",
        "imagem": "final_ruim_derrota.png",
        "opcoes": [{"texto": ">", "proxima_cena": "mission_failed"}]
        #MISSION FAILED
    },

    "final_bom_resistencia": {
        "texto": "Você foge levando os dados e consegue transmiti-los para outros grupos de resistência...",
        "imagem": "final_bom_fuga_dados.png",
        "opcoes": [{"texto": ">", "proxima_cena": "final_bom_resistencia1"}]
    },

    "final_bom_resistencia1": {
        "texto": "Graças a você, a cura é desenvolvida por cientistas escondidos. FINAL BOM: A humanidade sobrevive e o governo perde força.",
        "imagem": "final_bom_fuga_dados1.png",
        "opcoes": []
    },

     "mission_failed": {
        "texto": "se deu mal...",
        "imagem": "mission_failed.jpg",
        "opcoes": []
    },

    
}