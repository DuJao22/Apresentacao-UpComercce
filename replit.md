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
- **Pagamentos**: Mercado Pago SDK (Python)

## Estrutura do Projeto

```
ecommerce/
├── app/
│   ├── blueprints/          # Módulos Flask
│   │   ├── auth.py         # Autenticação e usuários
│   │   ├── shop.py         # Loja e catálogo
│   │   ├── cart.py         # Carrinho e checkout
│   │   ├── admin.py        # Painel administrativo
│   │   └── customer.py     # Área do cliente
│   ├── models/             # Modelos de dados
│   ├── templates/          # Templates Jinja2
│   │   ├── layouts/       # Layouts base
│   │   ├── auth/          # Páginas de autenticação
│   │   ├── shop/          # Páginas da loja
│   │   ├── admin/         # Painel administrativo
│   │   └── customer/      # Área do cliente
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
- **18 Produtos de Exemplo**: Catálogo pré-populado com 5 perfumes, 6 roupas e 7 acessórios
- **54 Imagens Profissionais**: 3 fotos de stock de alta qualidade para cada produto

### ✅ Carrinho e Checkout
- Carrinho persistente na sessão
- Atualização de quantidades
- Checkout com endereço de entrega
- **Integração com Mercado Pago**: Pagamentos online com cartão, PIX, boleto
- **Pagamento em Dinheiro**: Com confirmação manual pelo admin
- Geração automática de pedidos
- Webhooks para confirmação automática de pagamentos

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
- **Comissão Configurável**: Admin pode definir percentual de comissão (0% a 100%) nas configurações
- Exportação CSV
- Logs de atividades administrativas
- **Configurações da Loja**: Permite configurar nome, descrição, email, telefone, endereço e comissão
- **Configuração Mercado Pago**: Interface para adicionar credenciais (Access Token e Public Key)
- **Confirmação de Pagamentos em Dinheiro**: Botão para admin confirmar recebimento de pagamentos em dinheiro
- **Sistema de Notificações em Tempo Real**:
  - Badge de notificação com contagem de pedidos pendentes
  - Pop-ups visuais na tela para novos pedidos
  - Notificações push do navegador
  - Som de alerta para novos pedidos
  - Verificação automática a cada 10 segundos
- **Status Detalhados de Pedidos**:
  - ⏳ Pendente (Aguardando Confirmação)
  - ✅ Confirmado (Pedido Aceito)
  - 📦 Em Separação (Preparando Pedido)
  - ✨ Pronto para Retirada (para retirada no local)
  - 🚚 Saiu para Entrega (para entrega em casa)
  - 🎉 Entregue/Retirado
  - ❌ Cancelado
- **Reset de Banco de Dados**: Opção para resetar produtos e categorias preservando histórico de pedidos
  - Produtos usados em pedidos: desativados (dados preservados)
  - Produtos nunca comprados: deletados permanentemente
  - Categorias: desativadas

### ✅ Área do Cliente (Nova!)
- **Dashboard Profissional**: Estatísticas de compras, pedidos recentes, acesso rápido
- **Gerenciamento de Pedidos**: Visualização completa com filtros por status
- **Detalhes do Pedido**: Timeline visual de rastreamento adaptável ao tipo de entrega
  - **Entrega em Casa**: Pedido → Aprovado → Enviado → Entregue
  - **Retirada no Local**: Pedido → Aprovado → Pronto → Retirado
- **Cancelamento de Pedidos**: Cliente pode cancelar pedidos pendentes (estoque é reajustado)
- **Configurações da Conta**: Atualização de dados pessoais e foto de perfil
- **Alteração de Senha**: Sistema seguro com validação
- **Design Premium**: Interface moderna e responsiva

### ✅ Interface Responsiva
- Design com Tailwind CSS
- Compatível com mobile e desktop
- **Painel Administrativo Responsivo**: Layout híbrido com tabelas para desktop e cards otimizados para mobile
- **Área do Cliente Responsiva**: Dashboard e pedidos otimizados para todas as telas
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

### 2. Executar a Migração (se banco já existir)
```bash
python migrate_database.py
```

### 3. Executar a Aplicação
```bash
python main.py
```

### 4. Acessar
- URL: `http://localhost:5000`
- Painel Admin: Login com credenciais de admin
- Área do Cliente: Login com credenciais de cliente (após login, acesso via menu do usuário)

## 📦 Como Testar o Sistema de Retirada/Entrega

### Passo 1: Configure o Local de Retirada (Admin)
1. Faça login como admin (`admin@ecommerce.com` / `admin123`)
2. Vá em **Painel Admin** > **Configurações**
3. Preencha o campo **Local de Retirada** com endereço e horários
4. Salve as configurações

### Passo 2: Teste o Checkout (Cliente)
1. Faça login como cliente (ou crie uma conta)
2. Adicione produtos ao carrinho
3. Clique em **Finalizar Compra**
4. **Escolha o tipo de entrega**:
   - 🚚 **Entrega em Casa**: Preencha o endereço
   - 🏪 **Retirar no Local**: Veja o endereço de retirada
5. Complete o pedido

### Credenciais de Teste
- **Admin**: `admin@ecommerce.com` / `admin123`
- **Cliente**: `cliente@teste.com` / `senha123`

## Banco de Dados

