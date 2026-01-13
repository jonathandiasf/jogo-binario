import tkinter as tk
import random
import json

RANKING_FILE = "ranking.json"

def carregar_ranking():
    try:
        with open(RANKING_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def salvar_ranking(nome, pontos):
    ranking = carregar_ranking()
    ranking.append({"nome": nome, "pontos": pontos})
    ranking = sorted(ranking, key=lambda x: x["pontos"], reverse=True)[:10]
    with open(RANKING_FILE, "w") as f:
        json.dump(ranking, f)

class JogoBinario:
    def __init__(self, root):
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

    def iniciar(self):
        self.dificuldade = self.dif_var.get()
        self.modo_inverso = self.modo_var.get()
        self.pontos = 0
        self.rodada_atual = 0
        self.entry = tk.Entry(self.root, font=("Arial", 14))
        self.entry.pack(pady=10)
        self.label.config(text="Vamos começar!")
        self.proxima_rodada()

    def proxima_rodada(self):
        if self.rodada_atual >= self.rodadas:
            self.fim_jogo()
            return
        self.rodada_atual += 1
        limite = 15 if self.dificuldade=="facil" else 255 if self.dificuldade=="medio" else 1023
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

    def verificar_resposta(self):
        resposta = self.entry.get()
        if resposta == self.resposta_correta:
            self.pontos += 1
            self.label.config(text="✅ Correto!")
        else:
            self.label.config(text=f"❌ Errado! Resposta certa: {self.resposta_correta}")
        self.root.after(2000, self.proxima_rodada)

    def fim_jogo(self):
        nome = self.entry.get() or "Jogador"
        salvar_ranking(nome, self.pontos)
        self.label.config(text=f"Fim do jogo! Pontos: {self.pontos}")
        self.mostrar_ranking()

    def mostrar_ranking(self):
        ranking = carregar_ranking()
        janela = tk.Toplevel(self.root)
        janela.title("Ranking 🏆")
        tk.Label(janela, text="Top 10 Jogadores", font=("Arial", 16)).pack(pady=10)
        for i, jogador in enumerate(ranking, start=1):
            tk.Label(janela, text=f"{i}. {jogador['nome']} - {jogador['pontos']} pontos").pack()

# Executar jogo
root = tk.Tk()
jogo = JogoBinario(root)
root.mainloop()
