import signal
import sys
from models.data import culturas_config, plantios, manejos
from services.area import registrar_area_plantio, listar_plantios, deletar_plantio
from services.manejo import registrar_manejo, listar_manejos, deletar_manejo
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
        print("2. Registrar área de plantio")
        print("3. Listar plantios")
        print("4. Deletar plantio")

        print("5. Registrar Manejo de insumos")
        print("6. Listar manejos de insumos")
        print("7. Deletar manejo")
        
        print("8. Exportar dados para CSV")
        print("9. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_culturas()
        elif opcao == "2":
            registrar_area_plantio()
        elif opcao == "3":
            listar_plantios()
        elif opcao == "4":
            deletar_plantio()

        elif opcao == "5":
            registrar_manejo()
        elif opcao == "6":
            listar_manejos()
        elif opcao == "7":
            deletar_manejo()

        elif opcao == "8":
            nome_arquivo = input("Informe o diretório para os arquivos CSV: ")
            exportar_dados_para_csv(nome_arquivo)

        elif opcao == "9":
            print("Encerrando o programa. Até mais!")
            break
        else:
            print("Opção inválida! Tente novamente.")

