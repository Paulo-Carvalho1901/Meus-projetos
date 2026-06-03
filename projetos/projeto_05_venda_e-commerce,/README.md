# ETL Products Pipeline

Pipeline ETL desenvolvido em Python para consumo de uma API REST, transformação dos dados, exportação para CSV, geração de logs, execução automatizada e containerização com Docker.

## Objetivo

Este projeto simula um cenário real de Engenharia de Dados e Automação, onde informações são extraídas de uma API externa, tratadas conforme regras de negócio e disponibilizadas em arquivos CSV para consumo posterior.

---

## Arquitetura

```text
API REST
    │
    ▼
Repository Layer
    │
    ▼
DTO Layer
    │
    ▼
Service Layer
    │
    ▼
Data Processing
    │
    ▼
CSV Export
    │
    ▼
Logs
```

### Responsabilidades

| Camada     | Responsabilidade                   |
| ---------- | ---------------------------------- |
| Repository | Comunicação com API externa        |
| DTO        | Estruturação dos dados             |
| Service    | Regras de negócio e transformações |
| Utils      | Logging e utilitários              |
| Main       | Orquestração da aplicação          |

---

## Tecnologias Utilizadas

- Python 3.12
- Pandas
- Requests
- Pytest
- Python-dotenv
- Logging
- Docker
- Docker Compose
- Schedule

---

## Estrutura do Projeto

```text
etl-project/

├── src/
│   ├── dto/
│   │   └── product_dto.py
│   │
│   ├── repository/
│   │   └── product_repository.py
│   │
│   ├── service/
│   │   └── product_service.py
│   │
│   ├── utils/
│   │   └── logger.py
│   │
│   └── main.py
│
├── tests/
│   └── test_service.py
│
├── logs/
├── output/
│
├── .env
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## Fluxo ETL

### Extract

Consome os dados da API Fake Store.

Exemplo:

```json
{
  "id": 1,
  "title": "Product",
  "price": 99.9,
  "category": "electronics"
}
```

---

### Transform

Durante o processamento são realizadas operações como:

- Remoção de duplicidades
- Limpeza de strings
- Ordenação de registros
- Validação de campos obrigatórios
- Criação de colunas derivadas
- Regras de negócio

Exemplo:

```python
df.drop_duplicates(inplace=True)
df = df[df["price"] > 0]
```

---

### Load

Os dados tratados são exportados para:

```text
output/products.csv
```

---

## Configuração

### Clone o projeto

```bash
git clone https://github.com/seu-usuario/etl-products.git

cd etl-products
```

---

### Criação do ambiente virtual

Linux/Mac

```bash
python -m venv venv

source venv/bin/activate
```

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

---

### Instalação das dependências

```bash
pip install -r requirements.txt
```

---

## Variáveis de Ambiente

Arquivo `.env`

```env
API_URL=https://fakestoreapi.com/products
CSV_PATH=output
LOG_PATH=logs
```

---

## Executando a Aplicação

```bash
python src/main.py
```

Saída esperada:

```text
CSV gerado com sucesso.
```

Arquivo criado:

```text
output/products.csv
```

---

## Logs

Todos os eventos da aplicação são registrados em:

```text
logs/application.log
```

Exemplo:

```text
2025-10-01 10:00:00 INFO CSV gerado com sucesso
```

---

## Testes Unitários

Executar:

```bash
pytest
```

Resultado esperado:

```text
==================
1 passed
==================
```

---

## Agendamento Automático

O projeto suporta execução recorrente utilizando Schedule.

Exemplo:

```python
schedule.every().day.at("08:00").do(main)
```

Executar:

```bash
python schedule_job.py
```

---

## Docker

### Build

```bash
docker build -t etl-products .
```

### Run

```bash
docker run etl-products
```

---

## Docker Compose

Executar:

```bash
docker compose up
```

Volumes:

```yaml
volumes:
  - ./output:/app/output
  - ./logs:/app/logs
```

---

## Boas Práticas Aplicadas

- Clean Code
- SOLID (parcial)
- Repository Pattern
- DTO Pattern
- Separation of Concerns
- Environment Variables
- Logging
- Unit Tests
- Dockerização

---

## Melhorias Futuras

### Versão 2

- Persistência em PostgreSQL
- SQLAlchemy
- Migrações com Alembic

### Versão 3

- Dashboard Power BI
- Dashboard Streamlit

### Versão 4

- Apache Airflow
- Orquestração de pipelines

### Versão 5

- Deploy AWS
- S3
- Lambda
- ECS

---

## Exemplo de Resultado

| id  | title     | price  | category    | rating |
| --- | --------- | ------ | ----------- | ------ |
| 1   | Product A | 120.50 | electronics | 4.8    |
| 2   | Product B | 95.00  | clothing    | 4.2    |

---

## Autor

Desenvolvido como projeto de estudos para prática de:

- Python
- ETL
- Integração com APIs REST
- Engenharia de Dados
- Automação de Processos
- Docker
- Testes Automatizados

---

## Licença

Este projeto está disponível para fins educacionais e de portfólio.
