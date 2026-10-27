from src.pedido import calcular_taxa_entrega


def test_taxa_para_2_km():
    assert calcular_taxa_entrega(2, 50) == 5


def test_taxa_para_4_km():
    assert calcular_taxa_entrega(4, 50) == 7


def test_entrega_gratis_para_pedido_de_100():
    assert calcular_taxa_entrega(5, 100) == 0
