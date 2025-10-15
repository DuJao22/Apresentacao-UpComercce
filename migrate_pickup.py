import sqlite3

DATABASE = 'ecommerce.db'

def migrate():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Adicionar campos na tabela configuracoes_loja
    try:
        cursor.execute('ALTER TABLE configuracoes_loja ADD COLUMN local_retirada TEXT')
        print("✓ Campo 'local_retirada' adicionado à tabela configuracoes_loja")
    except sqlite3.OperationalError as e:
        print(f"Campo 'local_retirada' já existe ou erro: {e}")
    
    try:
        cursor.execute('ALTER TABLE configuracoes_loja ADD COLUMN email_notificacao TEXT')
        print("✓ Campo 'email_notificacao' adicionado à tabela configuracoes_loja")
    except sqlite3.OperationalError as e:
        print(f"Campo 'email_notificacao' já existe ou erro: {e}")
    
    # Adicionar campo na tabela pedidos
    try:
        cursor.execute('ALTER TABLE pedidos ADD COLUMN tipo_entrega TEXT DEFAULT "entrega"')
        print("✓ Campo 'tipo_entrega' adicionado à tabela pedidos")
    except sqlite3.OperationalError as e:
        print(f"Campo 'tipo_entrega' já existe ou erro: {e}")
    
    conn.commit()
    conn.close()
    print("\n✓ Migração concluída com sucesso!")

if __name__ == '__main__':
    migrate()
