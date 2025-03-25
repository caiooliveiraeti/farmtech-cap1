import math
from services.cultura import listar_culturas

def calcular_area(cultura):
    print(f"\nCalculando área para: {cultura['nome']}")
    valores = {}

    for d in cultura["dimensoes"]:
        valores[d] = float(input(f"Digite o valor de '{d}' em metros: "))

    tipo = cultura["tipo_area"]

    if tipo == "retangular":
        area = valores["largura"] * valores["comprimento"]
    elif tipo == "triangular":
        area = (valores["base"] * valores["altura"]) / 2
    else:
        raise ValueError("Tipo de área desconhecido!")

    print(f"Área calculada: {area:.2f} m²")
    return area, valores


def registrar_area_plantio():
    from models.data import culturas_config, plantios
    listar_culturas()
    idx = int(input("Escolha o índice da cultura para calcular área: "))

    if idx < 0 or idx >= len(culturas_config):
        print("Índice inválido!")
        return

    cultura = culturas_config[idx]
    area, dimensoes_valores = calcular_area(cultura)

    registro = {
        "cultura": cultura["nome"],
        "area": area,
        "dimensoes": dimensoes_valores
    }

    plantios.append(registro)
    print("✅ Registro de plantio adicionado!")


def listar_plantios():
    from models.data import plantios
    print("\n--- Plantios Registrados ---")
    if not plantios:
        print("Nenhum plantio cadastrado.")
        return

    for idx, plantio in enumerate(plantios):
        print(f"{idx}. Cultura: {plantio['cultura']}")
        print(f"   Área: {plantio['area']:.2f} m²")
        print(f"   Dimensões fornecidas: {plantio['dimensoes']}")
