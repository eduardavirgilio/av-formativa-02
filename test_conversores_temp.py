import pytest
from conversores_temp import converter_temperatura

# passando os parametros
@pytest.mark.parametrize("valor, de_escala, para_escala, situacao_esperada",
                         [
                             (200, "KELVIN", "CELSIUS", -73.15), # conversão de kelvin para celsius
                             (320, "KELVIN", "FAHRENHEIT", 116.33), # conversão de kelvin para fahrenheit
                             (32, "celsius", "kelvin", 305.15), # conversão de celsius para kelvin
                             (20, "celsius", "FAHRENHEIT", 68), # conversão de celsius para fahrenheit
                             (102.50, "FAHRENHEIT", "CELSIUS", 39.17), # conversão de fahrenheit para celsius
                             (1000, "fahrenheit", "KELVIN", 810.93), # conversão de fahrenheit para kelvin
                         ])


def test_classificar_conversoes_parametrizadas(valor, de_escala, para_escala, situacao_esperada):
    resultado = converter_temperatura(valor, de_escala, para_escala)

    assert resultado == situacao_esperada

# testes de erro --------------------------------------------------------------------------------------------------------------------------

def test_kelvin_de_escala_negativo():
    # Definindo a entrada
    valor = -200
    de_escala = "KELVIN"
    para_escala = "CELSIUS"

    # Executando a função e esperando erro
    with pytest.raises(ValueError, match="Temperatura em KELVIN não pode ser negativa"):
        converter_temperatura(valor, de_escala, para_escala) 