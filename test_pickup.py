import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()

# 1. Verificar se os campos foram adicionados
print("=== Verificando estrutura das tabelas ===\n")

cursor.execute("PRAGMA table_info(configuracoes_loja)")
print("Campos da tabela configuracoes_loja:")
for row in cursor.fetchall():
    print(f"  - {row[1]} ({row[2]})")

print("\n")

cursor.execute("PRAGMA table_info(pedidos)")
print("Campos da tabela pedidos:")
for row in cursor.fetchall():
    print(f"  - {row[1]} ({row[2]})")

# 2. Atualizar configurações com local de retirada de teste
print("\n=== Atualizando configurações de teste ===\n")

cursor.execute('''
    UPDATE configuracoes_loja 
    SET local_retirada = ?, 
        email_notificacao = ? 
    WHERE id = 1
''', (
    'Rua Exemplo, 123 - Centro\nCidade - Estado\nCEP: 12345-678\n\nHorário de funcionamento: Segunda a Sexta, 9h às 18h',
    'admin@ecommerce.com'
))

conn.commit()

# 3. Verificar se foi atualizado
cursor.execute("SELECT * FROM configuracoes_loja WHERE id = 1")
config = cursor.fetchone()
print("Configurações atualizadas:")
print(f"  Nome da Loja: {config[1]}")
print(f"  Local de Retirada: {config[6]}")
print(f"  Email Notificação: {config[7]}")

# 4. Verificar pedidos existentes
print("\n=== Verificando pedidos existentes ===\n")
cursor.execute("SELECT id, usuario_id, total, tipo_entrega, status FROM pedidos ORDER BY criado_em DESC LIMIT 5")
pedidos = cursor.fetchall()

if pedidos:
    print("Últimos 5 pedidos:")
    for p in pedidos:
        tipo = p[3] if p[3] else 'entrega'
        print(f"  Pedido #{p[0]} - R$ {p[2]:.2f} - Tipo: {tipo} - Status: {p[4]}")
else:
    print("Nenhum pedido encontrado.")

conn.close()
print("\n✓ Teste concluído com sucesso!")
