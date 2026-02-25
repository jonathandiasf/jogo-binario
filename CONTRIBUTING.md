# Guia de Contribuição - Jogo Binário

Obrigado por estar interessado em contribuir para o projeto Jogo Binário! Este documento fornece diretrizes e instruções para que você possa contribuir de forma eficaz.

## 📋 Código de Conduta

Por favor, seja respeitoso com outros contribuidores e usuários. Comportamento abusivo, discriminatório ou inadequado não será tolerado.

## 🚀 Como Contribuir

### 1. Faça um Fork do Repositório

```bash
# Clone o repositório para sua máquina
git clone https://github.com/jonathandiasf/jogo-binario.git
cd jogo-binario

# Crie uma branch para sua contribuição
git checkout -b feature/sua-feature-aqui
```

### 2. Configure o Ambiente

```bash
# Crie um ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# macOS/Linux:
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt
```

### 3. Faça suas Mudanças

- Siga o estilo de código existente
- Adicione docstrings em todas as funções e classes
- Use type hints quando apropriado
- Tente manter a compatibilidade com Python 3.7+

### 4. Teste suas Mudanças

```bash
# Execute o jogo para testar manualmente
python RANKING.py

# Ou execute a versão CLI
python JOGO-BINARIO.py
```

### 5. Commit e Push

```bash
# Adicione suas mudanças
git add .

# Crie um commit com uma mensagem clara
git commit -m "feat: descrição clara da sua mudança"

# Push para seu fork
git push origin feature/sua-feature-aqui
```

### 6. Abra um Pull Request

- Vá para o repositório original no GitHub
- Clique em "New Pull Request"
- Descreva claramente what você fez, por quê e como testar

## 📝 Padrões de Commit

Use as seguintes prefixos para seus commits:

- `feat:` - Adiciona uma nova funcionalidade
- `fix:` - Corrige um bug
- `docs:` - Mudanças apenas em documentação
- `style:` - Mudanças de formatação (não afetam código)
- `refactor:` - Refatoração de código sem mudar funcionalidade
- `test:` - Adiciona ou modifica testes
- `chore:` - Outras mudanças (dependências, build, etc)

### Exemplos:

```bash
git commit -m "feat: adiciona modo difícil ao jogo"
git commit -m "fix: corrige bug na conversão binária"
git commit -m "docs: atualiza README com exemplos"
```

## 🎯 Áreas para Contribuição

### Funcionalidades Solicitadas:

- [ ] Adicionar testes unitários
- [ ] Melhorar a interface gráfica
- [ ] Adicionar mais níveis de dificuldade
- [ ] Implementar sistema de pontos dinâmico
- [ ] Adicionar som e efeitos visuais
- [ ] Criar versão web (Flask/Django)
- [ ] Tradução para outros idiomas
- [ ] Dark mode na interface

### Bugs Conhecidos:

- [ ] Melhorar validação de entrada
- [ ] Adicionar tratamento de exceções mais robusto

## 📚 Documentação

Se você estiver adicionando uma nova funcionalidade:

1. Atualize o README.md se necessário
2. Adicione docstrings em estilo Google ou NumPy
3. Atualize o CHANGELOG.md

### Exemplo de Docstring:

```python
def minha_funcao(parametro1: str, parametro2: int) -> bool:
    """
    Descrição breve da função.

    Descrição mais detalhada se necessário.

    Args:
        parametro1 (str): Descrição do parametro 1
        parametro2 (int): Descrição do parametro 2

    Returns:
        bool: Descrição do retorno

    Raises:
        ValueError: Descrição de quando esta exceção é levantada

    Example:
        >>> resultado = minha_funcao("teste", 42)
        >>> print(resultado)
        True
    """
    pass
```

## 🐛 Reportando Bugs

Se encontrar um bug, por favor:

1. Verifique se o bug já foi reportado (GitHub Issues)
2. Crie um novo issue com:
   - **Título claro** do problema
   - **Descrição detalhada** do que acontece
   - **Passos para reproduzir** o problema
   - **Comportamento esperado** vs **comportamento atual**
   - **Screenshots** se aplicável
   - **Ambiente:** Python version, SO, etc

### Exemplo:

```
Título: Bug na conversão de números grandes

Descrição:
Ao tentar converter números maiores que 1000 para binário na dificuldade avançada, 
o jogo trava.

Passos para reproduzir:
1. Inicie o jogo
2. Selecione dificuldade "avançado"
3. Quando perguntado um número > 1000, o programa trava

Esperado: Deveria exibir a pergunta normalmente
Obtido: Congelamento da interface

Ambiente:
- Python 3.9
- Windows 10
```

## 💡 Sugestões de Melhorias

Se tiver sugestões de funcionalidades ou melhorias:

1. Abra uma discussion ou issue com `[SUGESTÃO]` no título
2. Descreva claramente o que você gostaria
3. Explique o benefício da mudança
4. Forneça exemplos se possível

## 🎓 Processo de Review

- Cada PR será reviado por um ou mais mantenedores
- Feedback será fornecido em no máximo 7 dias
- Pequenas mudanças podem ser aprovadas rapidamente
- Grandes mudanças podem precisar de ajustes
- Todos os testes devem passar antes da aprovação

## 📞 Dúvidas?

Se tiver dúvidas:

- Abra uma discussion no GitHub
- Envie uma mensagem para o mantenedor principal
- Revise a documentação existente

## Obrigado! 🙏

Sua contribuição é valiosa e ajuda a melhorar este projeto para todos!

---

**Happy coding!** 🚀
