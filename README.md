# 🔐 Login SSO com Google (OAuth2)

Este projeto foi desenvolvido com o objetivo de **aprender e entender o funcionamento do Single Sign-On (SSO)**, utilizando autenticação OAuth2 com contas do Google.

## 🧠 Sobre o Projeto

O **Single Sign-On (SSO)** é um método de autenticação que permite ao usuário acessar múltiplas aplicações com apenas um login. Isso melhora a experiência do usuário e aumenta a segurança, centralizando o processo de autenticação.

Neste projeto, implementei um sistema de login com Google em **Python**, usando a biblioteca **Authlib** com o framework **Flask**.

## ⚙️ Tecnologias e Ferramentas Utilizadas

- **Python**
- **Flask** – framework web leve e rápido
- **Authlib** – biblioteca para autenticação OAuth2
- **Google OAuth 2.0** – provedor de autenticação
- **HTML/CSS** – para a interface simples de login

## 🧪 Objetivo do Projeto

> Este projeto foi feito com fins educacionais, para que eu pudesse compreender como funciona a autenticação SSO, especialmente com a integração via Google OAuth2 em uma aplicação web.

## 🚀 Como Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/BryanR17/Login-SSO.git
   cd Login-SSO
   ```

2. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # no Windows: venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Crie um projeto no [Google Cloud Console](https://console.cloud.google.com/), ative a API OAuth2 e configure seu `client_id` e `client_secret`.

5. Adicione um arquivo `.env` com suas credenciais:
   ```
   CLIENT_ID=seu_client_id_aqui
   CLIENT_SECRET=seu_client_secret_aqui
   SECRET_KEY=uma_chave_secreta
   ```

6. Execute a aplicação:
   ```bash
   flask run
   ```

7. Acesse em seu navegador: [http://localhost:5000](http://localhost:5000)

## 📸 Demonstração
![image](https://github.com/user-attachments/assets/6fb3c67c-eaae-4d1d-bfb9-646cd739078b)

## 📚 Aprendizados

- Entendimento do fluxo OAuth2
- Integração com APIs externas (Google)
- Implementação segura de login com terceiros
- Conceitos fundamentais do SSO
