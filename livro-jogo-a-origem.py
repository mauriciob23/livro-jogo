#Trabalho de Lógica e Algoritimo - Livro Jogo
#Aluno(a)s:	Jennyfer Mayara Moraes de Souza
#			Mauricio Jose Barros de Oliveira

def escolha_valida(pergunta): #função usada para criar um laço de repetição caso o usuario entre com um valor invalido (diferente de a ou b)
    while True: 
        escolha = input(pergunta).lower() #exibe a pergunta e converte a entrada para minusculo
        if escolha in ['a', 'b'] : #verifica se a entrada do usuario é valida
            return escolha #retorna a escolha feita, encerrando a função
        else:
            print("Escolha inválida. Digite apenas 'a' ou 'b'.\n")
            
print("\t\t\tFragmentos de um Futuro Perdido")
print("Ano de 2061. A Terra está devastada após um vírus misterioso dizimar a humanidade.")                                     # ILUSTRAÇÃO - OK
print("Você é um cientista sobrevivente, com memórias fragmentadas e uma missão que pode salvar ou condenar o mundo.")          # ILUSTRAÇÃO - OK

print("\nVocê acorda em um laboratório destruído. Sua cabeça lateja e pedaços da memória começam a voltar.")                    # ILUSTRAÇÃO - OK
print("Primeira decisão: O que você faz?")
print("a) Vasculhar o laboratório em busca de pistas.") #Leva para a linha 22                                                   # ILUSTRAÇÃO - OK
print("b) Sair imediatamente e procurar seu antigo parceiro.") #Leva para a linha 79                                            # ILUSTRAÇÃO - OK

escolha1 = escolha_valida("Escolha (a/b): ").lower()  #chama a função escolha_valida e passando como argumento o texto "Escolha (a/b): ". Esse texto entra na função no lugar do parâmetro (pergunta).

if escolha1 == "a": 
    print("\nVocê encontra registros dos seus últimos experimentos, um estranho rádio comunicador e coordenadas de uma instalação militar.")   # ILUSTRAÇÃO - OK
    print("Segunda decisão: Você...")
    print("a) Segue as coordenadas para a instalação militar em busca de recursos.") #Leva para a linha 30                                     # ILUSTRAÇÃO - OK
    print("b) Tenta entrar em contato com outros sobreviventes pela rádio.")                                                                   # ILUSTRAÇÃO - OK

    escolha2 = escolha_valida("Escolha (a/b): ").lower()

    if escolha2 == "a":
        print("\nA instalação está fortemente vigiada por drones do governo.")                      # ILUSTRAÇÃO - OK
        print("Terceira decisão: Você...")
        print("a) Tenta se infiltrar furtivamente.") #Leva para Linha 38                            # ILUSTRAÇÃO - OK
        print("b) Recua e procura outro caminho.") #Leva para Linha 56 (FINAL ALTERNATIVO)          # -----> FALTA ILUSTRAÇÃO

        escolha3 = escolha_valida("Escolha (a/b): ").lower()

        if escolha3 == "a":
            print("\nVocê consegue entrar, mas ativa um alarme.")                                       # ILUSTRAÇÃO - OK
            print("Seu antigo parceiro aparece de repente, ele estava escondido ali.")                  # ILUSTRAÇÃO - OK
            print("Quarta decisão: Ele oferece uma chance de usar a máquina do tempo. Você aceita?")    # ILUSTRAÇÃO - OK
            print("a) Sim, tentar mudar o passado.") #Leva para Linha 47 (FINAL 1)                      # ILUSTRAÇÃO - OK
            print("b) Não, focar em criar a cura no presente.") #Leva para Linha 51 (FINAL 2)           # ILUSTRAÇÃO - OK

            escolha4 = escolha_valida("Escolha (a/b): ").lower()

            if escolha4 == "a": #FINAL 1                                                                # ILUSTRAÇÃO - OK
                print("\nVocês ativam a máquina... mas algo dá errado.")                                # ILUSTRAÇÃO - OK   
                print("Você é lançado para um futuro ainda pior, onde a humanidade já não existe.")     # ILUSTRAÇÃO - OK
                print("FINAL RUIM: A tentativa de mudar o passado falhou e piorou tudo.")               # ILUSTRAÇÃO - OK - [FINAL 1 OK]
            elif escolha4 == "b": #FINAL 2
                print("\nVocês combinam esforços e usam os dados recuperados para sintetizar uma vacina.")      #ILUSTRAÇÃO - OK
                print("Após semanas de trabalho, conseguem imunizar um pequeno grupo.")                         #ILUSTRAÇÃO - OK
                print("FINAL BOM: Um novo começo para a humanidade.")                                           #ILUSTRAÇÃO - OK
           
        elif escolha3 == "b": #FINAL ALTERNATIVO 
            print("\nAo tentar fugir, você é capturado pelos drones do governo.")           #ILUSTRAÇÃO - OK
            print("Eles te levam para um centro de interrogatório.")                        #ILUSTRAÇÃO - OK
            print("FINAL NEUTRO: Você sobrevive, mas perde sua liberdade.")                 #ILUSTRAÇÃO - OK - Misson Failed

    elif escolha2 == "b":
        print("\nVocê consegue sinal na rádio e recebe uma resposta.")                                  #ILUSTRAÇÃO - OK       
        print("Uma comunidade secreta de sobreviventes te convida.")                                    #ILUSTRAÇÃO - OK
        print("Terceira decisão: Você...")
        print("a) Aceita o convite e segue para a comunidade...") #Leva para a Linha 70 (FINAL 3)       #ILUSTRAÇÃO - OK
        print("b) Desconfia e decide investigar mais...") #Leva para a Linha 74 (FINAL 4)

        escolha3 = escolha_valida("Escolha (a/b): ").lower()

        if escolha3 == "a": #FINAL 3
            print("\nChegando lá, você descobre que eles estão trabalhando em uma cura coletiva.")          #ILUSTRAÇÃO - OK
            print("Com sua ajuda, aceleram o processo e salvam centenas de pessoas.")                       #ILUSTRAÇÃO - OK
            print("FINAL BOM: Uma chance real de reconstruir a civilização.")                               #ILUSTRAÇÃO - OK
        elif escolha3 == "b": #FINAL 4
            print("\nVocê descobre que era uma armadilha dos soldados do governo.")
            print("Você é capturado e nunca mais ouvido.")                                                  #ILUSTRAÇÃO - OK
            print("FINAL RUIM: A busca pela verdade te custou a vida.")                                     #ILUSTRAÇÃO - OK

