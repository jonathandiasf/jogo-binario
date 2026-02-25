"""
Testes para o módulo JOGO-BINARIO.py

Testa as funções principais:
- gerar_numero()
- converter_para_binario()
- perguntar_jogador() [não testável sem input]
- verificar_resposta()
- jogar() [não testável sem input]
"""

import pytest
import sys
from io import StringIO
from unittest.mock import patch

# Adiciona o diretório pai ao path para importar JOGO-BINARIO
sys.path.insert(0, r'c:\Users\ThinkPad\OneDrive\jogo_binario.py')

import importlib.util

# Importa dinamicamente o módulo JOGO-BINARIO.py
spec = importlib.util.spec_from_file_location(
    "JOGO_BINARIO",
    r'c:\Users\ThinkPad\OneDrive\jogo_binario.py\JOGO-BINARIO.py'
)
jogo_binario = importlib.util.module_from_spec(spec)
spec.loader.exec_module(jogo_binario)


class TestGerarNumero:
    """Testes para a função gerar_numero()"""

    def test_gerar_numero_retorna_inteiro(self):
        """Verifica se gerar_numero retorna um inteiro"""
        resultado = jogo_binario.gerar_numero()
        assert isinstance(resultado, int)

    def test_gerar_numero_intervalo(self):
        """Verifica se o número está no intervalo correto (1-50)"""
        for _ in range(100):  # Testa múltiplas vezes
            resultado = jogo_binario.gerar_numero()
            assert 1 <= resultado <= 50

    def test_gerar_numero_varia(self):
        """Verifica se números diferentes são gerados (não é constante)"""
        numeros = [jogo_binario.gerar_numero() for _ in range(20)]
        assert len(set(numeros)) > 1  # Pelo menos 2 números diferentes


class TestConverterParaBinario:
    """Testes para a função converter_para_binario()"""

    def test_converter_para_binario_zero(self):
        """Testa conversão do número 0"""
        resultado = jogo_binario.converter_para_binario(0)
        assert resultado == "0"

    def test_converter_para_binario_um(self):
        """Testa conversão do número 1"""
        resultado = jogo_binario.converter_para_binario(1)
        assert resultado == "1"

    def test_converter_para_binario_dois(self):
        """Testa conversão do número 2"""
        resultado = jogo_binario.converter_para_binario(2)
        assert resultado == "10"

    def test_converter_para_binario_dez(self):
        """Testa conversão do número 10"""
        resultado = jogo_binario.converter_para_binario(10)
        assert resultado == "1010"

    def test_converter_para_binario_quinze(self):
        """Testa conversão do número 15"""
        resultado = jogo_binario.converter_para_binario(15)
        assert resultado == "1111"

    def test_converter_para_binario_256(self):
        """Testa conversão do número 256"""
        resultado = jogo_binario.converter_para_binario(256)
        assert resultado == "100000000"

    def test_converter_para_binario_retorna_string(self):
        """Verifica se o retorno é uma string"""
        resultado = jogo_binario.converter_para_binario(10)
        assert isinstance(resultado, str)

    def test_converter_para_binario_sem_prefixo_0b(self):
        """Verifica se o retorno não tem o prefixo '0b'"""
        resultado = jogo_binario.converter_para_binario(10)
        assert not resultado.startswith("0b")

    @pytest.mark.parametrize("numero,esperado", [
        (1, "1"),
        (2, "10"),
        (3, "11"),
        (4, "100"),
        (5, "101"),
        (8, "1000"),
        (16, "10000"),
        (32, "100000"),
    ])
    def test_converter_para_binario_multiplos_valores(self, numero, esperado):
        """Testa múltiplas conversões parametrizadas"""
        resultado = jogo_binario.converter_para_binario(numero)
        assert resultado == esperado


class TestVerificarResposta:
    """Testes para a função verificar_resposta()"""

    def test_verificar_resposta_correta(self, capsys):
        """Verifica se reconhece resposta correta"""
        resultado = jogo_binario.verificar_resposta(10, "1010")
        assert resultado is True
        captured = capsys.readouterr()
        assert "✅ Correto!" in captured.out

    def test_verificar_resposta_incorreta(self, capsys):
        """Verifica se reconhece resposta incorreta"""
        resultado = jogo_binario.verificar_resposta(10, "1011")
        assert resultado is False
        captured = capsys.readouterr()
        assert "❌ Errado" in captured.out
        assert "1010" in captured.out

    def test_verificar_resposta_retorna_bool(self):
        """Verifica se o retorno é bool"""
        resultado = jogo_binario.verificar_resposta(5, "101")
        assert isinstance(resultado, bool)

    def test_verificar_resposta_zero(self):
        """Testa verificação para o número 0"""
        assert jogo_binario.verificar_resposta(0, "0") is True
        assert jogo_binario.verificar_resposta(0, "1") is False

    def test_verificar_resposta_sensivel_caracteres(self):
        """Verifica se é sensível a espaços/caracteres extras"""
        # A resposta correta é "1010" para 10
        assert jogo_binario.verificar_resposta(10, "1010") is True
        assert jogo_binario.verificar_resposta(10, " 1010") is False
        assert jogo_binario.verificar_resposta(10, "1010 ") is False

    @pytest.mark.parametrize("numero,resposta", [
        (1, "1"),
        (2, "10"),
        (3, "11"),
        (7, "111"),
        (15, "1111"),
        (256, "100000000"),
    ])
    def test_verificar_resposta_corretas_multiples(self, numero, resposta):
        """Testa múltiplas respostas corretas"""
        assert jogo_binario.verificar_resposta(numero, resposta) is True

    @pytest.mark.parametrize("numero,resposta", [
        (1, "0"),
        (2, "11"),
        (3, "10"),
        (7, "110"),
        (256, "10000000"),
    ])
    def test_verificar_resposta_incorretas_multiples(self, numero, resposta):
        """Testa múltiplas respostas incorretas"""
        assert jogo_binario.verificar_resposta(numero, resposta) is False


class TestIntegracao:
    """Testes de integração entre funções"""

    def test_gerar_numero_pode_ser_convertido(self):
        """Verifica se número gerado pode ser convertido"""
        numero = jogo_binario.gerar_numero()
        binario = jogo_binario.converter_para_binario(numero)
        assert isinstance(binario, str)
        assert all(c in "01" for c in binario)

    def test_ciclo_completo_resposta_correta(self):
        """Testa o ciclo completo: gera número, converte, verifica"""
        numero = 10
        binario_esperado = jogo_binario.converter_para_binario(numero)
        resposta_correta = jogo_binario.verificar_resposta(numero, binario_esperado)
        assert resposta_correta is True

    def test_ciclo_completo_resposta_incorreta(self):
        """Testa o ciclo completo com resposta errada"""
        numero = 10
        resposta_incorreta = "1111"  # Isso é 15, não 10
        resultado = jogo_binario.verificar_resposta(numero, resposta_incorreta)
        assert resultado is False
