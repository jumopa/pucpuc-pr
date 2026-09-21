import pytest

# 5 Testes unitários 
def test_somar():
    assert somar(2, 3) == 5

def test_subtrair():
    assert subtrair(5, 2) == 3

def test_multiplicar():
    assert multiplicar(3, 4) == 12

def test_dividir():
    assert dividir(10, 2) == 5

def test_eh_par():
    assert eh_par(4) is True
    assert eh_par(5) is False
