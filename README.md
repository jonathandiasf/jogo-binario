*Este jogo converte números decimais em binário, e vice-versa.*
*A finalidade é mostrar se o usuário respondeu "Correto" ou "Errado". No final os pontos são acumulados em um ranking.*

🧩 Estrutura geral
- O jogo tem duas versões:
- Terminal (CLI): usa input() e print() para interação simples.
- Interface gráfica (GUI): feita com Tkinter, mais amigável e visual.

🎮 Lógica do jogo
- Geração de número aleatório:
random.randint(1, limite)
- O limite depende da dificuldade escolhida (15, 255 ou 1023).
- Conversão decimal ↔ binário:
- Decimal → Binário: bin(numero)[2:] (remove o prefixo 0b).
- Binário → Decimal: basta comparar com o número original.
- Rodadas:
- O jogo tem 5 rodadas fixas.
- Em cada rodada, o jogador responde e ganha pontos se acertar

🖥️ Interface gráfica (Tkinter)- Menu inicial:
- Escolha da dificuldade (facil, medio, avancado).
- Opção de modo inverso (binário → decimal).
- Botão para iniciar o jogo.
- Entrada de resposta:
- Campo Entry para digitar a resposta.
- O jogo verifica automaticamente após 15 segundos (root.after).
- Feedback:
- Mensagens ✅ Correto ou ❌ Errado.
- Mostra a resposta certa quando o jogador erra.

🏆 Ranking- Persistência em JSON:
- Arquivo ranking.json guarda os 10 melhores jogadores.
- Funções:
- carregar_ranking() → lê o ranking.
- salvar_ranking() → adiciona novo jogador e ordena por pontos.
- Exibição:
- Janela extra (Toplevel) mostra o Top 10 com nome e pontuação.

# Conversão de binário → decimal #
- Identificar as posições: cada dígito binário corresponde a uma potência de 2, começando da direita (2⁰, 2¹, 2²...).
- Multiplicar e somar: multiplica cada dígito pelo valor da potência de 2 correspondente e soma os resultados.
  
# Conversão de decimal → binário #
- Divisão sucessiva por 2: divide o número decimal por 2, anotando o resto (0 ou 1).
- Repetir até o quociente ser 0.
- Ler os restos de baixo para cima.
- Exemplo: 13_{10}
- 13 ÷ 2 = 6 resto 1
- 6 ÷ 2 = 3 resto 0
- 3 ÷ 2 = 1 resto 1
- 1 ÷ 2 = 0 resto 1
→ Lendo de baixo para cima: 1101
Resultado: 13_{10}=1101_2.

 # Pontos importantes para lembrar #
- Cada posição no binário vale uma potência de 2.
- O último dígito à direita (bit menos significativo) vale 2^0=1.
- O primeiro dígito à esquerda (bit mais significativo) indica o maior valor de potência de 2 presente.
- O processo é reversível: qualquer número decimal pode ser escrito em binário e vice-versa.
- Binário é a linguagem dos computadores, pois é simples de representar fisicamente (0 = ausência de sinal, 1 = presença de sinal).

# Como rodar o jogo no VSCode #

1 Instale o Python
- Certifique-se de ter o Python 3.10+ instalado.
- Verifique com:
python --version
2 Abra o projeto no VS Code
- Clique em File → Open Folder e selecione a pasta do jogo.
- O arquivo principal deve ser jogo_binario.py.
3 Instale a extensão do Python
- No VS Code, vá em Extensions (Ctrl+Shift+X).
- Procure por Python e instale a oficial da Microsoft.
- Isso habilita recursos como execução, depuração e linting.
4 Execute o jogo
- Abra o arquivo jogo_binario.py.
- Clique em Run → Start Debugging (F5) ou use o botão ▶️ no canto superior direito.
- A janela do jogo em Tkinter vai abrir automaticamente.
5 Ranking
- O ranking é salvo em ranking.json.
- Se quiser resetar, basta apagar o arquivo.
