# Monitoramento — Data Architecture Demo

Este documento descreve como monitorar o pipeline ETL executado em Cloud Run Jobs, incluindo logs, métricas, alertas e boas práticas de observabilidade na Google Cloud Platform.

---

## 🎯 Objetivo

Garantir que o pipeline ETL seja:
- Observável
- Auditável
- Fácil de depurar
- Confiável em produção

---

## 🧩 Componentes de Observabilidade

A arquitetura utiliza três serviços principais:

### **1. Cloud Logging**
Coleta logs estruturados do Cloud Run Job, Cloud Scheduler e Cloud Build.

### **2. Cloud Monitoring**
Exibe métricas de execução, latência, falhas e consumo de recursos.

### **3. Cloud Error Reporting**
Agrupa exceções e erros não tratados.

---

## 📜 Logs do Cloud Run Job

Para visualizar logs do job:

```bash
gcloud logging read "resource.type=cloud_run_job AND resource.labels.job_name=etl-job" --limit 50
```

Ou via Console:
- Cloud Run → Jobs → etl-job → Logs

### Estrutura recomendada de logs

Use logs estruturados em JSON:

```python
import json
import logging

logging.basicConfig(level=logging.INFO)

logging.info(json.dumps({
    "event": "ingestion_started",
    "timestamp": "2026-08-02T15:00:00Z"
}))
```

Benefícios:
- Fácil de filtrar
- Fácil de agregar
- Integra com dashboards

---

## 📊 Métricas no Cloud Monitoring

O Cloud Run Jobs expõe métricas automáticas:

### Métricas principais
- **run.googleapis.com/job/completed_count** — execuções concluídas
- **run.googleapis.com/job/failed_count** — execuções com erro
- **run.googleapis.com/job/execution_duration** — tempo total do job
- **run.googleapis.com/job/retry_count** — número de retries

### Criar dashboard
1. Acesse Cloud Monitoring
2. Dashboards → Create Dashboard
3. Adicione gráficos:
   - Execuções por dia
   - Latência média
   - Falhas por job

---

## 🚨 Alertas

Configure alertas para:
- Falha do job
- Latência acima do esperado
- Falta de execução (job não rodou)

### Exemplo de política de alerta

1. Monitoring → Alerting → Create Policy
2. Condição:
   - Métrica: `run.googleapis.com/job/failed_count`
   - Threshold: > 0
3. Notificação:
   - Email
   - Slack (via webhook)
   - PagerDuty

---

## 🧪 Testando o Monitoramento

### Testar logs
```bash
gcloud run jobs execute etl-job --region southamerica-east1
```
Verifique:
- Logs de ingestão
- Logs de transformação
- Logs de carga

### Testar alertas
- Force uma falha proposital
- Verifique se o alerta dispara

---

## 🔐 Auditoria

O Cloud Audit Logs registra:
- Execuções do Cloud Run Job
- Disparos do Cloud Scheduler
- Builds do Cloud Build
- Alterações de IAM

Ver logs de auditoria:
```bash
gcloud logging read "logName:cloudaudit.googleapis.com" --limit 20
```

---

## 🧠 Boas Práticas

- Use logs estruturados
- Crie dashboards por camada (raw, staged, curated)
- Configure alertas para falhas e ausência de execução
- Monitore tamanho dos arquivos no GCS
- Monitore custo do BigQuery

---

## 📬 Contato

Mario Jorge de Abreu Busch (mariojorgebusch@icloud.com)

Rio de Janeiro, Brasil

GitHub: https://github.com/mariojbusch