# Sistema de E-commerce - João Layon

## Visão Geral
Sistema completo de e-commerce desenvolvido em Python Flask para venda de perfumes, roupas e acessórios. Inclui painel administrativo completo, controle de estoque, sistema de faturamento e interface responsiva.

## Desenvolvedor
**João Layon** - Todos os direitos reservados

## Stack Tecnológica
- **Backend**: Python 3.11 + Flask
- **Banco de Dados**: SQLite3 (sem ORM)
- **Frontend**: HTML5 + Tailwind CSS + Font Awesome
- **Segurança**: Werkzeug (hashing), Flask-WTF (CSRF)
- **Processamento de Imagens**: Pillow

## Estrutura do Projeto

```
ecommerce/
├── app/
│   ├── blueprints/          # Módulos Flask
│   │   ├── auth.py         # Autenticação e usuários
│   │   ├── shop.py         # Loja e catálogo
│   │   ├── cart.py         # Carrinho e checkout
│   │   └── admin.py        # Painel administrativo
│   ├── models/             # Modelos de dados
│   ├── templates/          # Templates Jinja2
│   │   ├── layouts/       # Layouts base
│   │   ├── auth/          # Páginas de autenticação
│   │   ├── shop/          # Páginas da loja
│   │   └── admin/         # Painel administrativo
│   ├── static/            # Arquivos estáticos
│   │   ├── css/          # Estilos
│   │   ├── js/           # JavaScript
│   │   └── uploads/      # Imagens (produtos, perfis)
│   └── utils/            # Funções auxiliares
│       ├── db.py        # Conexão SQLite
│       ├── helpers.py   # Helpers (upload, validação)
│       └── decorators.py # Decorators (auth, admin)
├── main.py              # Aplicação principal
├── init_db.py          # Script de inicialização do banco
├── config.py           # Configurações
└── README.md           # Documentação
```

## Funcionalidades Implementadas

### ✅ Autenticação e Usuários
- Cadastro de clientes com CPF, data de nascimento, telefone, email
- Login seguro com hash de senhas (Werkzeug)
- Upload de foto de perfil
- Alteração de senha
- Perfis: admin e cliente
- Recuperação de senha (admin pode resetar)

### ✅ Catálogo de Produtos
- Categorias personalizadas (Perfumes, Roupas, Acessórios)
- Produtos com: nome, descrição, preço, SKU, estoque, peso, dimensões, marca
- Até 5 imagens por produto
- Atributos opcionais (cor, tamanho) com variações
- Busca e filtros

### ✅ Carrinho e Checkout
- Carrinho persistente na sessão
- Atualização de quantidades
- Checkout com endereço de entrega
- Métodos de pagamento simulados
- Geração automática de pedidos

### ✅ Controle de Estoque
- Atualização automática ao confirmar pedidos
- Alertas de estoque baixo
- Gestão de quantidades por produto

### ✅ Painel Administrativo
- Dashboard com métricas
- Gestão de usuários (ativar/desativar, resetar senha)
- Gestão de categorias
- Gestão de produtos (criar, editar, ativar/desativar)
- Gestão de pedidos (visualizar, atualizar status)
- Sistema de faturamento com relatórios
- Exportação CSV
- Logs de atividades administrativas
- **Configurações da Loja**: Permite configurar nome, descrição, email, telefone e endereço

### ✅ Interface Responsiva
- Design com Tailwind CSS
- Compatível com mobile e desktop
- **Painel Administrativo Responsivo**: Layout híbrido com tabelas para desktop e cards otimizados para mobile
- Todas as páginas administrativas (categorias, produtos, usuários, pedidos) com paridade completa de dados entre desktop e mobile
- Navegação intuitiva
- Feedbacks visuais

## Credenciais Padrão

**Administrador:**
- Email: `admin@ecommerce.com`
- Senha: `admin123`

⚠️ **Importante**: Altere a senha padrão após o primeiro login!

## Como Executar

### 1. Inicializar o Banco de Dados
```bash
python init_db.py
```

### 2. Executar a Aplicação
```bash
python main.py
```

### 3. Acessar
- URL: `http://localhost:5000`
- Painel Admin: Login com credenciais de admin

## Banco de Dados

### Tabelas Principais
- `usuarios` - Usuários do sistema (clientes e admin)
- `categorias` - Categorias de produtos
- `produtos` - Produtos do catálogo
- `produto_imagens` - Imagens dos produtos (até 5 por produto)
- `produto_atributos` - Variações de produtos (cor, tamanho, etc.)
- `pedidos` - Pedidos realizados
- `pedido_itens` - Itens de cada pedido
- `logs_admin` - Logs de atividades administrativas
- `configuracoes_loja` - Configurações personalizáveis da loja (nome, contatos, etc.)

## Segurança Implementada
- ✅ Hashing de senhas com Werkzeug
- ✅ Proteção CSRF com Flask-WTF
- ✅ Validação de inputs (servidor e cliente)
- ✅ Upload seguro de imagens
- ✅ Sanitização de dados
- ✅ Controle de permissões (decorators)

## Variáveis de Ambiente
- `SESSION_SECRET` - Chave secreta para sessões (já configurada)

## Recursos para Implementação Futura
- Sistema de cupons e descontos
- Filtros avançados de busca
- Página de recomendações baseada em histórico
- Gateway de pagamento real (Stripe, PagSeguro)
- Notificações por email
- Sistema de avaliações de produtos
- Chat de suporte

## Manutenção

### Backup do Banco de Dados
```bash
cp ecommerce.db ecommerce.db.backup
```

### Limpar Banco de Dados
```bash
python init_db.py  # Remove e recria o banco
```

## Sistema de Configurações da Loja

O administrador pode personalizar as informações da loja através do painel administrativo:

### Configurações Disponíveis
- **Nome da Loja**: Aparece no cabeçalho e rodapé
- **Descrição**: Texto descritivo no rodapé
- **Email de Contato**: Exibido na seção de contato
- **Telefone**: Número de contato da loja
- **Endereço** (opcional): Localização física da loja

### Acesso
1. Fazer login como administrador
2. Acessar o Painel Administrativo
3. Clicar em "Configurações"
4. Editar as informações desejadas
5. Salvar

⚠️ **Nota**: O crédito "Desenvolvido por João Layon" é fixo e não pode ser alterado.

## Créditos
Sistema desenvolvido por **João Layon** com Flask, SQLite3 e Tailwind CSS.

---

**Última atualização**: 15 de Outubro de 2025
