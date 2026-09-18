# Módulo de Login — API

## 1. Objetivo

Este projeto implementa um módulo de **login simplificado** para uma API desenvolvida com **FastAPI**. O usuário envia nome e senha, e a API verifica as credenciais e retorna seu perfil e suas permissões.

## 2. Estrutura

```text
app/
├── data/
│   └── usuarios_mock.py
│
├── models/
│   └── usuario.py
│
├── controllers/
│   └── auth_controller.py
│
└── routes/
    └── auth_routes.py

main.py
```

## 3. Funcionamento

O login é realizado através da rota:

```text
POST /api/auth/login
```

A requisição recebe o nome e a senha do usuário. O `AuthController` procura o usuário nos dados mockados e verifica a senha. Se as credenciais forem válidas, são retornados o nome, o perfil e as permissões do usuário.

Em caso de credenciais inválidas, a API retorna o status **401**.

## 4. Perfis e permissões

O sistema possui três tipos de usuário:

* **Visitante:** pode favoritar.
* **Contribuidor:** pode favoritar e publicar.
* **Moderador:** pode favoritar, publicar e moderar.

As permissões são definidas através de **herança e sobrescrita de métodos**, evitando concentrar todas as regras em condicionais no Controller.

## 5. Responsabilidade dos arquivos

* **`usuarios_mock.py`**: contém os usuários utilizados para testes.
* **`usuario.py`**: define a classe `Usuario` e seus perfis derivados.
* **`auth_controller.py`**: contém a lógica de autenticação.
* **`auth_routes.py`**: define a rota de login e as respostas HTTP.
* **`main.py`**: registra as rotas na aplicação FastAPI.

## 6. Conceitos utilizados

* Programação Orientada a Objetos (POO);
* Encapsulamento;
* Herança;
* Sobrescrita de métodos;
* Separação de responsabilidades;
* Arquitetura em camadas/MVC;
* FastAPI e rotas HTTP;
* Status HTTP `401`.

## 7. Fluxo

```text
Usuário
   ↓
POST /api/auth/login
   ↓
Auth Route
   ↓
Auth Controller
   ↓
Usuario
   ↓
Verificação da senha
   ↓
Perfil e permissões
   ↓
Resposta da API
```

## 8. Execução

Com as dependências instaladas, executar:

```bash
uvicorn main:app --reload
```

A API pode ser testada através da documentação automática do FastAPI em `/docs`.
