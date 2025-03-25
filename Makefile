# Default target
all: exportar_dados calcular_estatisticas

# Target to run the Python script
app:
	python3 main.py

# Target to run the R script
report:
	Rscript rscripts/estatisticas.R

# Clean target (optional)
clean:
	rm -f data/*.csv
