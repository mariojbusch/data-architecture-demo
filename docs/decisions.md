# ADRs — Architecture Decision Records

Este documento registra as principais decisões arquiteturais tomadas durante o desenvolvimento do projeto **Data Architecture Demo**, seguindo o padrão ADR.

---

## ADR 001 — Uso da Google Cloud Platform
**Decisão:** Utilizar GCP como provedor principal.
**Justificativa:** Serviços serverless maduros, BigQuery, Cloud Storage.

---

## ADR 002 — Cloud Run Jobs para execução do ETL
**Decisão:** Executar o ETL via Cloud Run Jobs.
**Justificativa:** Serverless, escalável, simples.

---

## ADR 003 — Cloud Scheduler para agendamento
**Decisão:** Disparar o ETL diariamente via Cloud Scheduler.

---

## ADR 004 — Arquitetura Medallion
**Decisão:** Organizar dados em Raw → Staged → Curated.

---

## ADR 005 — BigQuery como Data Warehouse
**Decisão:** Usar BigQuery para análises.

---

## ADR 006 — Terraform para provisionamento
**Decisão:** Provisionar infraestrutura via IaC.

---

## ADR 007 — Cloud Build para CI/CD
**Decisão:** Automatizar build e deploy via Cloud Build.

---

## ADR 008 — Python como linguagem principal
**Decisão:** Implementar ETL em Python.

---

## ADR 009 — Estrutura modular do ETL
**Decisão:** Separar ingestão, transformação, carga e orquestração.

---

## ADR 010 — Documentação visual completa
**Decisão:** Criar documentação textual + diagrama.

---

## 📬 Contato
Mario Jorge de Abreu Busch — Rio de Janeiro, Brasil
GitHub: https://github.com/mariojbusch