elif escolha1 == "b":
    print("\nVocê parte em busca de seu antigo parceiro.")                                                  # ILUSTRAÇÃO - OK
    print("Após horas, o encontra isolado, cercado de equipamentos estranhos.")
    print("Ele te revela que aperfeiçoou uma máquina do tempo, mas ela não é estável.")                     # ILUSTRAÇÃO - OK
    print("Segunda decisão: Você...")
    print("a) Concorda em usar a máquina para impedir o surgimento do vírus.") #Leva para a Linha 89        # ILUSTRAÇÃO - OK
    print("b) Sugere trabalhar juntos em uma vacina no presente.") #Leva para a Linha 107

    escolha2 = escolha_valida("Escolha (a/b): ").lower()

    if escolha2 == "a":
        print("\nVocês ativam a máquina e viajam para 2020.")                                               # ILUSTRAÇÃO - OK
        print("Terceira decisão: Você encontra o laboratório onde tudo começou.")                           # ILUSTRAÇÃO - OK
        print("a) Destruir o laboratório imediatamente.") #Leva para a Linha 97                             # ILUSTRAÇÃO - OK
        print("b) Roubar os dados e buscar outra solução.") #Leva para a Linha 101                          

        escolha3 = escolha_valida("Escolha (a/b): ").lower()

        if escolha3 == "a": #FINAL 3
            print("\nA explosão impede o surgimento do vírus, mas altera outras linhas do tempo.")          # ILUSTRAÇÃO - OK
            print("O mundo volta ao normal, mas com estranhas mudanças históricas.")                        # ILUSTRAÇÃO - OK
            print("FINAL BOM: O vírus nunca existiu, mas... algo está diferente.")                          # ILUSTRAÇÃO - OK
        elif escolha3 == "b": #FINAL 4.1
            print("\nVocê descobre que o vírus não foi um acidente, mas sim uma arma.")                             
            print("Ao retornar, traz dados suficientes para expor e derrubar o governo autoritário.")               #ILUSTRAÇÃO - OK (?)
            print("FINAL EXCELENTE: Você não só salva a humanidade, como também liberta as pessoas da opressão.")   #ILUSTRAÇÃO - OK
        

    elif escolha2 == "b": 
        print("\nVocês começam a trabalhar na vacina.")
        print("De repente, são atacados por agentes do governo que querem silenciá-los.")
        print("Terceira decisão: Você...")
        print("a) Luta contra eles.") #LEVA PARA A LINHA 116 (FINAL 5)                                  #ILUSTRAÇÃO - OK
        print("b) Foge e tenta salvar os dados.") #Leva para a linha 120 (FINAL 6)                      #ILUSTRAÇÃO - OK

        escolha3 = input("Escolha (a/b): ").lower()

        if escolha3 == "a": #FINAL 5
            print("\nA luta é intensa, mas vocês são capturados.")                              #ILUSTRAÇÃO - OK
            print("Os dados são destruídos.")                                                   #ILUSTRAÇÃO - OK                
            print("FINAL RUIM: O governo vence, e a esperança morre com vocês.")                #ILUSTRAÇÃO - OK
        elif escolha3 == "b": #FINAL 6
            print("\nVocê foge levando os dados, consegue transmiti-los para outros grupos de resistência.")    #ILUSTRAÇÃO - OK
            print("Graças a você, a cura é desenvolvida por cientistas escondidos.")                            #ILUSTRAÇÃO - OK
            print("FINAL BOM: A humanidade sobrevive e o governo perde força.")                                 #ILUSTRAÇÃO - OK (?)


print("\n\t\t\tFim da Jornada") #FINISH!