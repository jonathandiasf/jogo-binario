# GitHub Actions Workflows

Este projeto está configurado com **4 workflows de CI/CD** automáticos.

## 📋 Lista de Workflows

### 1️⃣ **Tests** (`.github/workflows/tests.yml`)

**Quando executa:** A cada push ou pull request em `main` ou `develop`

**O que faz:**
- ✅ Executa os testes com pytest
- ✅ Testa em múltiplas versões Python (3.8, 3.9, 3.10, 3.11, 3.12)
- ✅ Testa em múltiplos SO (Ubuntu, Windows, macOS)
- ✅ Gera relatório de cobertura de código
- ✅ Envia cobertura para Codecov

**Status dos testes:**
- Python 3.8 até 3.12
- Todos os testes devem passar (56 testes)

---

### 2️⃣ **Linting** (`.github/workflows/linting.yml`)

**Quando executa:** A cada push ou pull request em `main` ou `develop`

**O que faz:**
- 📌 Valida sintaxe Python com flake8
- 📌 Verifica formatação com black
- 📌 Ordena imports com isort
- 📌 Analisa código com pylint

**Continue on Error:** Sim (não bloqueia o build)

---

### 3️⃣ **Code Quality Check** (`.github/workflows/quality.yml`)

**Quando executa:** A cada push ou pull request em `main` ou `develop`

**O que faz:**
- ✨ Verifica estrutura do projeto
- ✨ Valida sintaxe dos arquivos Python
- ✨ Verifica requirements.txt
- ✨ Valida arquivos JSON
- ✨ Verifica permissões de arquivos

---

### 4️⃣ **Release** (`.github/workflows/release.yml`)

**Quando executa:** Ao criar uma tag `v*` (exemplo: `v1.0.0`)

**O que faz:**
- 🚀 Executa testes completos
- 🚀 Cria release notes automaticamente
- 🚀 Publica release no GitHub
- 🚀 Gera instruções de instalação

---

## 🔄 Status dos Workflows

Para ver o status dos workflows, acesse:

```
https://github.com/jonathandiasf/jogo-binario/actions
```

---

## 📊 Badges (Para adicionar no README)

```markdown
![Tests](https://github.com/jonathandiasf/jogo-binario/workflows/Tests/badge.svg)
![Linting](https://github.com/jonathandiasf/jogo-binario/workflows/Linting/badge.svg)
![Code Quality Check](https://github.com/jonathandiasf/jogo-binario/workflows/Code%20Quality%20Check/badge.svg)
```

---

## 🚀 Como Criar uma Release

### Via Terminal (Git)

```bash
# 1. Criar uma tag localmente
git tag -a v1.0.0 -m "Release version 1.0.0"

# 2. Enviar a tag para GitHub
git push origin v1.0.0

# 3. O workflow será executado automaticamente
# 4. Verifique em: https://github.com/jonathandiasf/jogo-binario/releases
```

### Via GitHub Web

1. Vá para **Releases** no repositório
2. Clique em **Draft a new release**
3. Crie uma tag (exemplo: `v1.0.0`)
4. Adicione title e descrição
5. Clique em **Publish release**

---

## 📈 Cobertura de Código

A cobertura de código é enviada automaticamente para:

- 🔗 **Codecov**: https://codecov.io/gh/jonathandiasf/jogo-binario

Para adicionar badge de cobertura no README:

```markdown
[![codecov](https://codecov.io/gh/jonathandiasf/jogo-binario/branch/main/graph/badge.svg)](https://codecov.io/gh/jonathandiasf/jogo-binario)
```

---

## 🔧 Customizar Workflows

Para editar os workflows:

1. Acesse `.github/workflows/`
2. Edite o arquivo YAML desejado
3. Commit e push para `main`
4. Os workflows usarão automaticamente a nova versão

---

## ✅ Checklist para Manutenção

- [ ] Todos os testes passando (56/56)
- [ ] Não há erros de linting
- [ ] Cobertura de código acima de 80%
- [ ] Documentação atualizada
- [ ] CHANGELOG.md atualizado
- [ ] Release notes preparadas

---

## 📚 Referências

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Pytest Documentation](https://docs.pytest.org/)
- [Codecov Setup](https://docs.codecov.io/docs)
- [Semantic Versioning](https://semver.org/lang/pt-BR/)

---

**Status dos Workflows:** ✅ Configurados e Operacionais

Última atualização: 2026-02-24
