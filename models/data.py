# Configuração das culturas disponíveis
culturas_config = [
    {"nome": "Soja", "tipo_area": "retangular", "dimensoes": ["largura", "comprimento"]},
    {"nome": "Milho", "tipo_area": "triangular", "dimensoes": ["base", "altura"]},
]

# Dados dinâmicos (registro das áreas e manejos calculados)
plantios = [
    {'id': '1e7b7f8e-8c9a-11ee-8c99-0242ac120002', 'cultura': 'Soja', 'area': 20000.0, 'dimensoes': {'largura': 100.0, 'comprimento': 200.0}},
    {'id': '1e7b80b6-8c9a-11ee-8c99-0242ac120002', 'cultura': 'Milho', 'area': 60000.0, 'dimensoes': {'base': 300.0, 'altura': 400.0}},
]

manejos = [
    {'id': '1e7b81d4-8c9a-11ee-8c99-0242ac120002', 'plantio_id': '1e7b7f8e-8c9a-11ee-8c99-0242ac120002', 'cultura': 'Soja', 'produto': 'Fertilizante NPK', 'quantidade_por_metro': 1.0, 'quantidade_total': 20000.0},
    {'id': '1e7b82f2-8c9a-11ee-8c99-0242ac120002', 'plantio_id': '1e7b7f8e-8c9a-11ee-8c99-0242ac120002', 'cultura': 'Soja', 'produto': 'Pulverizador biológico', 'quantidade_por_metro': 2.0, 'quantidade_total': 40000.0},
    {'id': '1e7b8410-8c9a-11ee-8c99-0242ac120002', 'plantio_id': '1e7b80b6-8c9a-11ee-8c99-0242ac120002', 'cultura': 'Milho', 'produto': 'Herbicida A', 'quantidade_por_metro': 1.0, 'quantidade_total': 60000.0},
    {'id': '1e7b852e-8c9a-11ee-8c99-0242ac120002', 'plantio_id': '1e7b80b6-8c9a-11ee-8c99-0242ac120002', 'cultura': 'Milho', 'produto': 'Ureia', 'quantidade_por_metro': 0.5, 'quantidade_total': 30000.0},
]