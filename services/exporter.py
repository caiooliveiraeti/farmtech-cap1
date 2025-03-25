import csv
import os
from models.data import plantios, manejos

def exportar_dados_para_csv(pasta="data"):
    if not os.path.exists(pasta):
        os.makedirs(pasta)
    
    # Exportar dados de plantios
    nome_arquivo_plantios = os.path.join(pasta, "plantios.csv")
    with open(nome_arquivo_plantios, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Escrever cabeçalho
        writer.writerow(["Tipo", "Cultura", "Area", "Dimensoes"])
        
        # Escrever dados de plantios
        for plantio in plantios:
            writer.writerow([
                "Plantio",
                plantio["cultura"],
                plantio["area"],
                "; ".join([f"{k}: {v}" for k, v in plantio["dimensoes"].items()])
            ])
    
    # Exportar dados de manejos
    nome_arquivo_manejos = os.path.join(pasta, "manejos.csv")
    with open(nome_arquivo_manejos, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Escrever cabeçalho
        writer.writerow(["Tipo", "Cultura", "Produto", "Quantidade", "QuantidadeTotal"])
        
        # Escrever dados de manejos
        for manejo in manejos:
            writer.writerow([
                "Manejo",
                manejo["cultura"],
                manejo["produto"],
                manejo["quantidade_por_metro"],
                manejo["quantidade_total"]
            ])

    print(f"✅ Dados de plantios exportados com sucesso para {nome_arquivo_plantios}")
    print(f"✅ Dados de manejos exportados com sucesso para {nome_arquivo_manejos}")
