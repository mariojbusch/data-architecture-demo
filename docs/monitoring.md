# Monitoramento — Data Architecture Demo

Este documento descreve como monitorar o pipeline ETL executado em Cloud Run Jobs.

---

## 🎯 Objetivo
Garantir que o pipeline ETL seja observável, auditável, confiável e fácil de depurar.

---

## 🧩 Componentes de Observabilidade
### Cloud Logging
- Logs estruturados
- Logs do Cloud Run Job
- Logs do Scheduler

### Cloud Monitoring
- Latência
- Falhas
- Execuções concluídas

### Cloud Error Reporting
- Agrupa exceções não tratadas

---

## 📜 Logs do Cloud Run Job
```bash
gcloud logging read "resource.type=cloud_run_job AND resource.labels.job_name=data-etl-job" --limit 50
```

---

## 📊 Métricas
- `job/completed_count`
- `job/failed_count`
- `job/execution_duration`

---

## 🚨 Alertas
- Falha do job
- Latência alta
- Job não executado

---

## 🔐 Auditoria
```bash
gcloud logging read "logName:cloudaudit.googleapis.com" --limit 20
```

---

## 🧠 Boas Práticas
- Use logs estruturados
- Crie dashboards por camada
- Monitore tamanho dos arquivos no GCS
- Monitore custo do BigQuery

---

## 📬 Contato
Mario Jorge de Abreu Busch — Rio de Janeiro, Brasil
GitHub: https://github.com/mariojbusch

