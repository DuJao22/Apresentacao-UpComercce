# 🚀 Deploy no Render - Instruções

## ⚙️ Configuração no Render

Para fazer o deploy corretamente no Render, siga estas instruções:

### 1. Configurações do Build

No painel do Render, em **Settings** > **Build & Deploy**, configure:

**Build Command:**
```bash
pip install -r requirements.txt
```

**Start Command:**
```bash
bash start.sh
```

### 2. Variáveis de Ambiente (opcional)

Se você usar o Mercado Pago, adicione em **Environment**:
- `MERCADOPAGO_ACCESS_TOKEN` = seu token do Mercado Pago

### 3. Fazer Deploy

1. Faça commit e push das mudanças para o GitHub:
```bash
git add .
git commit -m "Adiciona script de inicialização para Render"
git push
```

2. O Render vai fazer o deploy automaticamente

## ✅ O que o script faz:

- Verifica se o banco de dados existe
- Se não existir, cria as tabelas e dados iniciais
- Inicia o servidor Gunicorn

## 👤 Usuário Administrador Padrão

Após o deploy, você pode fazer login com:
- **Email:** admin@ecommerce.com
- **Senha:** admin123

⚠️ **Importante:** Altere a senha após o primeiro login!

## 📝 Observações

- O banco de dados SQLite é criado automaticamente no primeiro deploy
- **ATENÇÃO:** No Render free tier, o sistema de arquivos é efêmero. Isso significa que o banco de dados será resetado sempre que o serviço reiniciar ou entrar em sleep mode.
- Para persistência de dados em produção, considere usar um banco de dados PostgreSQL (disponível no Render).

## 🔄 Alternativa: Usar PostgreSQL (Recomendado para Produção)

Se quiser persistência de dados, você deve:
1. Criar um banco PostgreSQL no Render
2. Modificar a aplicação para usar PostgreSQL ao invés de SQLite
3. Usar variáveis de ambiente para a string de conexão

## 🆘 Problemas Comuns

### O site está no ar mas não mostra produtos
- Isso é normal na primeira execução
- Faça login como admin e adicione produtos pelo painel administrativo

### Erro "no such table"
- Verifique se o Start Command está configurado corretamente: `bash start.sh`
- Verifique os logs do deploy para ver se o banco foi inicializado
