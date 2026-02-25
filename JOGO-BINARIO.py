"""
Módulo de Lógica do Jogo Binário

Este módulo contém as funções principais para executar o jogo de conversão
binária em modo CLI (Command Line Interface). Permite ao jogador converter
números decimais para binário através de um quiz com 5 rodadas.

Funções:
    - gerar_numero(): Gera um número aleatório entre 1 e 50
    - converter_para_binario(numero): Converte decimal para binário
    - perguntar_jogador(numero): Solicita resposta do jogador
    - verificar_resposta(numero, resposta): Valida a resposta
    - jogar(): Executa o loop principal do jogo

Autor: Seu Nome
Data: 2026
"""

import random


def gerar_numero() -> int:
    """
    Gera um número decimal aleatório.

    Returns:
        int: Número aleatório entre 1 e 50
    """
    return random.randint(1, 50)


def converter_para_binario(numero: int) -> str:
    """
    Converte um número decimal para sua representação em binário.

    Args:
        numero (int): Número decimal a ser convertido

    Returns:
        str: Representação binária do número (sem o prefixo '0b')

    Exemplo:
        >>> converter_para_binario(10)
        '1010'
    """
    return bin(numero)[2:]  # Remove o prefixo '0b'


def perguntar_jogador(numero: int) -> str:
    """
    Solicita ao jogador a resposta (representação binária de um número).

    Args:
        numero (int): Número decimal para o qual a resposta é solicitada

    Returns:
        str: Resposta digitada pelo jogador
    """
    resposta = input(f"Qual é o binário de {numero}? ")
    return resposta


def verificar_resposta(numero: int, resposta: str) -> bool:
    """
    Verifica se a resposta do jogador está correta.

    Args:
        numero (int): Número decimal original
        resposta (str): Resposta do jogador

    Returns:
        bool: True se correto, False caso contrário
    """
    binario_correto = converter_para_binario(numero)
    if resposta == binario_correto:
        print("✅ Correto!")
        return True
    else:
        print(f"❌ Errado. A resposta correta é {binario_correto}.")
        return False


def jogar() -> None:
    """
    Executa o jogo principal com 5 rodadas.

    O jogador deve converter 5 números decimais para binário.
    Ao final, exibe o total de pontos conquistados.
    """
    pontos = 0
    rodadas = 5
    for i in range(5):
        numero = gerar_numero()
        resposta = perguntar_jogador(numero)
        if verificar_resposta(numero, resposta):
            pontos += 1
    print(f"\nVocê fez {pontos}/{rodadas}")


if __name__ == "__main__":
    # Inínio do jogo
    jogar()


