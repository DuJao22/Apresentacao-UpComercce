from flask import Blueprint, render_template, request, redirect, url_for, flash, session, jsonify
from app.utils.db import query_db, execute_db
from app.utils.decorators import login_required

cart_bp = Blueprint('cart', __name__, url_prefix='/carrinho')

@cart_bp.route('/')
def index():
    cart = session.get('cart', {})
    cart_items = []
    total = 0
    
    for product_id, item in cart.items():
        produto = query_db('''
            SELECT p.*, 
                   (SELECT caminho_imagem FROM produto_imagens WHERE produto_id = p.id ORDER BY ordem LIMIT 1) as imagem_principal
            FROM produtos p
            WHERE p.id = ?
        ''', [product_id], one=True)
        
        if produto:
            subtotal = produto['preco'] * item['quantity']
            cart_items.append({
                'produto': produto,
                'quantity': item['quantity'],
                'subtotal': subtotal
            })
            total += subtotal
    
    return render_template('shop/cart.html', cart_items=cart_items, total=total)

@cart_bp.route('/adicionar', methods=['POST'])
def adicionar():
    product_id = request.form.get('product_id')
    quantity = int(request.form.get('quantity', 1))
    
    produto = query_db('SELECT * FROM produtos WHERE id = ? AND ativo = 1', [product_id], one=True)
    
    if not produto:
        flash('Produto não encontrado.', 'danger')
        return redirect(url_for('shop.index'))
    
    if produto['quantidade_estoque'] < quantity:
        flash('Quantidade indisponível em estoque.', 'danger')
        return redirect(url_for('shop.produto', id=product_id))
    
    cart = session.get('cart', {})
    
    if product_id in cart:
        cart[product_id]['quantity'] += quantity
    else:
        cart[product_id] = {'quantity': quantity}
    
    session['cart'] = cart
    flash(f'{produto["nome"]} adicionado ao carrinho!', 'success')
    return redirect(url_for('shop.produto', id=product_id))

@cart_bp.route('/atualizar', methods=['POST'])
def atualizar():
    product_id = request.form.get('product_id')
    quantity = int(request.form.get('quantity', 1))
    
    cart = session.get('cart', {})
    
    if quantity > 0:
        produto = query_db('SELECT quantidade_estoque FROM produtos WHERE id = ?', [product_id], one=True)
        if produto and produto['quantidade_estoque'] >= quantity:
            cart[product_id]['quantity'] = quantity
        else:
            flash('Quantidade indisponível em estoque.', 'danger')
    else:
        if product_id in cart:
            del cart[product_id]
    
    session['cart'] = cart
    return redirect(url_for('cart.index'))

@cart_bp.route('/remover/<product_id>')
def remover(product_id):
    cart = session.get('cart', {})
    if product_id in cart:
        del cart[product_id]
        session['cart'] = cart
        flash('Item removido do carrinho.', 'info')
    return redirect(url_for('cart.index'))

@cart_bp.route('/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    cart = session.get('cart', {})
    
    if not cart:
        flash('Seu carrinho está vazio.', 'warning')
        return redirect(url_for('shop.index'))
    
    if request.method == 'POST':
        endereco = request.form.get('endereco')
        metodo_pagamento = request.form.get('metodo_pagamento')
        observacoes = request.form.get('observacoes', '')
        
        total = 0
        for product_id, item in cart.items():
            produto = query_db('SELECT preco FROM produtos WHERE id = ?', [product_id], one=True)
            if produto:
                total += produto['preco'] * item['quantity']
        
        pedido_id = execute_db('''
            INSERT INTO pedidos (usuario_id, total, status, metodo_pagamento, endereco_entrega, observacoes)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (session['user_id'], total, 'pendente', metodo_pagamento, endereco, observacoes))
        
        for product_id, item in cart.items():
            produto = query_db('SELECT * FROM produtos WHERE id = ?', [product_id], one=True)
            if produto:
                subtotal = produto['preco'] * item['quantity']
                execute_db('''
                    INSERT INTO pedido_itens (pedido_id, produto_id, quantidade, preco_unitario, subtotal)
                    VALUES (?, ?, ?, ?, ?)
                ''', (pedido_id, product_id, item['quantity'], produto['preco'], subtotal))
                
                execute_db('''
                    UPDATE produtos 
                    SET quantidade_estoque = quantidade_estoque - ?, atualizado_em = CURRENT_TIMESTAMP
                    WHERE id = ?
                ''', (item['quantity'], product_id))
        
        session.pop('cart', None)
        flash('Pedido realizado com sucesso!', 'success')
        return redirect(url_for('auth.profile'))
    
    cart_items = []
    total = 0
    
    for product_id, item in cart.items():
        produto = query_db('SELECT * FROM produtos WHERE id = ?', [product_id], one=True)
        if produto:
            subtotal = produto['preco'] * item['quantity']
            cart_items.append({
                'produto': produto,
                'quantity': item['quantity'],
                'subtotal': subtotal
            })
            total += subtotal
    
    return render_template('shop/checkout.html', cart_items=cart_items, total=total)
