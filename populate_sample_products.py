import sqlite3

def populate_sample_products():
    conn = sqlite3.connect('ecommerce.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT id FROM categorias WHERE nome = "Perfumes"')
    categoria_perfumes = cursor.fetchone()
    if categoria_perfumes:
        categoria_perfumes_id = categoria_perfumes[0]
    else:
        cursor.execute('INSERT INTO categorias (nome, descricao, slug) VALUES (?, ?, ?)',
                      ('Perfumes', 'Fragrâncias importadas e nacionais', 'perfumes'))
        categoria_perfumes_id = cursor.lastrowid
    
    cursor.execute('SELECT id FROM categorias WHERE nome = "Roupas"')
    categoria_roupas = cursor.fetchone()
    if categoria_roupas:
        categoria_roupas_id = categoria_roupas[0]
    else:
        cursor.execute('INSERT INTO categorias (nome, descricao, slug) VALUES (?, ?, ?)',
                      ('Roupas', 'Moda feminina e masculina', 'roupas'))
        categoria_roupas_id = cursor.lastrowid
    
    cursor.execute('SELECT id FROM categorias WHERE nome = "Acessórios"')
    categoria_acessorios = cursor.fetchone()
    if categoria_acessorios:
        categoria_acessorios_id = categoria_acessorios[0]
    else:
        cursor.execute('INSERT INTO categorias (nome, descricao, slug) VALUES (?, ?, ?)',
                      ('Acessórios', 'Bolsas, relógios e joias', 'acessorios'))
        categoria_acessorios_id = cursor.lastrowid
    
    perfumes = [
        ('Essência Floral', 'Perfume feminino com notas florais e cítricas. Fixação de 8 horas.', 189.90, 'PERF001', 25, '0.15kg', '50ml', 'Luxe Paris'),
        ('Amadeirado Intenso', 'Perfume masculino com notas amadeiradas. Fixação prolongada.', 215.00, 'PERF002', 18, '0.25kg', '100ml', 'Elite Fragrance'),
        ('Lavanda Suave', 'Perfume unissex com lavanda e notas suaves. Ideal para o dia a dia.', 149.90, 'PERF003', 30, '0.15kg', '50ml', 'Natural Scents'),
        ('Oriental Misterioso', 'Perfume feminino oriental com especiarias e flores exóticas.', 259.90, 'PERF004', 15, '0.2kg', '75ml', 'Luxe Paris'),
        ('Citrus Fresh', 'Perfume masculino refrescante com cítricos e menta.', 179.00, 'PERF005', 22, '0.25kg', '100ml', 'Fresh Collection'),
    ]
    
    roupas = [
        ('Vestido Floral Elegante', 'Vestido longo com estampa floral. Tecido leve e confortável.', 199.90, 'VEST001', 15, '0.3kg', 'P/M/G', 'Belle Fashion'),
        ('Camisa Social Masculina', 'Camisa social slim fit. 100% algodão. Cores: Branco, Azul.', 129.90, 'CAM001', 25, '0.2kg', 'P/M/G/GG', 'Urban Style'),
        ('Calça Jeans Feminina', 'Calça jeans skinny de cintura alta. Muito confortável.', 179.90, 'CAL001', 20, '0.4kg', '36/38/40/42', 'Denim Co'),
        ('Blazer Executivo', 'Blazer masculino para trabalho. Corte moderno e elegante.', 299.90, 'BLZ001', 12, '0.5kg', 'P/M/G/GG', 'Executive Look'),
        ('Saia Midi Plissada', 'Saia midi plissada. Elegante e versátil para várias ocasiões.', 149.90, 'SAI001', 18, '0.25kg', 'P/M/G', 'Belle Fashion'),
        ('Camiseta Básica Premium', 'Camiseta 100% algodão. Alta qualidade. Diversas cores.', 79.90, 'CAM002', 40, '0.15kg', 'P/M/G/GG', 'Basic Collection'),
    ]
    
    acessorios = [
        ('Bolsa de Couro Clássica', 'Bolsa de couro legítimo. Espaçosa e elegante. Cor: Preto.', 349.90, 'BOLS001', 10, '0.8kg', '35x25x12cm', 'Leather Goods'),
        ('Relógio Digital Esportivo', 'Relógio digital à prova d\'água. Cronômetro e alarme.', 189.90, 'REL001', 15, '0.1kg', 'Ajustável', 'TimeZone'),
        ('Óculos de Sol Premium', 'Óculos de sol com proteção UV400. Armação em acetato.', 249.90, 'OCU001', 20, '0.05kg', 'Único', 'SunStyle'),
        ('Carteira de Couro', 'Carteira masculina em couro legítimo. Vários compartimentos.', 129.90, 'CART001', 25, '0.15kg', '11x9cm', 'Leather Goods'),
        ('Cinto de Couro Reversível', 'Cinto reversível preto/marrom. Fivela elegante.', 99.90, 'CINT001', 30, '0.2kg', 'Ajustável', 'Leather Goods'),
        ('Colar Dourado Delicado', 'Colar folheado a ouro com pingente coração. Elegante.', 159.90, 'COL001', 12, '0.02kg', '45cm', 'Jewel Style'),
        ('Pulseira de Couro Trançada', 'Pulseira masculina em couro trançado. Estilo casual.', 69.90, 'PULS001', 28, '0.03kg', 'Ajustável', 'Urban Style'),
    ]
    
    print("Adicionando perfumes...")
    for produto in perfumes:
        try:
            cursor.execute('''
                INSERT INTO produtos (categoria_id, nome, descricao, preco, sku, quantidade_estoque, peso, dimensoes, marca, ativo)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 1)
            ''', (categoria_perfumes_id,) + produto)
            print(f"  ✓ {produto[0]}")
        except sqlite3.IntegrityError:
            print(f"  - {produto[0]} (já existe)")
    
    print("\nAdicionando roupas...")
    for produto in roupas:
        try:
            cursor.execute('''
                INSERT INTO produtos (categoria_id, nome, descricao, preco, sku, quantidade_estoque, peso, dimensoes, marca, ativo)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 1)
            ''', (categoria_roupas_id,) + produto)
            print(f"  ✓ {produto[0]}")
        except sqlite3.IntegrityError:
            print(f"  - {produto[0]} (já existe)")
    
    print("\nAdicionando acessórios...")
    for produto in acessorios:
        try:
            cursor.execute('''
                INSERT INTO produtos (categoria_id, nome, descricao, preco, sku, quantidade_estoque, peso, dimensoes, marca, ativo)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 1)
            ''', (categoria_acessorios_id,) + produto)
            print(f"  ✓ {produto[0]}")
        except sqlite3.IntegrityError:
            print(f"  - {produto[0]} (já existe)")
    
    conn.commit()
    conn.close()
    print("\n✅ Produtos de exemplo adicionados com sucesso!")
    print(f"Total de {len(perfumes)} perfumes, {len(roupas)} roupas e {len(acessorios)} acessórios.")

if __name__ == '__main__':
    populate_sample_products()
