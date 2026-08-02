# ADRs — Architecture Decision Records

Este documento registra as principais decisões arquiteturais tomadas durante o desenvolvimento do projeto **Data Architecture Demo**, seguindo o padrão ADR (Architecture Decision Record). Cada decisão inclui contexto, alternativas consideradas, justificativa e impacto.

---

## ADR 001 — Uso da Google Cloud Platform

### Contexto
O projeto precisava de uma arquitetura moderna, escalável, de baixo custo e fácil de demonstrar.

### Decisão
Utilizar a **Google Cloud Platform (GCP)** como provedor principal.

### Justificativa
- Serviços serverless maduros (Cloud Run, Cloud Functions)
- BigQuery como data warehouse líder do mercado
- Cloud Storage com custo baixo e alta durabilidade
- Integração nativa com Terraform e CI/CD

### Consequências
- Dependência da GCP
- Custos previsíveis e baixos

---

## ADR 002 — Cloud Run Jobs para execução do ETL

### Contexto
Era necessário executar pipelines ETL sem gerenciar servidores.

### Decisão
Utilizar **Cloud Run Jobs** para execução do ETL.

### Justificativa
- Execução totalmente serverless
- Escalabilidade automática
- Suporte nativo a containers
- Integração com Cloud Scheduler

### Consequências
- Pipeline mais simples
- Deploy padronizado via Docker

---

## ADR 003 — Cloud Scheduler para agendamento

### Contexto
O ETL precisava rodar diariamente sem intervenção manual.

### Decisão
Utilizar **Cloud Scheduler** para disparar o Cloud Run Job.

### Justificativa
- Cron nativo
- Autenticação via OAuth
- Baixo custo

### Consequências
- Dependência de um serviço adicional
- Monitoramento via Logging

---

## ADR 004 — Arquitetura Medallion (Raw → Staged → Curated)

### Contexto
Era necessário organizar os dados em camadas para garantir governança e rastreabilidade.

### Decisão
Implementar a arquitetura **Medallion**.

### Justificativa
- Padrão amplamente utilizado
- Facilita auditoria e versionamento
- Permite evolução incremental

### Consequências
- Três buckets distintos
- Pipelines secundários para staged e curated

---

## ADR 005 — BigQuery como Data Warehouse

### Contexto
Precisávamos de um ambiente analítico escalável e com SQL padrão.

### Decisão
Utilizar **BigQuery**.

### Justificativa
- Performance excepcional
- Custos baixos para datasets pequenos
- Integração com Looker Studio

### Consequências
- Custos por consulta
- Necessidade de boas práticas de particionamento

---

## ADR 006 — Terraform para provisionamento

### Contexto
A infraestrutura precisava ser reprodutível e versionada.

### Decisão
Utilizar **Terraform**.

### Justificativa
- IaC padrão de mercado
- Reprodutibilidade total
- Controle via Git

### Consequências
- Curva de aprendizado
- Necessidade de manter estado

---

## ADR 007 — Cloud Build para CI/CD

### Contexto
Era necessário automatizar o build da imagem Docker.

### Decisão
Utilizar **Cloud Build**.

### Justificativa
- Integração nativa com GCP
- Baixo custo
- Pipeline simples

### Consequências
- Dependência de YAML
- Logs no Cloud Build

---

## ADR 008 — Python como linguagem principal

### Contexto
O ETL precisava ser simples, legível e rápido de desenvolver.

### Decisão
Utilizar **Python**.

### Justificativa
- Ecossistema rico
- Bibliotecas nativas para ETL
- Fácil integração com GCP

### Consequências
- Necessidade de gerenciar dependências
- Uso de virtualenv

---

## ADR 009 — Estrutura modular do ETL

### Contexto
O código precisava ser organizado e fácil de manter.

### Decisão
Separar o ETL em módulos:
- ingestion
- transform
- load
- main

### Justificativa
- Clareza
- Testabilidade
- Reutilização

### Consequências
- Mais arquivos
- Estrutura mais robusta

---

## ADR 010 — Documentação visual completa

### Contexto
O projeto precisava ser demonstrável e fácil de explicar.

### Decisão
Criar documentação visual e textual completa.

### Justificativa
- Facilita apresentações
- Ajuda em entrevistas e portfólio
- Torna o repositório profissional

### Consequências
- Manutenção da documentação

---

## 📬 Contato

Mario Jorge de Abreu Busch — Rio de Janeiro, Brasil
GitHub: https://github.com/mariojbusch