### Tabelas Principais
- `usuarios` - Usuários do sistema (clientes e admin)
- `categorias` - Categorias de produtos
- `produtos` - Produtos do catálogo
- `produto_imagens` - Imagens dos produtos (até 5 por produto)
- `produto_atributos` - Variações de produtos (cor, tamanho, etc.)
- `pedidos` - Pedidos realizados (com campos Mercado Pago: mercadopago_payment_id, mercadopago_preference_id, confirmado_admin)
- `pedido_itens` - Itens de cada pedido
- `logs_admin` - Logs de atividades administrativas
- `configuracoes_loja` - Configurações personalizáveis da loja (nome, contatos, credenciais Mercado Pago, etc.)

## Segurança Implementada
- ✅ Hashing de senhas com Werkzeug
- ✅ Proteção CSRF com Flask-WTF
- ✅ Validação de inputs (servidor e cliente)
- ✅ Upload seguro de imagens
- ✅ Sanitização de dados
- ✅ Controle de permissões (decorators)

## Variáveis de Ambiente
- `SESSION_SECRET` - Chave secreta para sessões (já configurada)

## ✅ Sistema de Pagamentos (Novo!)

### Mercado Pago
O sistema está integrado com o Mercado Pago para processar pagamentos online:

#### Como Configurar
1. Faça login como admin (`admin@ecommerce.com` / `admin123`)
2. Vá em **Painel Admin** > **Configurações**
3. Role até a seção **Configuração Mercado Pago**
4. Obtenha suas credenciais em [Mercado Pago Developers](https://www.mercadopago.com/developers/panel)
5. Insira o **Access Token** e **Public Key**
6. **IMPORTANTE**: Configure também o **Webhook Secret** para segurança:
   - No painel do Mercado Pago, vá em **Webhooks** > **Configurar Notificações**
   - Adicione a URL do webhook: `https://seu-dominio.com/webhook/mercadopago`
   - Copie o Secret gerado automaticamente
   - Cole no campo **Webhook Secret** nas configurações
7. Salve as configurações

#### Funcionalidades
- ✅ **Checkout Pro**: Redirecionamento para Mercado Pago
- ✅ **Múltiplas Formas de Pagamento**: Cartão, PIX, boleto, saldo em conta
- ✅ **Webhooks Automáticos**: Confirmação automática de pagamentos
- ✅ **Validação de Assinatura**: Webhooks validados com HMAC-SHA256 para segurança
- ✅ **Rastreamento**: ID do pagamento armazenado no pedido
- ✅ **URLs de Retorno**: Redirecionamento após pagamento (sucesso/falha/pendente)

### Pagamento em Dinheiro
Para pagamentos em dinheiro na entrega:

1. **Cliente** seleciona "Dinheiro" no checkout
2. **Admin** recebe o pedido com status "Pendente"
3. **Admin** confirma o pagamento após receber o dinheiro
4. Sistema atualiza status para "Pago"

## Recursos para Implementação Futura
- Sistema de cupons e descontos
- Filtros avançados de busca
- Página de recomendações baseada em histórico
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

## Manutenção e Migração do Banco de Dados

### Executar Migração (para bancos existentes)
Se você já tem um banco de dados existente e precisa adicionar as novas colunas:
```bash
python migrate_database.py
```

Este script adiciona as colunas necessárias:
- `local_retirada` e `email_notificacao` em `configuracoes_loja`
- `tipo_entrega` em `pedidos`

### Criar Novo Banco de Dados
Para criar um novo banco de dados do zero com todas as tabelas e configurações:
```bash
python init_db.py
```

⚠️ **Atenção**: Este comando apaga o banco existente e cria um novo!

## Favicon e Interface

✅ **Favicon Personalizado**: Todas as páginas exibem o favicon SVG da loja (ícone de sacola de compras em roxo/indigo)
✅ **Interface Responsiva**: Design otimizado para desktop e mobile com Tailwind CSS

## Créditos
Sistema desenvolvido por **João Layon** com Flask, SQLite3 e Tailwind CSS.

---

**Última atualização**: 18 de Outubro de 2025

## Alterações Recentes (18/10/2025)

### ✅ Correções Implementadas
1. **Bug de Status Corrigido**: Resolvida inconsistência na exibição de status de pedidos na área do cliente
   - Timelines agora mostram corretamente as bolinhas coloridas para todos os status
   - Status "Pronto para Retirada" e "Saiu para Entrega" agora funcionam perfeitamente
   
2. **Catálogo Completo**: Sistema agora inclui 18 produtos de exemplo profissionais
   - 5 Perfumes premium (Essência Floral, Amadeirado Intenso, Lavanda Suave, Oriental Misterioso, Citrus Fresh)
   - 6 Roupas (Vestido, Camisa Social, Calça Jeans, Blazer, Saia, Camiseta)
   - 7 Acessórios (Bolsa, Relógio, Óculos, Carteira, Cinto, Colar, Pulseira)
   - Cada produto com 3 fotos profissionais de stock = 54 imagens no total

3. **Funcionalidade de Reset**: Nova opção no painel administrativo
   - Permite resetar todo o catálogo de produtos e categorias
   - Inteligente: preserva produtos usados em pedidos (apenas desativa)
   - Seguro: histórico de pedidos 100% preservado
   - Transação atômica com rollback em caso de erro
