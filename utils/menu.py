import signal
import sys
from models.data import culturas_config, plantios, manejos
from services.area import registrar_area_plantio, listar_plantios
from services.manejo import registrar_manejo, listar_manejos
from services.cultura import listar_culturas
from services.exporter import exportar_dados_para_csv

def signal_handler(sig, frame):
    print("\nEncerrando o programa. Até mais!")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def menu_principal():
    while True:
        print("\n===== FarmTech Solutions =====")
        print("1. Listar culturas disponíveis")
        print("2. Calcular área de plantio")
        print("3. Listar plantios registrados")
        print("4. Manejo de insumos")
        print("5. Listar manejos de insumos")
        print("6. Exportar dados para CSV")
        print("7. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_culturas()
        elif opcao == "2":
            registrar_area_plantio()
        elif opcao == "3":
            listar_plantios()
        elif opcao == "4":
            registrar_manejo()
        elif opcao == "5":
            listar_manejos()
        elif opcao == "6":
            nome_arquivo = input("Informe o diretório para os arquivos CSV: ")
            exportar_dados_para_csv(nome_arquivo)
        elif opcao == "7":
            print("Encerrando o programa. Até mais!")
            break
        else:
            print("Opção inválida! Tente novamente.")

