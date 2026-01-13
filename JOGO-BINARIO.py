import random 

def gerar_numero():
    return random.randint(1, 50)

def converter_para_binario(numero):
    return bin(numero)[2:] # Remove o prefixo '0b'

def perguntar_jogador(numero):
    resposta = input(f"Qual é o binário de {numero}? ")
    return resposta

def verificar_resposta(numero, resposta):
    binario_correto = converter_para_binario(numero)
    if resposta == binario_correto:
           print("✅ Correto!")
           return True
    else:
          print(f"❌ Errado. A resposta correta é {binario_correto}.")
          return False

def jogar():
    pontos = 0
    rodadas = 5
    for i in range(5):
        numero = gerar_numero()
        resposta = perguntar_jogador(numero)
        if verificar_resposta(numero, resposta):
            pontos += 1
    print(f"\nVocê fez {pontos}/{rodadas}")

# Ínicio do jogo

jogar()


