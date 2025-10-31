# Projeto de estudo — async_python

Este repositório contém um projeto de estudo em Python que usa FastAPI e Uvicorn para demonstrar padrões assíncronos e organização de projeto backend.

## Descrição

Objetivo: servir como base de estudos para aplicações assíncronas em Python (FastAPI + Uvicorn). O projeto inclui código de exemplo organizado em `src/` com rotas, controllers, modelos e repositórios.

## Pré-requisitos

- Python 3.8+ (recomendado 3.10+)
- pip
- Recomendo usar um ambiente virtual (venv)

## Instalação (rápido)

Abra o PowerShell e execute:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install fastapi uvicorn
```

Observação: não existe um `requirements.txt` no repositório atualmente; se quiser gerar um, após instalar dependências use `pip freeze > requirements.txt`.

## Como executar

O projeto já contém um arquivo `run.py` na raiz que executa Uvicorn apontando para a aplicação FastAPI.

Para iniciar a aplicação (modo desenvolvimento):

```powershell
python run.py
```

Ou execute Uvicorn diretamente:

```powershell
uvicorn src.main.server.server:app --reload --host 0.0.0.0 --port 8000
```

Depois de iniciado, a documentação interativa estará disponível em:

- http://127.0.0.1:8000/docs  (Swagger UI)
- http://127.0.0.1:8000/redoc (ReDoc)

## Estrutura principal do projeto

Resumo das pastas mais importantes:

- `src/` — código-fonte da aplicação
	- `main/server/server.py` — instância FastAPI (ponto de entrada usado por Uvicorn)
	- `main/routes/` — definições de rotas (ex.: `pessoas_routes.py`)
	- `controllers/`, `models/`, `repositories/` — camadas da aplicação
- `exe*` — scripts/execuções de exemplo (alguns run.py dentro dessas pastas)

Explore a pasta `src` para ver exemplos de endpoints e organização do código.

## Endpoints

Os endpoints estão definidos em `src/main/routes/`. Um roteiro rápido:

- Para ver os endpoints disponíveis, abra `http://127.0.0.1:8000/docs` enquanto o servidor estiver rodando.

## Contribuição / próximos passos

- Adicionar um `requirements.txt` com todas as dependências.
- Documentar variáveis de ambiente e configuração de banco (se aplicar).
- Escrever testes automatizados (pytest) e um pequeno script de CI local.

Se quiser, eu posso:

- gerar um `requirements.txt` a partir do ambiente local;
- adicionar instruções de Docker;
- adicionar testes simples com `pytest`.

## Licença

Coloque aqui a licença desejada (por exemplo MIT) — atualmente não há arquivo de licença no repositório.

 