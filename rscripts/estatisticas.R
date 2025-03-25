# Carregar bibliotecas necessárias
# Função para calcular estatísticas dos plantios
calcular_estatisticas_plantios <- function(caminho_arquivo) {
  dados_plantios <- read.csv(caminho_arquivo)
  
  # Calcular média e desvio padrão da área
  media_area <- mean(dados_plantios$Area)
  desvio_padrao_area <- sd(dados_plantios$Area)
  
  cat("\nEstatísticas dos Plantios:\n")
  cat("Média da Área (m²):", media_area, "\n")
  cat("Desvio Padrão da Área (m²):", desvio_padrao_area, "\n")
}

# Função para calcular estatísticas dos manejos
calcular_estatisticas_manejos <- function(caminho_arquivo) {
  dados_manejos <- read.csv(caminho_arquivo)
  
  # Calcular média e desvio padrão da quantidade total
  media_quantidade_total <- mean(dados_manejos$QuantidadeTotal)
  desvio_padrao_quantidade_total <- sd(dados_manejos$QuantidadeTotal)
  
  cat("\nEstatísticas dos Manejos:\n")
  cat("Média da Quantidade Total (mL):", media_quantidade_total, "\n")
  cat("Desvio Padrão da Quantidade Total (mL):", desvio_padrao_quantidade_total, "\n")
}


arquivo_plantios <- "data/plantios.csv"
arquivo_manejos <- "data/manejos.csv"

if (file.exists(arquivo_plantios)) {
  calcular_estatisticas_plantios(arquivo_plantios)
} else {
  cat("Arquivo de plantios não encontrado.\n")
}

if (file.exists(arquivo_manejos)) {
  calcular_estatisticas_manejos(arquivo_manejos)
} else {
  cat("Arquivo de manejos não encontrado.\n")
}
