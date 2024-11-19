#!/usr/bin/env bash

# Iniciar o backend
echo "Iniciando o backend..."
python3 -m backend.app &

# Mudar para o diretório do frontend
cd frontend || exit

# Iniciar o frontend
echo "Iniciando o frontend..."
npm run dev

# Para rodar no Bash: ./start.sh