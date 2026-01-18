# game_data.py

historia = {
    # --- CENA INICIAL ---
    "inicio": {
        "texto": "Ano de 2061. A Terra está devastada após um vírus misterioso dizimar a humanidade. Você é um cientista sobrevivente, com memórias fragmentadas. Você acorda em um laboratório destruído. Sua cabeça lateja e pedaços da memória começam a voltar. Primeira decisão: O que você faz?",
        "imagem": "01_laboratorio_destruido.jpg", 
        "opcoes": [
            {"texto": "Vasculhar o laboratório em busca de pistas", "proxima_cena": "cena_busca_lab"},
            {"texto": "Sair imediatamente e procurar seu antigo parceiro", "proxima_cena": "cena_procurar_parceiro"}
        ]
    },

    # --- RAMO A: VASCULHAR O LABORATÓRIO ---
    "cena_busca_lab": {
        "texto": "Você encontra registros dos seus últimos experimentos, um estranho rádio comunicador e coordenadas de uma instalação militar. Segunda decisão: Você...",
        "imagem": "02_radio_coordenadas.jpg",
        "opcoes": [
            {"texto": "Seguir as coordenadas para a instalação militar", "proxima_cena": "cena_instalacao_militar"},
            {"texto": "Tentar contato com sobreviventes pelo rádio", "proxima_cena": "cena_radio_sobreviventes"}
        ]
    },

    # --- RAMO A.1: INSTALAÇÃO MILITAR ---
    "cena_instalacao_militar": {
        "texto": "A instalação está fortemente vigiada por drones do governo. Terceira decisão: Você...",
        "imagem": "03_drones_governo.jpg",
        "opcoes": [
            {"texto": "Tentar se infiltrar furtivamente", "proxima_cena": "cena_infiltracao"},
            {"texto": "Recuar e procurar outro caminho", "proxima_cena": "final_neutro_captura"}
        ]
    },

    "cena_infiltracao": {
        "texto": "Você consegue entrar, mas ativa um alarme. Seu antigo parceiro aparece de repente, ele estava escondido ali. Ele oferece uma chance de usar a máquina do tempo. Quarta decisão: Você aceita?",
        "imagem": "04_encontro_parceiro_alarme.jpg",
        "opcoes": [
            {"texto": "Sim, tentar mudar o passado", "proxima_cena": "final_ruim_passado"},
            {"texto": "Não, focar em criar a cura no presente", "proxima_cena": "final_bom_vacina_presente"}
        ]
    },

    # --- RAMO A.2: RÁDIO SOBREVIVENTES ---
    "cena_radio_sobreviventes": {
        "texto": "Você consegue sinal na rádio e recebe uma resposta. Uma comunidade secreta de sobreviventes te convida. Terceira decisão: Você...",
        "imagem": "05_radio_comunicacao.jpg",
        "opcoes": [
            {"texto": "Aceitar o convite e seguir para a comunidade", "proxima_cena": "final_bom_comunidade"},
            {"texto": "Desconfiar e decidir investigar mais", "proxima_cena": "final_ruim_armadilha"}
        ]
    },

    # --- RAMO B: PROCURAR PARCEIRO ---
    "cena_procurar_parceiro": {
        "texto": "Você parte em busca de seu antigo parceiro. Após horas, o encontra isolado, cercado de equipamentos estranhos. Ele revela que aperfeiçoou uma máquina do tempo instável. Segunda decisão: Você...",
        "imagem": "06_parceiro_maquina.jpg",
        "opcoes": [
            {"texto": "Concordar em usar a máquina (Impedir o vírus)", "proxima_cena": "cena_viagem_2020"},
            {"texto": "Sugerir trabalhar juntos na vacina no presente", "proxima_cena": "cena_trabalho_vacina"}
        ]
    },

    "cena_viagem_2020": {
        "texto": "Vocês ativam a máquina e viajam para 2020. Vocês encontram o laboratório onde tudo começou. Terceira decisão: O que fazer?",
        "imagem": "07_laboratorio_2020.jpg",
        "opcoes": [
            {"texto": "Destruir o laboratório imediatamente", "proxima_cena": "final_bom_mudancas_historicas"},
            {"texto": "Roubar os dados e buscar outra solução", "proxima_cena": "final_excelente_governo"}
        ]
    },

    "cena_trabalho_vacina": {
        "texto": "Vocês começam a trabalhar na vacina. De repente, são atacados por agentes do governo que querem silenciá-los. Terceira decisão: Você...",
        "imagem": "08_ataque_agentes.jpg",
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
        "texto": "Vocês ativam a máquina... mas algo dá errado. Você é lançado para um futuro ainda pior, onde a humanidade já não existe. FINAL RUIM: A tentativa de mudar o passado falhou e piorou tudo.",
        "imagem": "final_ruim_futuro_pior.jpg",
        "opcoes": [] # Lista vazia = Fim de Jogo
    },

    "final_bom_vacina_presente": {
        "texto": "Vocês combinam esforços e usam os dados recuperados para sintetizar uma vacina. Após semanas de trabalho, conseguem imunizar um pequeno grupo. FINAL BOM: Um novo começo para a humanidade.",
        "imagem": "final_bom_vacina.jpg",
        "opcoes": []
    },

    "final_neutro_captura": {
        "texto": "Ao tentar fugir, você é capturado pelos drones do governo. Eles te levam para um centro de interrogatório. FINAL NEUTRO: Você sobrevive, mas perde sua liberdade.",
        "imagem": "final_neutro_preso.jpg",
        "opcoes": []
    },

    # Finais do Ramo A.2
    "final_bom_comunidade": {
        "texto": "Chegando lá, você descobre que eles estão trabalhando em uma cura coletiva. Com sua ajuda, aceleram o processo e salvam centenas de pessoas. FINAL BOM: Uma chance real de reconstruir a civilização.",
        "imagem": "final_bom_comunidade.jpg",
        "opcoes": []
    },

    "final_ruim_armadilha": {
        "texto": "Você descobre que era uma armadilha dos soldados do governo. Você é capturado e nunca mais ouvido. FINAL RUIM: A busca pela verdade te custou a vida.",
        "imagem": "final_ruim_armadilha.jpg",
        "opcoes": []
    },

    # Finais do Ramo B
    "final_bom_mudancas_historicas": {
        "texto": "A explosão impede o surgimento do vírus, mas altera outras linhas do tempo. O mundo volta ao normal, mas com estranhas mudanças históricas. FINAL BOM: O vírus nunca existiu, mas... algo está diferente.",
        "imagem": "final_bom_mudanca_tempo.jpg",
        "opcoes": []
    },

    "final_excelente_governo": {
        "texto": "Você descobre que o vírus não foi um acidente, mas sim uma arma. Ao retornar, traz dados suficientes para expor e derrubar o governo autoritário. FINAL EXCELENTE: Você não só salva a humanidade, como também liberta as pessoas da opressão.",
        "imagem": "final_excelente_midia.jpg",
        "opcoes": []
    },

    "final_ruim_luta": {
        "texto": "A luta é intensa, mas vocês são capturados. Os dados são destruídos. FINAL RUIM: O governo vence, e a esperança morre com vocês.",
        "imagem": "final_ruim_derrota.jpg",
        "opcoes": []
    },

    "final_bom_resistencia": {
        "texto": "Você foge levando os dados e consegue transmiti-los para outros grupos de resistência. Graças a você, a cura é desenvolvida por cientistas escondidos. FINAL BOM: A humanidade sobrevive e o governo perde força.",
        "imagem": "final_bom_fuga_dados.jpg",
        "opcoes": []
    }
}