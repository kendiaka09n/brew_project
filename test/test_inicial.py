from src.pipeline.status_api import check_status

def test_verifica_status_api():
    saida=check_status()
    valor_esperado = 200
    assert saida == valor_esperado