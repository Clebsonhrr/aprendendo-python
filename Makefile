printar-nome:
	echo 'vitas gostoso'

criar-venv: 
	python3 -m venv .venv

mover-venv: 
	mv ./.venv ./trabalho/

deletar-venv:
	rm -rf ./trabalho/.venv

preparar-trabalho:
	make criar-venv
	make mover-venv

instalar-bibliotecas:
	./trabalho/.venv/bin/python -m pip install pandas openpyxl
	