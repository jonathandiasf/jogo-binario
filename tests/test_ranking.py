"""
Testes para o módulo RANKING.py

Testa as funções de persistência de ranking:
- carregar_ranking()
- salvar_ranking()
"""

import pytest
import json
import os
import sys
import tempfile
from pathlib import Path
from unittest.mock import patch, MagicMock

# Adiciona o diretório pai ao path para importar RANKING
sys.path.insert(0, r'c:\Users\ThinkPad\OneDrive\jogo_binario.py')

import importlib.util

# Importa dinamicamente o módulo RANKING
spec = importlib.util.spec_from_file_location(
    "RANKING",
    r'c:\Users\ThinkPad\OneDrive\jogo_binario.py\RANKING.py'
)
ranking_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ranking_module)


class TestCarregarRanking:
    """Testes para a função carregar_ranking()"""

    def test_carregar_ranking_arquivo_nao_existe(self):
        """Verifica se retorna lista vazia quando arquivo não existe"""
        with patch.object(ranking_module, 'RANKING_FILE', '/caminho/inexistente/ranking.json'):
            resultado = ranking_module.carregar_ranking()
            assert resultado == []

    def test_carregar_ranking_arquivo_vazio(self):
        """Verifica comportamento com arquivo vazio"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            f.write('[]')
            temp_file = f.name

        try:
            with patch.object(ranking_module, 'RANKING_FILE', temp_file):
                resultado = ranking_module.carregar_ranking()
                assert resultado == []
        finally:
            os.unlink(temp_file)

    def test_carregar_ranking_com_dados(self):
        """Verifica carregamento com dados válidos"""
        dados = [
            {"nome": "João", "pontos": 25},
            {"nome": "Maria", "pontos": 20}
        ]
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump(dados, f)
            temp_file = f.name

        try:
            with patch.object(ranking_module, 'RANKING_FILE', temp_file):
                resultado = ranking_module.carregar_ranking()
                assert resultado == dados
        finally:
            os.unlink(temp_file)

    def test_carregar_ranking_retorna_lista(self):
        """Verifica se sempre retorna uma lista"""
        with patch.object(ranking_module, 'RANKING_FILE', '/caminho/inexistente/ranking.json'):
            resultado = ranking_module.carregar_ranking()
            assert isinstance(resultado, list)

    def test_carregar_ranking_json_invalido(self):
        """Verifica comportamento com JSON inválido"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            f.write('{ invalid json }')
            temp_file = f.name

        try:
            with patch.object(ranking_module, 'RANKING_FILE', temp_file):
                resultado = ranking_module.carregar_ranking()
                assert resultado == []
        finally:
            os.unlink(temp_file)


