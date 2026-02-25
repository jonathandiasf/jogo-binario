*Este jogo converte números decimais em binário, e vice-versa.*
*A finalidade é mostrar se o usuário respondeu "Correto" ou "Errado". No final os pontos são acumulados em um ranking.*

## 🧩 Estrutura geral
- O jogo tem duas versões:
  - Terminal (CLI): usa input() e print() para interação simples.
  - Interface gráfica (GUI): feita com Tkinter, mais amigável e visual.

## 🎮 Lógica do jogo
- **Geração de número aleatório:** `random.randint(1, limite)`
  - O limite depende da dificuldade escolhida (15, 255 ou 1023).
- **Conversão decimal ↔ binário:**
  - Decimal → Binário: `bin(numero)[2:]` (remove o prefixo 0b).
  - Binário → Decimal: basta comparar com o número original.
- **Rodadas:**
  - O jogo tem 5 rodadas fixas.
  - Em cada rodada, o jogador responde e ganha pontos se acertar.

## 🖥️ Interface gráfica (Tkinter)
- **Menu inicial:**
  - Escolha da dificuldade (facil, medio, avancado).
  - Opção de modo inverso (binário → decimal).
  - Botão para iniciar o jogo.
- **Entrada de resposta:**
  - Campo Entry para digitar a resposta.
  - O jogo verifica automaticamente após 15 segundos (root.after).
- **Feedback:**
  - Mensagens ✅ Correto ou ❌ Errado.
  - Mostra a resposta certa quando o jogador erra.

## 🏆 Ranking
- **Persistência em JSON:**
  - Arquivo ranking.json guarda os 10 melhores jogadores.
- **Funções:**
  - `carregar_ranking()` → lê o ranking.
  - `salvar_ranking()` → adiciona novo jogador e ordena por pontos.
- **Exibição:**
  - Janela extra (Toplevel) mostra o Top 10 com nome e pontuação.

## 📚 Conversão de binário → decimal
- Identificar as posições: cada dígito binário corresponde a uma potência de 2, começando da direita (2⁰, 2¹, 2²...).
- Multiplicar e somar: multiplica cada dígito pelo valor da potência de 2 correspondente e soma os resultados.
- Exemplo: 1011₂ = (1·2³)+(0·2²)+(1·2¹)+(1·2⁰) = 8+0+2+1 = 11₁₀

## 📚 Conversão de decimal → binário
- Divisão sucessiva por 2: divide o número decimal por 2, anotando o resto (0 ou 1).
- Repetir até o quociente ser 0.
- Ler os restos de baixo para cima.
- Exemplo: 13₁₀
  - 13 ÷ 2 = 6 resto 1
  - 6 ÷ 2 = 3 resto 0
  - 3 ÷ 2 = 1 resto 1
  - 1 ÷ 2 = 0 resto 1
  - → Lendo de baixo para cima: 1101
  - Resultado: 13₁₀ = 1101₂

## ⚡ Pontos importantes para lembrar
- Cada posição no binário vale uma potência de 2.
- O último dígito à direita (bit menos significativo) vale 2⁰=1.
- O primeiro dígito à esquerda (bit mais significativo) indica o maior valor de potência de 2 presente.
- O processo é reversível: qualquer número decimal pode ser escrito em binário e vice-versa.
- Binário é a linguagem dos computadores, pois é simples de representar fisicamente (0 = ausência de sinal, 1 = presença de sinal).

## 🚀 Como rodar o jogo na sua máquina

### Pré-requisitos
- Python 3.7 ou superior
- Git (opcional, para clonar o repositório)

### Instalação

#### 1. Clone o repositório
```bash
git clone https://github.com/jonathandiasf/jogo-binario.git
cd jogo-binario
```

#### 2. Crie um ambiente virtual
```bash
python -m venv venv
```

#### 3. Ative o ambiente virtual

**No Windows (PowerShell):**
```bash
.\venv\Scripts\Activate.ps1
```

**No Windows (CMD):**
```bash
venv\Scripts\activate.bat
```

**No macOS/Linux:**
```bash
source venv/bin/activate
```

#### 4. Instale as dependências (se houver)
```bash
pip install -r requirements.txt
```

#### 5. Execute o jogo
```bash
python RANKING.py
```

### Alternativa: Executar no VS Code
- Instale o Python (3.10+)
- Abra o projeto no VS Code (File → Open Folder)
- Instale a extensão Python da Microsoft
- Clique em Run → Start Debugging (F5) ou use o botão ▶️
- A janela do jogo em Tkinter vai abrir automaticamente

## 📁 Estrutura do Projeto
- `JOGO-BINARIO.py` - Lógica principal do jogo
- `RANKING.py` - Interface gráfica com tkinter
- `ranking.json` - Arquivo de persistência do ranking
- `.gitignore` - Arquivo para ignorar diretórios/arquivos desnecessários
- `requirements.txt` - Dependências do projeto
- `README.md` - Este arquivo

## 📝 Ranking
- O ranking é salvo em `ranking.json`
- Se quiser resetar, basta deletar o arquivo

## 👨‍💻 Autores e Licença
Projeto educacional de Conversão Binária
