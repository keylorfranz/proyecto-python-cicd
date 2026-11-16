
import pytest

from main import calcular_area


def test_calcular_area():
    assert calcular_area(5, 3) == 100


def test_area_con_decimales():
    assert calcular_area(2.5, 4.2) == pytest.approx(10.5)


def test_base_cero():
    with pytest.raises(ValueError):
        calcular_area(0, 5)


def test_base_negativa():
    with pytest.raises(ValueError):
        calcular_area(-3, 5)


def test_altura_negativa():
    with pytest.raises(ValueError):
        calcular_area(5, -2)