class TestSalvarRanking:
    """Testes para a função salvar_ranking()"""

    def test_salvar_ranking_novo_jogador(self):
        """Verifica se novo jogador é adicionado"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump([], f)
            temp_file = f.name

        try:
            with patch.object(ranking_module, 'RANKING_FILE', temp_file):
                ranking_module.salvar_ranking("João", 25)
                resultado = ranking_module.carregar_ranking()
                assert len(resultado) == 1
                assert resultado[0]["nome"] == "João"
                assert resultado[0]["pontos"] == 25
        finally:
            os.unlink(temp_file)

    def test_salvar_ranking_multiplos_jogadores(self):
        """Verifica adição de múltiplos jogadores"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump([], f)
            temp_file = f.name

        try:
            with patch.object(ranking_module, 'RANKING_FILE', temp_file):
                ranking_module.salvar_ranking("João", 25)
                ranking_module.salvar_ranking("Maria", 30)
                ranking_module.salvar_ranking("Pedro", 20)
                resultado = ranking_module.carregar_ranking()
                assert len(resultado) == 3
        finally:
            os.unlink(temp_file)

    def test_salvar_ranking_ordena_por_pontos(self):
        """Verifica se ordena por pontos decrescentes"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump([], f)
            temp_file = f.name

        try:
            with patch.object(ranking_module, 'RANKING_FILE', temp_file):
                ranking_module.salvar_ranking("João", 10)
                ranking_module.salvar_ranking("Maria", 30)
                ranking_module.salvar_ranking("Pedro", 20)
                resultado = ranking_module.carregar_ranking()
                
                # Verifica se está ordenado (pontos decrescentes)
                assert resultado[0]["pontos"] == 30  # Maria
                assert resultado[1]["pontos"] == 20  # Pedro
                assert resultado[2]["pontos"] == 10  # João
        finally:
            os.unlink(temp_file)

    def test_salvar_ranking_mantém_top_10(self):
        """Verifica se mantém apenas os 10 melhores"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump([], f)
            temp_file = f.name

        try:
            with patch.object(ranking_module, 'RANKING_FILE', temp_file):
                # Adiciona 15 jogadores
                for i in range(15):
                    ranking_module.salvar_ranking(f"Jogador{i}", i * 10)
                
                resultado = ranking_module.carregar_ranking()
                assert len(resultado) == 10  # Mantém apenas 10
                
                # Os 10 melhores: 140, 130, 120, 110, 100, 90, 80, 70, 60, 50
                assert resultado[0]["pontos"] == 140
                assert resultado[-1]["pontos"] == 50
        finally:
            os.unlink(temp_file)

    def test_salvar_ranking_com_mesmo_nome_diferentes_scores(self):
        """Verifica se permite mesmo nome com scores diferentes"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump([], f)
            temp_file = f.name

        try:
            with patch.object(ranking_module, 'RANKING_FILE', temp_file):
                ranking_module.salvar_ranking("João", 10)
                ranking_module.salvar_ranking("João", 20)
                ranking_module.salvar_ranking("João", 15)
                resultado = ranking_module.carregar_ranking()
                
                assert len(resultado) == 3
                # Todos com nome "João" mas pontos diferentes
                assert all(jogador["nome"] == "João" for jogador in resultado)
                assert [j["pontos"] for j in resultado] == [20, 15, 10]
        finally:
            os.unlink(temp_file)

    def test_salvar_ranking_dados_sao_dicts(self):
        """Verifica se os dados salvos são dicionários com chaves corretas"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump([], f)
            temp_file = f.name

        try:
            with patch.object(ranking_module, 'RANKING_FILE', temp_file):
                ranking_module.salvar_ranking("João", 25)
                resultado = ranking_module.carregar_ranking()
                
                assert isinstance(resultado[0], dict)
                assert "nome" in resultado[0]
                assert "pontos" in resultado[0]
        finally:
            os.unlink(temp_file)

    @pytest.mark.parametrize("nome,pontos", [
        ("Alice", 100),
        ("Bob", 50),
        ("Charlie", 75),
        ("Diana", 90),
        ("Eve", 60),
    ])
    def test_salvar_ranking_multiplos_parametrizado(self, nome, pontos):
        """Testa salvamento parametrizado"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump([], f)
            temp_file = f.name

        try:
            with patch.object(ranking_module, 'RANKING_FILE', temp_file):
                ranking_module.salvar_ranking(nome, pontos)
                resultado = ranking_module.carregar_ranking()
                
                assert len(resultado) == 1
                assert resultado[0]["nome"] == nome
                assert resultado[0]["pontos"] == pontos
        finally:
            os.unlink(temp_file)


class TestIntegracaoRanking:
    """Testes de integração do ranking"""

    def test_ciclo_completo_ranking(self):
        """Testa ciclo completo: carrega, salva, carrega novamente"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump([], f)
            temp_file = f.name

        try:
            with patch.object(ranking_module, 'RANKING_FILE', temp_file):
                # Carrega vazio
                resultado1 = ranking_module.carregar_ranking()
                assert resultado1 == []
                
                # Salva novo jogador
                ranking_module.salvar_ranking("João", 25)
                
                # Carrega novamente
                resultado2 = ranking_module.carregar_ranking()
                assert len(resultado2) == 1
                assert resultado2[0]["nome"] == "João"
        finally:
            os.unlink(temp_file)

    def test_multiplas_operacoes_sequenciais(self):
        """Testa múltiplas operações em sequência"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump([], f)
            temp_file = f.name

        try:
            with patch.object(ranking_module, 'RANKING_FILE', temp_file):
                # Salva 3 jogadores
                jogadores = [
                    ("Alice", 100),
                    ("Bob", 50),
                    ("Charlie", 75),
                ]
                
                for nome, pontos in jogadores:
                    ranking_module.salvar_ranking(nome, pontos)
                
                # Carrega e verifica
                resultado = ranking_module.carregar_ranking()
                assert len(resultado) == 3
                
                # Verifica ordem (descendente)
                pontos_ordenados = [j["pontos"] for j in resultado]
                assert pontos_ordenados == sorted(pontos_ordenados, reverse=True)
        finally:
            os.unlink(temp_file)
