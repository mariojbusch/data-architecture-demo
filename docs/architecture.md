# Arquitetura — Data Architecture Demo

Este documento descreve a arquitetura completa do projeto **Data Architecture Demo**, incluindo fluxo de dados, componentes GCP, camadas do Data Lake, execução do ETL, CI/CD, monitoramento e governança.

---

## 🧩 Visão Geral
A arquitetura implementa um pipeline ETL moderno, escalável e totalmente serverless utilizando:
- **Cloud Run Jobs** para execução do ETL
- **Cloud Scheduler** para agendamento
- **Cloud Storage** como Data Lake
- **BigQuery** como Data Warehouse
- **Cloud Build** para CI/CD
- **Terraform** para provisionamento
- **IAM** para segurança e governança

O fluxo segue o padrão **Medallion Architecture**:
```
Raw → Staged → Curated
```

---

## 🔄 Fluxo de Dados (ETL)

### 1. Ingestion
- Implementado em `src/ingestion/ingest_api.py`
- Coleta dados de uma API externa
- Salva arquivo temporário em `/tmp/api_data_<timestamp>.json`

### 2. Transform
- Implementado em `src/transformation/transform.py`
- Normaliza JSON
- Remove campos desnecessários
- Prepara dados para carga

### 3. Load
- Implementado em `src/load/load.py`
- Envia arquivo transformado para o bucket RAW
- Caminho final: `raw/api_data_<timestamp>.json`

### 4. Staged e Curated
- Pipelines secundários movem dados para `staged` e `curated`
- BigQuery consome dados da camada curated

---

## 🏗️ Componentes da Arquitetura

### Cloud Run Jobs
- Executa o ETL de forma serverless
- Usa Service Account com permissões de Storage
- Escala automaticamente
- Orquestra `main.py`, que chama ingestão → transformação → carga

### Cloud Scheduler
- Dispara o job diariamente às 03:00
- Autenticação via OAuth

### Cloud Storage (Data Lake)

| Camada | Bucket | Função |
|--------|---------|--------|
| Raw | `data-architecture-demo-raw` | Dados brutos |
| Staged | `data-architecture-demo-staged` | Dados limpos |
| Curated | `data-architecture-demo-curated` | Dados prontos para análise |

### BigQuery
- Dataset analítico
- Tabelas particionadas por data

### Cloud Build
- Constrói imagem Docker
- Faz deploy automático no Cloud Run Jobs
- Pipeline definido em `infra/cloudbuild.yaml`

### Terraform
- Provisiona buckets, dataset, service accounts e permissões

---

## 📐 Diagrama da Arquitetura
O diagrama visual completo está disponível em:
```
docs/architecture-diagram.png
```

Diagrama Mermaid:
```mermaid
flowchart TD
    API[API Externa] --> ING[Ingestion]
    ING --> TR[Transform]
    TR --> LOAD[Load]

    LOAD --> RAW[Bucket RAW]
    RAW --> STAGED[Bucket STAGED]
    STAGED --> CURATED[Bucket CURATED]
    CURATED --> BQ[BigQuery Dataset]

    SCHED[Cloud Scheduler] --> CRJ[Cloud Run Job]
    CRJ --> ING

    GITHUB[GitHub Repo] --> CB[Cloud Build]
    CB --> CRJ

    LOG[Cloud Logging] --> MON[Cloud Monitoring]
```

---

## 🔐 Segurança e Governança
- Versionamento de objetos habilitado
- Soft delete com retenção de 7 dias
- IAM granular via Service Accounts
- Auditoria via Cloud Audit Logs

---

## 📊 Observabilidade
### Cloud Logging
- Logs estruturados
- Logs do Cloud Run Job
- Logs do Cloud Scheduler

### Cloud Monitoring
- Latência
- Execuções bem-sucedidas
- Falhas

### Cloud Error Reporting
- Agrupa exceções não tratadas

---

## 🚀 Próximos Passos
- Pipeline de carga para BigQuery
- Dashboard analítico no Looker Studio
- Alertas automáticos no Monitoring
- Versionamento de tabelas curated

---

## 📬 Contato
Mario Busch (mariojorgebusch@icloud.com)
Rio de Janeiro, Brasil
GitHub: https://github.com/mariojbusch

