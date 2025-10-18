#!/bin/bash

# Script de inicialização para o Render
echo "🚀 Iniciando aplicação..."

# Verificar se o banco de dados existe
if [ ! -f "ecommerce.db" ]; then
    echo "📦 Banco de dados não encontrado. Inicializando..."
    python init_db.py
else
    echo "✓ Banco de dados já existe"
fi

# Iniciar o servidor Gunicorn
echo "🌐 Iniciando servidor Gunicorn..."
exec gunicorn --bind 0.0.0.0:$PORT main:app
