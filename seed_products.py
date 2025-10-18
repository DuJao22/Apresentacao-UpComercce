import sqlite3
import os

DATABASE = 'ecommerce.db'

def seed_products():
    """Adiciona produtos de amostra ao banco de dados"""
    
    if not os.path.exists(DATABASE):
        print(f"❌ Erro: Banco de dados não encontrado: {DATABASE}")
        return
    
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    print("🌱 Adicionando produtos de amostra...")
    
    # Verificar se já existem produtos
    cursor.execute("SELECT COUNT(*) FROM produtos")
    count = cursor.fetchone()[0]
    
    if count > 0:
        print(f"• Já existem {count} produtos no banco. Pulando seed.")
        conn.close()
        return
    
    # Obter IDs das categorias
    cursor.execute("SELECT id FROM categorias WHERE slug = 'perfumes'")
    cat_perfumes = cursor.fetchone()[0]
    
    cursor.execute("SELECT id FROM categorias WHERE slug = 'roupas'")
    cat_roupas = cursor.fetchone()[0]
    
    cursor.execute("SELECT id FROM categorias WHERE slug = 'acessorios'")
    cat_acessorios = cursor.fetchone()[0]
    
    # Lista de produtos de amostra
    produtos = [
        # Perfumes
        (cat_perfumes, 'Essência Floral', 'Perfume feminino com notas florais delicadas', 189.90, 'PERF-001', 15, 0.1, '5x5x10 cm', 'Essence'),
        (cat_perfumes, 'Amadeirado Intenso', 'Perfume masculino amadeirado e marcante', 215.00, 'PERF-002', 12, 0.1, '5x5x10 cm', 'Forest'),
        (cat_perfumes, 'Lavanda Suave', 'Perfume unissex com lavanda francesa', 149.90, 'PERF-003', 20, 0.1, '5x5x10 cm', 'Lavande'),
        (cat_perfumes, 'Oriental Misterioso', 'Perfume oriental com especiarias', 259.90, 'PERF-004', 8, 0.1, '5x5x10 cm', 'Orient'),
        (cat_perfumes, 'Cítrico Refrescante', 'Perfume cítrico para o dia a dia', 169.90, 'PERF-005', 18, 0.1, '5x5x10 cm', 'Citrus'),
        
        # Roupas
        (cat_roupas, 'Camiseta Básica Cotton', 'Camiseta 100% algodão em diversas cores', 79.90, 'ROUPA-001', 50, 0.2, '30x40 cm', 'BasicWear'),
        (cat_roupas, 'Calça Jeans Slim', 'Calça jeans slim fit premium', 189.90, 'ROUPA-002', 30, 0.5, '40x50 cm', 'Denim Co'),
        (cat_roupas, 'Vestido Elegante', 'Vestido social para ocasiões especiais', 299.90, 'ROUPA-003', 15, 0.3, '35x45 cm', 'Elegance'),
        (cat_roupas, 'Camisa Social Branca', 'Camisa social masculina tradicional', 129.90, 'ROUPA-004', 25, 0.3, '35x45 cm', 'Classic'),
        (cat_roupas, 'Jaqueta Jeans', 'Jaqueta jeans versátil', 249.90, 'ROUPA-005', 20, 0.6, '45x55 cm', 'Urban'),
        
        # Acessórios
        (cat_acessorios, 'Colar Dourado', 'Colar folheado a ouro 18k', 159.90, 'ACESS-001', 12, 0.05, '5x5x2 cm', 'Gold Line'),
        (cat_acessorios, 'Pulseira de Couro', 'Pulseira masculina em couro legítimo', 89.90, 'ACESS-002', 25, 0.05, '20x3 cm', 'Leather Co'),
        (cat_acessorios, 'Óculos de Sol', 'Óculos de sol com proteção UV', 199.90, 'ACESS-003', 18, 0.1, '15x6x5 cm', 'SunStyle'),
        (cat_acessorios, 'Relógio Casual', 'Relógio casual masculino resistente à água', 349.90, 'ACESS-004', 10, 0.15, '10x10x3 cm', 'TimeStyle'),
        (cat_acessorios, 'Bolsa de Couro', 'Bolsa feminina em couro sintético', 279.90, 'ACESS-005', 15, 0.4, '30x25x10 cm', 'BagStyle'),
        (cat_acessorios, 'Cinto de Couro', 'Cinto masculino em couro legítimo', 119.90, 'ACESS-006', 30, 0.2, '120x4 cm', 'Belt Co'),
        (cat_acessorios, 'Brincos Pérola', 'Brincos com pérolas cultivadas', 139.90, 'ACESS-007', 20, 0.02, '3x3x2 cm', 'Pearl'),
        (cat_acessorios, 'Carteira Masculina', 'Carteira em couro com compartimentos', 99.90, 'ACESS-008', 35, 0.1, '12x10x2 cm', 'Wallet Pro'),
        (cat_acessorios, 'Lenço de Seda', 'Lenço feminino em seda pura', 89.90, 'ACESS-009', 22, 0.05, '90x90 cm', 'Silk Style'),
    ]
    
    # Inserir produtos
    for produto in produtos:
        cursor.execute('''
            INSERT INTO produtos (categoria_id, nome, descricao, preco, sku, quantidade_estoque, peso, dimensoes, marca)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', produto)
    
    conn.commit()
    
    # Verificar quantos foram inseridos
    cursor.execute("SELECT COUNT(*) FROM produtos")
    total = cursor.fetchone()[0]
    
    conn.close()
    
    print(f"✅ {total} produtos de amostra adicionados com sucesso!")

if __name__ == '__main__':
    seed_products()
