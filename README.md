*Este jogo converte números decimais em binário, e vice-versa.*
*A finalidade é mostrar se o usuário respondeu "Correto" ou "Errado". No final os pontos são acumulados em um ranking.*

# Conversão de binário → decimal #
- Identificar as posições: cada dígito binário corresponde a uma potência de 2, começando da direita (2⁰, 2¹, 2²...).
- Multiplicar e somar: multiplica cada dígito pelo valor da potência de 2 correspondente e soma os resultados.
- Exemplo: 1011_2
(1\cdot 2^3)+(0\cdot 2^2)+(1\cdot 2^1)+(1\cdot 2^0)=8+0+2+1=11
- Resultado: 1011_2=11_{10}.

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

# Como rodar o jogo na sua máquina #


