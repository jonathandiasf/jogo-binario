"""
Módulo de Interface Gráfica e Ranking do Jogo Binário

Este módulo implementa a interface gráfica (GUI) do jogo binário utilizando Tkinter.
Gerencia o jogo interativo, a persistência de dados do ranking e a exibição dos resultados.

Classes:
    - JogoBinario: Classe principal que implementa a lógica do jogo com GUI

Funções:
    - carregar_ranking(): Carrega o ranking salvo em JSON
    - salvar_ranking(nome, pontos): Salva novo jogador no ranking

Autor: Seu Nome
Data: 2026
"""

import tkinter as tk
import random
import json
from typing import List, Dict

RANKING_FILE = "ranking.json"


def carregar_ranking() -> List[Dict[str, any]]:
    """
    Carrega o ranking de jogadores do arquivo JSON.

    Returns:
        List[Dict]: Lista de dicionários com nome e pontos dos jogadores.
                    Retorna lista vazia se o arquivo não existir.

    Exemplo:
        >>> ranking = carregar_ranking()
        >>> print(ranking)
        [{'nome': 'João', 'pontos': 25}, {'nome': 'Maria', 'pontos': 20}]
    """
    try:
        with open(RANKING_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def salvar_ranking(nome: str, pontos: int) -> None:
    """
    Salva um novo jogador no ranking e ordena os 10 melhores.

    Args:
        nome (str): Nome do jogador
        pontos (int): Pontuação alcançada pelo jogador

    Note:
        - Mantém apenas os 10 jogadores com melhor pontuação
        - Ordena por pontos em ordem decrescente
        - Salva os dados em formato JSON
    """
    ranking = carregar_ranking()
    ranking.append({"nome": nome, "pontos": pontos})
    ranking = sorted(ranking, key=lambda x: x["pontos"], reverse=True)[:10]
    with open(RANKING_FILE, "w") as f:
        json.dump(ranking, f)

class JogoBinario:
    """
    Classe principal que implementa o jogo binário com interface gráfica.

    Gerencia a interface Tkinter, a lógica do jogo, pontuação e exibição
    do ranking de jogadores.

    Attributes:
        root (tk.Tk): Janela principal da aplicação
        pontos (int): Pontos acumulados pelo jogador na partida atual
        rodadas (int): Número total de rodadas do jogo (fixo em 5)
        dificuldade (str): Nível de dificuldade escolhido ('facil', 'medio', 'avancado')
        modo_inverso (bool): Se True, converte binário → decimal; se False, decimal → binário
        rodada_atual (int): Número da rodada em execução
        numero (int): Número atual sendo perguntado
        resposta_correta (str): Resposta correta para a pergunta atual

    Methods:
        __init__: Inicializa a interface e o menu de seleção
        iniciar: Inicia uma partida do jogo
        proxima_rodada: Exibe a próxima pergunta e agenda verificação
        verificar_resposta: Valida a resposta e exibe resultado
        fim_jogo: Encerra o jogo e salva o ranking
        mostrar_ranking: Exibe a janela com o Top 10 de jogadores
    """

    def __init__(self, root: tk.Tk) -> None:
        """
        Inicializa a interface gráfica e o menu de seleção de dificuldade.

        Args:
            root (tk.Tk): Janela principal da aplicação Tkinter
        """
        self.root = root
        self.root.title("Jogo Binário 🎮")
        self.pontos = 0
        self.rodadas = 5
        self.dificuldade = "facil"
        self.modo_inverso = False

        # Menu inicial
        self.label = tk.Label(root, text="Escolha a dificuldade:", font=("Arial", 16))
        self.label.pack(pady=10)

        self.dif_var = tk.StringVar(value="facil")
        tk.Radiobutton(root, text="Fácil", variable=self.dif_var, value="facil").pack()
        tk.Radiobutton(root, text="Médio", variable=self.dif_var, value="medio").pack()
        tk.Radiobutton(root, text="Avançado", variable=self.dif_var, value="avancado").pack()

        self.modo_var = tk.BooleanVar(value=False)
        tk.Checkbutton(root, text="Modo inverso (binário → decimal)", variable=self.modo_var).pack()

        self.botao = tk.Button(root, text="Iniciar Jogo", command=self.iniciar)
        self.botao.pack(pady=10)

    def iniciar(self) -> None:
        """
        Inicia uma nova partida do jogo.

        Lê as opções selecionadas pelo jogador, reseta a pontuação
        e exibe a primeira rodada.
        """
        self.dificuldade = self.dif_var.get()
        self.modo_inverso = self.modo_var.get()
        self.pontos = 0
        self.rodada_atual = 0
        self.entry = tk.Entry(self.root, font=("Arial", 14))
        self.entry.pack(pady=10)
        self.label.config(text="Vamos começar!")
        self.proxima_rodada()

    def proxima_rodada(self) -> None:
        """
        Exibe a próxima pergunta do jogo.

        Determina o número aleatório baseado na dificuldade, formata a pergunta
        (decimal → binário ou binário → decimal) e agenda a verificação da resposta.

        Dificuldades e seus limites:
            - Fácil: 1 a 15
            - Médio: 1 a 255
            - Avançado: 1 a 1023
        """
        if self.rodada_atual >= self.rodadas:
            self.fim_jogo()
            return
        self.rodada_atual += 1
        limite = 15 if self.dificuldade == "facil" else 255 if self.dificuldade == "medio" else 1023
        numero = random.randint(1, limite)
        self.numero = numero
        if self.modo_inverso:
            self.label.config(text=f"Qual é o decimal de {bin(numero)[2:]}?")
            self.resposta_correta = str(numero)
        else:
            self.label.config(text=f"Qual é o binário de {numero}?")
            self.resposta_correta = bin(numero)[2:]
        self.entry.delete(0, tk.END)
        self.root.after(15000, self.verificar_resposta)

    def verificar_resposta(self) -> None:
        """
        Valida a resposta do jogador e exibe o feedback.

        Compara a resposta com a correta, incrementa pontos se acertado,
        exibe mensagem de feedback e agenda a próxima rodada.

        Feedback:
            - ✅ Correto! (incrementa 1 ponto)
            - ❌ Errado! Resposta certa: [valor] (sem incremento)
        """
        resposta = self.entry.get()
        if resposta == self.resposta_correta:
            self.pontos += 1
            self.label.config(text="✅ Correto!")
        else:
            self.label.config(text=f"❌ Errado! Resposta certa: {self.resposta_correta}")
        self.root.after(2000, self.proxima_rodada)

    def fim_jogo(self) -> None:
        """
        Encerra a partida e salva o score no ranking.

        Solicita o nome do jogador (se não digitado, usa "Jogador" como padrão),
        salva a pontuação no ranking e exibe a janela com o Top 10.
        """
        nome = self.entry.get() or "Jogador"
        salvar_ranking(nome, self.pontos)
        self.label.config(text=f"Fim do jogo! Pontos: {self.pontos}")
        self.mostrar_ranking()

    def mostrar_ranking(self) -> None:
        """
        Exibe uma janela com o Top 10 de jogadores.

        Cria uma nova janela (Toplevel) mostrando os jogadores com
        maior pontuação em ordem decrescente.
        """
        ranking = carregar_ranking()
        janela = tk.Toplevel(self.root)
        janela.title("Ranking 🏆")
        tk.Label(janela, text="Top 10 Jogadores", font=("Arial", 16)).pack(pady=10)
        for i, jogador in enumerate(ranking, start=1):
            tk.Label(janela, text=f"{i}. {jogador['nome']} - {jogador['pontos']} pontos").pack()


if __name__ == "__main__":
    # Inicializa e executa o jogo
    root = tk.Tk()
    jogo = JogoBinario(root)
    root.mainloop()
