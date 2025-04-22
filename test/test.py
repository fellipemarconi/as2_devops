import pytest
from unittest.mock import patch
from src.main import *

@pytest.mark.asyncio
async def test_funcaoteste():
    with patch('random.randint', return_value=12345):
        result = await funcaoteste()  # Aguardar a coroutine
        assert result == {"teste": True, "num_aleatorio": 12345}


@pytest.mark.asyncio
async def test_create_estudante():
    estudante_teste = Estudante(name="Fulano", curso="Curso 1", ativo=False)
    result = await create_estudante(estudante_teste)  # Aguardar a coroutine
    assert estudante_teste == result


@pytest.mark.asyncio
async def test_update_estudante_negativo():
    result = await update_estudante(-5)  # Aguardar a coroutine
    assert not result


@pytest.mark.asyncio
async def test_delete_estudante_negativo():
    result = await delete_estudante(-5)  # Aguardar a coroutine
    assert not result


@pytest.mark.asyncio
async def test_update_estudante_positivo():
    result = await update_estudante(10)  # Aguardar a coroutine
    assert result


@pytest.mark.asyncio
async def test_delete_estudante_positivo():
    estudante_teste = Estudante(name="Fulano", curso="Curso 1", ativo=True)
    await create_estudante(estudante_teste)  # Aguardar a criação
    result = await delete_estudante(5)  # Aguardar a exclusão
    assert result




