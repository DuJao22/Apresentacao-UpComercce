import sqlite3
import shutil
import os
from pathlib import Path

def add_product_images():
    conn = sqlite3.connect('ecommerce.db')
    cursor = conn.cursor()
    
    os.makedirs('app/static/uploads/products', exist_ok=True)
    
    image_mapping = {
        'PERF001': [
            'attached_assets/stock_images/luxury_perfume_bottl_6f8ca8f2.jpg',
            'attached_assets/stock_images/luxury_perfume_bottl_df803223.jpg',
            'attached_assets/stock_images/luxury_perfume_bottl_d4d86bcf.jpg',
        ],
        'PERF002': [
            'attached_assets/stock_images/luxury_perfume_bottl_d7899f0a.jpg',
            'attached_assets/stock_images/luxury_perfume_bottl_5bcf218a.jpg',
            'attached_assets/stock_images/luxury_perfume_bottl_6f8ca8f2.jpg',
        ],
        'PERF003': [
            'attached_assets/stock_images/luxury_perfume_bottl_df803223.jpg',
            'attached_assets/stock_images/luxury_perfume_bottl_d7899f0a.jpg',
            'attached_assets/stock_images/luxury_perfume_bottl_d4d86bcf.jpg',
        ],
        'PERF004': [
            'attached_assets/stock_images/luxury_perfume_bottl_5bcf218a.jpg',
            'attached_assets/stock_images/luxury_perfume_bottl_6f8ca8f2.jpg',
            'attached_assets/stock_images/luxury_perfume_bottl_df803223.jpg',
        ],
        'PERF005': [
            'attached_assets/stock_images/luxury_perfume_bottl_d4d86bcf.jpg',
            'attached_assets/stock_images/luxury_perfume_bottl_d7899f0a.jpg',
            'attached_assets/stock_images/luxury_perfume_bottl_5bcf218a.jpg',
        ],
        'VEST001': [
            'attached_assets/stock_images/elegant_dress_fashio_f817924f.jpg',
            'attached_assets/stock_images/elegant_dress_fashio_c342373d.jpg',
            'attached_assets/stock_images/elegant_dress_fashio_d18daa73.jpg',
        ],
        'CAM001': [
            'attached_assets/stock_images/men_formal_shirt_whi_8c44654d.jpg',
            'attached_assets/stock_images/men_formal_shirt_whi_e2e619e0.jpg',
            'attached_assets/stock_images/men_formal_shirt_whi_fe616b53.jpg',
        ],
        'CAL001': [
            'attached_assets/stock_images/women_jeans_denim_fa_c54d0174.jpg',
            'attached_assets/stock_images/women_jeans_denim_fa_16e8845b.jpg',
            'attached_assets/stock_images/women_jeans_denim_fa_10a4dd8f.jpg',
        ],
        'BLZ001': [
            'attached_assets/stock_images/men_blazer_suit_eleg_891a9ffb.jpg',
            'attached_assets/stock_images/men_blazer_suit_eleg_e3a67d35.jpg',
            'attached_assets/stock_images/men_blazer_suit_eleg_2e21f74d.jpg',
        ],
        'SAI001': [
            'attached_assets/stock_images/women_pleated_skirt__ba56008a.jpg',
            'attached_assets/stock_images/women_pleated_skirt__55916b05.jpg',
            'attached_assets/stock_images/women_pleated_skirt__220831d7.jpg',
        ],
        'CAM002': [
            'attached_assets/stock_images/basic_t-shirt_cotton_bf440eb7.jpg',
            'attached_assets/stock_images/basic_t-shirt_cotton_79937013.jpg',
            'attached_assets/stock_images/basic_t-shirt_cotton_a79a460c.jpg',
        ],
        'BOLS001': [
            'attached_assets/stock_images/leather_handbag_luxu_5b278583.jpg',
            'attached_assets/stock_images/leather_handbag_luxu_9b534bd1.jpg',
            'attached_assets/stock_images/leather_handbag_luxu_0c95ff80.jpg',
        ],
        'REL001': [
            'attached_assets/stock_images/sport_digital_watch_a835ca8f.jpg',
            'attached_assets/stock_images/sport_digital_watch_cc0a304c.jpg',
            'attached_assets/stock_images/sport_digital_watch_b3ee0fe6.jpg',
        ],
        'OCU001': [
            'attached_assets/stock_images/sunglasses_fashion_l_dfd85867.jpg',
            'attached_assets/stock_images/sunglasses_fashion_l_9048b82a.jpg',
            'attached_assets/stock_images/sunglasses_fashion_l_262a0d43.jpg',
        ],
        'CART001': [
            'attached_assets/stock_images/leather_wallet_men_a3808cb2.jpg',
            'attached_assets/stock_images/leather_wallet_men_8fb0a578.jpg',
            'attached_assets/stock_images/leather_wallet_men_8d954a4c.jpg',
        ],
        'CINT001': [
            'attached_assets/stock_images/leather_belt_elegant_a5c12f8a.jpg',
            'attached_assets/stock_images/leather_belt_elegant_6b7bd4c2.jpg',
            'attached_assets/stock_images/leather_belt_elegant_d1ef7be8.jpg',
        ],
        'COL001': [
            'attached_assets/stock_images/gold_necklace_jewelr_b4a69069.jpg',
            'attached_assets/stock_images/gold_necklace_jewelr_4046d7a0.jpg',
            'attached_assets/stock_images/gold_necklace_jewelr_893154a9.jpg',
        ],
        'PULS001': [
            'attached_assets/stock_images/leather_bracelet_men_002822db.jpg',
            'attached_assets/stock_images/leather_bracelet_men_1225efcb.jpg',
            'attached_assets/stock_images/leather_bracelet_men_b0027ab3.jpg',
        ],
    }
    
    print("Adicionando imagens aos produtos...\n")
    
    for sku, image_paths in image_mapping.items():
        cursor.execute('SELECT id, nome FROM produtos WHERE sku = ?', (sku,))
        produto = cursor.fetchone()
        
        if not produto:
            print(f"  ⚠ Produto {sku} não encontrado")
            continue
        
        produto_id, produto_nome = produto
        print(f"Produto: {produto_nome} (SKU: {sku})")
        
        for ordem, source_path in enumerate(image_paths, start=1):
            if not os.path.exists(source_path):
                print(f"  ⚠ Imagem não encontrada: {source_path}")
                continue
            
            filename = os.path.basename(source_path)
            dest_path = f'app/static/uploads/products/{filename}'
            
            shutil.copy2(source_path, dest_path)
            
            db_path = f'uploads/products/{filename}'
            
            cursor.execute('''
                INSERT INTO produto_imagens (produto_id, caminho_imagem, ordem)
                VALUES (?, ?, ?)
            ''', (produto_id, db_path, ordem))
            
            print(f"  ✓ Imagem {ordem} adicionada")
        
        print()
    
    conn.commit()
    conn.close()
    print("✅ Todas as imagens foram adicionadas com sucesso!")

if __name__ == '__main__':
    add_product_images()
