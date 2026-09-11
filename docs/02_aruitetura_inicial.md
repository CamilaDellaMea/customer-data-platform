# Arquitetura Inicial

## Fontes de dados

O projeto terá múltiplas fontes:

- PostgreSQL
- arquivos CSV
- APIs
- eventos em tempo real

## Fluxo inicial

Fontes
↓
Ingestão
↓
Armazenamento bruto
↓
Tratamento
↓
Camada analítica
↓
Power BI / Machine Learning / IA

## Estratégia de evolução

A arquitetura será construída por etapas.

Primeiro:

CSV / PostgreSQL
↓
Python
↓
PostgreSQL
↓
Power BI

Depois serão adicionados:

- Dagster
- dbt
- Kafka
- Parquet
- Machine Learning
- IA