import sqlite3
import os

DATABASE = 'ecommerce.db'

def seed_products():
    """Adiciona produtos de amostra ao banco de dados com imagens"""
    
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
    
    # Lista de produtos de amostra com imagens
    produtos_com_imagens = [
        # Perfumes
        {
            'categoria': cat_perfumes,
            'nome': 'Essência Floral',
            'descricao': 'Perfume feminino com notas florais delicadas',
            'preco': 189.90,
            'sku': 'PERF-001',
            'estoque': 15,
            'peso': 0.1,
            'dimensoes': '5x5x10 cm',
            'marca': 'Essence',
            'imagens': [
                'https://images.unsplash.com/photo-1541643600914-78b084683601?w=500',
                'https://images.unsplash.com/photo-1588405748880-12d1d2a59db9?w=500',
                'https://images.unsplash.com/photo-1592945403244-b3fbafd7f539?w=500'
            ]
        },
        {
            'categoria': cat_perfumes,
            'nome': 'Amadeirado Intenso',
            'descricao': 'Perfume masculino amadeirado e marcante',
            'preco': 215.00,
            'sku': 'PERF-002',
            'estoque': 12,
            'peso': 0.1,
            'dimensoes': '5x5x10 cm',
            'marca': 'Forest',
            'imagens': [
                'https://images.unsplash.com/photo-1585159812596-fac104f2f069?w=500',
                'https://images.unsplash.com/photo-1563170351-be82bc888aa4?w=500'
            ]
        },
        {
            'categoria': cat_perfumes,
            'nome': 'Lavanda Suave',
            'descricao': 'Perfume unissex com lavanda francesa',
            'preco': 149.90,
            'sku': 'PERF-003',
            'estoque': 20,
            'peso': 0.1,
            'dimensoes': '5x5x10 cm',
            'marca': 'Lavande',
            'imagens': [
                'https://images.unsplash.com/photo-1594035910387-fea47794261f?w=500',
                'https://images.unsplash.com/photo-1547887537-6158d64c35b3?w=500'
            ]
        },
        {
            'categoria': cat_perfumes,
            'nome': 'Oriental Misterioso',
            'descricao': 'Perfume oriental com especiarias',
            'preco': 259.90,
            'sku': 'PERF-004',
            'estoque': 8,
            'peso': 0.1,
            'dimensoes': '5x5x10 cm',
            'marca': 'Orient',
            'imagens': [
                'https://images.unsplash.com/photo-1528740561666-dc2479dc08ab?w=500'
            ]
        },
        
        # Roupas
        {
            'categoria': cat_roupas,
            'nome': 'Camiseta Básica Cotton',
            'descricao': 'Camiseta 100% algodão em diversas cores',
            'preco': 79.90,
            'sku': 'ROUPA-001',
            'estoque': 50,
            'peso': 0.2,
            'dimensoes': '30x40 cm',
            'marca': 'BasicWear',
            'imagens': [
                'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=500',
                'https://images.unsplash.com/photo-1583743814966-8936f5b7be1a?w=500'
            ]
        },
        {
            'categoria': cat_roupas,
            'nome': 'Calça Jeans Slim',
            'descricao': 'Calça jeans slim fit premium',
            'preco': 189.90,
            'sku': 'ROUPA-002',
            'estoque': 30,
            'peso': 0.5,
            'dimensoes': '40x50 cm',
            'marca': 'Denim Co',
            'imagens': [
                'https://images.unsplash.com/photo-1542272604-787c3835535d?w=500',
                'https://images.unsplash.com/photo-1598554747436-c9293d6a588f?w=500'
            ]
        },
        {
            'categoria': cat_roupas,
            'nome': 'Vestido Elegante',
            'descricao': 'Vestido social para ocasiões especiais',
            'preco': 299.90,
            'sku': 'ROUPA-003',
            'estoque': 15,
            'peso': 0.3,
            'dimensoes': '35x45 cm',
            'marca': 'Elegance',
            'imagens': [
                'https://images.unsplash.com/photo-1595777457583-95e059d581b8?w=500',
                'https://images.unsplash.com/photo-1566174053879-31528523f8ae?w=500'
            ]
        },
        {
            'categoria': cat_roupas,
            'nome': 'Camisa Social Branca',
            'descricao': 'Camisa social masculina tradicional',
            'preco': 129.90,
            'sku': 'ROUPA-004',
            'estoque': 25,
            'peso': 0.3,
            'dimensoes': '35x45 cm',
            'marca': 'Classic',
            'imagens': [
                'https://images.unsplash.com/photo-1596755094514-f87e34085b2c?w=500',
                'https://images.unsplash.com/photo-1602810318383-e386cc2a3ccf?w=500'
            ]
        },
        {
            'categoria': cat_roupas,
            'nome': 'Jaqueta Jeans',
            'descricao': 'Jaqueta jeans versátil',
            'preco': 249.90,
            'sku': 'ROUPA-005',
            'estoque': 20,
            'peso': 0.6,
            'dimensoes': '45x55 cm',
            'marca': 'Urban',
            'imagens': [
                'https://images.unsplash.com/photo-1551028719-00167b16eac5?w=500'
            ]
        },
        
        # Acessórios
        {
            'categoria': cat_acessorios,
            'nome': 'Colar Dourado',
            'descricao': 'Colar folheado a ouro 18k',
            'preco': 159.90,
            'sku': 'ACESS-001',
            'estoque': 12,
            'peso': 0.05,
            'dimensoes': '5x5x2 cm',
            'marca': 'Gold Line',
            'imagens': [
                'https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?w=500',
                'https://images.unsplash.com/photo-1611591437281-460bfbe1220a?w=500'
            ]
        },
        {
            'categoria': cat_acessorios,
            'nome': 'Pulseira de Couro',
            'descricao': 'Pulseira masculina em couro legítimo',
            'preco': 89.90,
            'sku': 'ACESS-002',
            'estoque': 25,
            'peso': 0.05,
            'dimensoes': '20x3 cm',
            'marca': 'Leather Co',
            'imagens': [
                'https://images.unsplash.com/photo-1611085583191-a3b181a88401?w=500'
            ]
        },
        {
            'categoria': cat_acessorios,
            'nome': 'Óculos de Sol',
            'descricao': 'Óculos de sol com proteção UV',
            'preco': 199.90,
            'sku': 'ACESS-003',
            'estoque': 18,
            'peso': 0.1,
            'dimensoes': '15x6x5 cm',
            'marca': 'SunStyle',
            'imagens': [
                'https://images.unsplash.com/photo-1572635196237-14b3f281503f?w=500',
                'https://images.unsplash.com/photo-1511499767150-a48a237f0083?w=500'
            ]
        },
        {
            'categoria': cat_acessorios,
            'nome': 'Relógio Casual',
            'descricao': 'Relógio casual masculino resistente à água',
            'preco': 349.90,
            'sku': 'ACESS-004',
            'estoque': 10,
            'peso': 0.15,
            'dimensoes': '10x10x3 cm',
            'marca': 'TimeStyle',
            'imagens': [
                'https://images.unsplash.com/photo-1524805444758-089113d48a6d?w=500',
                'https://images.unsplash.com/photo-1523170335258-f5ed11844a49?w=500'
            ]
        },
        {
            'categoria': cat_acessorios,
            'nome': 'Bolsa de Couro',
            'descricao': 'Bolsa feminina em couro sintético',
            'preco': 279.90,
            'sku': 'ACESS-005',
            'estoque': 15,
            'peso': 0.4,
            'dimensoes': '30x25x10 cm',
            'marca': 'BagStyle',
            'imagens': [
                'https://images.unsplash.com/photo-1564422170194-896b89110ef8?w=500',
                'https://images.unsplash.com/photo-1548036328-c9fa89d128fa?w=500'
            ]
        },
        {
            'categoria': cat_acessorios,
            'nome': 'Cinto de Couro',
            'descricao': 'Cinto masculino em couro legítimo',
            'preco': 119.90,
            'sku': 'ACESS-006',
            'estoque': 30,
            'peso': 0.2,
            'dimensoes': '120x4 cm',
            'marca': 'Belt Co',
            'imagens': [
                'https://images.unsplash.com/photo-1624222247344-550fb60583f0?w=500'
            ]
        },
        {
            'categoria': cat_acessorios,
            'nome': 'Carteira Masculina',
            'descricao': 'Carteira em couro com compartimentos',
            'preco': 99.90,
            'sku': 'ACESS-007',
            'estoque': 35,
            'peso': 0.1,
            'dimensoes': '12x10x2 cm',
            'marca': 'Wallet Pro',
            'imagens': [
                'https://images.unsplash.com/photo-1627123424574-724758594e93?w=500',
                'https://images.unsplash.com/photo-1606502281004-f86cf1282af5?w=500'
            ]
        }
    ]
    
    # Inserir produtos e suas imagens
    total_produtos = 0
    total_imagens = 0
    
    for produto_data in produtos_com_imagens:
        # Inserir produto
        cursor.execute('''
            INSERT INTO produtos (categoria_id, nome, descricao, preco, sku, quantidade_estoque, peso, dimensoes, marca)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            produto_data['categoria'],
            produto_data['nome'],
            produto_data['descricao'],
            produto_data['preco'],
            produto_data['sku'],
            produto_data['estoque'],
            produto_data['peso'],
            produto_data['dimensoes'],
            produto_data['marca']
        ))
        
        produto_id = cursor.lastrowid
        total_produtos += 1
        
        # Inserir imagens do produto
        for ordem, url_imagem in enumerate(produto_data['imagens']):
            cursor.execute('''
                INSERT INTO produto_imagens (produto_id, caminho_imagem, ordem)
                VALUES (?, ?, ?)
            ''', (produto_id, url_imagem, ordem))
            total_imagens += 1
    
    conn.commit()
    conn.close()
    
    print(f"✅ {total_produtos} produtos adicionados com sucesso!")
    print(f"📷 {total_imagens} imagens de produtos adicionadas!")

if __name__ == '__main__':
    seed_products()
