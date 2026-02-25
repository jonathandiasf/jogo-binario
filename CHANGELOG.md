# Changelog - Jogo Binário

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto segue [Semantic Versioning](https://semver.org/lang/pt-BR/).

## [Unreleased]

### Planned
- [ ] Adicionar suite de testes unitários
- [ ] Melhorias na interface gráfica (tema dark mode)
- [ ] Novos níveis de dificuldade
- [ ] Sistema de pontuação dinâmico
- [ ] Efeitos sonoros e visuais
- [ ] Versão web do jogo
- [ ] Suporte a múltiplos idiomas

---

## [1.0.0] - 2026-02-24

### Added
- ✨ Versão inicial do Jogo Binário
- 🎮 Interface gráfica com Tkinter
  - Menu de seleção de dificuldade (Fácil, Médio, Avançado)
  - Opção de modo inverso (binário → decimal)
  - Display visual do ranking em tempo real
- 🎯 Lógica do jogo com 5 rodadas
  - Conversão decimal ↔ binário
  - Sistema de pontuação
  - Timer automático de 15 segundos por resposta
- 🏆 Sistema de ranking persistente
  - Salva os 10 melhores jogadores
  - Armazenamento em JSON
  - Exibição de ranking em janela separada
- 📱 Versão CLI (Command Line Interface)
  - Execução pelo terminal
  - input/output simples
- 📚 Documentação completa
  - README.md com instruções de instalação e uso
  - Docstrings em todas as funções e classes
  - Type hints para melhor legibilidade
  - CONTRIBUTING.md para guia de contribuição
  - CHANGELOG.md (este arquivo)
  - LICENSE (MIT)
- 🔧 Configuração do projeto
  - .gitignore com padrões Python
  - requirements.txt para dependências
  - Estrutura modular do código

### Technical Details
- **Linguagem:** Python 3.7+
- **GUI Framework:** Tkinter (nativo)
- **Data Storage:** JSON
- **Versionamento:** Git

### File Structure
```
jogo-binario/
├── JOGO-BINARIO.py      # Versão CLI do jogo
├── RANKING.py           # Interface gráfica com Tkinter
├── ranking.json         # Arquivo de ranking (gerado em runtime)
├── README.md            # Documentação principal
├── CONTRIBUTING.md      # Guia de contribuição
├── CHANGELOG.md         # Este arquivo
├── LICENSE              # MIT License
├── requirements.txt     # Dependências do projeto
└── .gitignore           # Padrões ignorados pelo Git
```

### Known Issues
- Sem issues reportadas na versão inicial

### Performance
- Tempo de inicialização: < 1 segundo
- Uso de memória: ~15 MB
- Compatível com Python 3.7+

### Browser/Platform Support
- ✅ Windows 7+
- ✅ macOS 10.9+
- ✅ Linux (distribuições com Python 3.7+)
- ✅ Requer Tkinter (incluído na maioria das instalações Python)

---

## Formato de Entradas

### Added
- Para novas funcionalidades

### Changed
- Para mudanças em funcionalidades existentes

### Deprecated
- Para funcionalidades que serão removidas em breve

### Removed
- Para funcionalidades removidas

### Fixed
- Para correção de bugs

### Security
- Para vulnerabilidades corrigidas

---

## Contribuindo

Se você encontrou um bug ou tem uma sugestão de melhoria, por favor:

1. Abra uma issue no [GitHub](https://github.com/jonathandiasf/jogo-binario)
2. Siga as diretrizes de [CONTRIBUTING.md](CONTRIBUTING.md)
3. Use commits descritivos com prefixos apropriados

---

## Versionamento

Este projeto segue o [Semantic Versioning](https://semver.org/lang/pt-BR/):

- **MAJOR** (primeira versão): mudanças incompatíveis na API
- **MINOR** (segunda versão): mudanças adicionadas de forma compatível
- **PATCH** (terceira versão): correção de bugs

Exemplo: `v1.2.3`
- `1` = MAJOR
- `2` = MINOR
- `3` = PATCH

---

**Última atualização:** 2026-02-24
**Mantido por:** Jonathan Dias
