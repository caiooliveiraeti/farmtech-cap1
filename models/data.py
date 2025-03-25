# Configuração das culturas disponíveis
culturas_config = [
    {"nome": "Soja", "tipo_area": "retangular", "dimensoes": ["largura", "comprimento"]},
    {"nome": "Milho", "tipo_area": "triangular", "dimensoes": ["base", "altura"]},
]

# Dados dinâmicos (registro das áreas e manejos calculados)
plantios = [
    {'cultura': 'Soja', 'area': 20000.0, 'dimensoes': {'largura': 100.0, 'comprimento': 200.0}},
    {'cultura': 'Milho', 'area': 60000.0, 'dimensoes': {'base': 300.0, 'altura': 400.0}},
]
manejos = [
    {'cultura': 'Soja', 'produto': 'Fertilizante NPK', 'quantidade_por_metro': 1.0, 'quantidade_total': 20000.0},
    {'cultura': 'Soja', 'produto': 'Pulverizador biológico', 'quantidade_por_metro': 2.0, 'quantidade_total': 40000.0},
    {'cultura': 'Milho', 'produto': 'Herbicida A', 'quantidade_por_metro': 1.0, 'quantidade_total': 60000.0},
    {'cultura': 'Milho', 'produto': 'Ureia', 'quantidade_por_metro': 0.5, 'quantidade_total': 30000.0}
]