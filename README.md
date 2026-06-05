# Cloud Monte Carlo Distribuído

Aplicação acadêmica para demonstrar processamento paralelo, processamento distribuído e computação em nuvem usando Python, FastAPI, Streamlit, Celery, Redis, Docker e Docker Compose.

## Como executar localmente

```bash
docker compose up --build
```

Acesse:
- Front-end: http://localhost:8501
- API: http://localhost:8000/docs

## Como testar a diferença de workers

Na interface, execute o mesmo número de iterações com 1 worker e depois com 4 workers. Registre o tempo exibido na tela.

## Estrutura

- `frontend/`: interface Streamlit.
- `backend/`: API FastAPI e tarefas Celery.
- `docker-compose.yml`: Redis, API, front-end e quatro workers isolados.
- `scripts/benchmark_local.py`: script para coletar métricas locais com multiprocessing.
