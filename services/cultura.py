def listar_culturas():
    print("\n--- Culturas Disponíveis ---")
    from models.data import culturas_config
    for idx, cultura in enumerate(culturas_config):
        print(f"{idx}. {cultura['nome']} (Tipo de área: {cultura['tipo_area']}, Dimensões: {', '.join(cultura['dimensoes'])})")

