def calcular_manejo(area, cultura_nome):
    print(f"\nManejo de insumos para a cultura: {cultura_nome}")
    produto = input("Informe o nome do produto: ")
    quantidade_por_metro = float(input("Quantidade aplicada por m² (mL): "))

    quantidade_total = quantidade_por_metro * area

    print(f"Será necessário {quantidade_total:.2f} mL de {produto} para {area:.2f} m².")

    return {
        "produto": produto,
        "quantidade_por_metro": quantidade_por_metro,
        "quantidade_total": quantidade_total
    }


def registrar_manejo():
    from models.data import plantios, manejos
    if not plantios:
        print("\n⚠️ Nenhum plantio registrado. Cadastre uma área primeiro.")
        return

    print("\n--- Plantios Registrados ---")
    for idx, plantio in enumerate(plantios):
        print(f"{idx}. Cultura: {plantio['cultura']}, Área: {plantio['area']:.2f} m²")

    idx = int(input("Escolha o índice do plantio para manejo: "))

    if idx < 0 or idx >= len(plantios):
        print("Índice inválido!")
        return

    plantio = plantios[idx]
    manejo = calcular_manejo(plantio['area'], plantio['cultura'])
    manejo["cultura"] = plantio['cultura']

    manejos.append(manejo)
    print("✅ Manejo registrado com sucesso!")

def listar_manejos():
    from models.data import manejos
    print("\n--- Manejos Registrados ---")
    if not manejos:
        print("Nenhum manejo registrado.")
        return

    for idx, manejo in enumerate(manejos):
        print(f"{idx}. Cultura: {manejo['cultura']}")
        print(f"   Produto: {manejo['produto']}")
        print(f"   Quantidade por m²: {manejo['quantidade_por_metro']} mL")
        print(f"   Quantidade total: {manejo['quantidade_total']:.2f} mL")
