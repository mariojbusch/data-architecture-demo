# Guia de Deploy — Data Architecture Demo

Este documento descreve o processo completo de deploy do pipeline ETL em produção utilizando Cloud Build, Cloud Run Jobs, Cloud Scheduler e Terraform.

---

## 🚀 Visão Geral

O deploy da arquitetura é dividido em quatro etapas principais:

1. Provisionamento da infraestrutura (Terraform)
2. Build da imagem Docker (Cloud Build)
3. Deploy do Cloud Run Job
4. Agendamento via Cloud Scheduler

Este guia assume que você já possui:
- Projeto GCP configurado
- Billing habilitado
- APIs necessárias ativadas
- gcloud CLI instalado

---

## 🧱 1. Provisionamento da Infraestrutura (Terraform)

A infraestrutura inclui:
- Buckets RAW, STAGED e CURATED
- Dataset BigQuery
- Service Account do Cloud Run
- Permissões IAM

### Passos

```bash
cd infra/terraform
terraform init
terraform apply
```

Após o apply, os recursos estarão disponíveis no projeto.

---

## 🏗️ 2. Build da Imagem Docker (Cloud Build)

O Cloud Build constrói a imagem e envia para o Container Registry.

### Comando

```bash
gcloud builds submit --tag gcr.io/$PROJECT_ID/data-etl
```

Isso irá:
- Ler o Dockerfile
- Construir a imagem
- Enviar para `gcr.io/$PROJECT_ID/data-etl`

---

## 🏃 3. Deploy do Cloud Run Job

O Cloud Run Job executa o pipeline ETL de forma serverless.

### Criar o Job

```bash
gcloud run jobs create etl-job \
  --image gcr.io/$PROJECT_ID/data-etl \
  --region southamerica-east1 \
  --service-account 26366089084-compute@developer.gserviceaccount.com
```

### Executar manualmente

```bash
gcloud run jobs execute etl-job --region southamerica-east1
```

---

## ⏰ 4. Agendamento com Cloud Scheduler

O Cloud Scheduler dispara o job diariamente às 03:00.

### Criar o cron

```bash
gcloud scheduler jobs create http etl-job-schedule \
  --schedule="0 3 * * *" \
  --uri="https://southamerica-east1-run.googleapis.com/apis/run.googleapis.com/v1/namespaces/$PROJECT_ID/jobs/etl-job:run" \
  --http-method=POST \
  --oauth-service-account-email=26366089084-compute@developer.gserviceaccount.com
```

### Verificar execução

```bash
gcloud scheduler jobs run etl-job-schedule
```

---

## 🔐 Permissões Necessárias

### Service Account do Cloud Run

Deve possuir:
- `roles/storage.objectCreator`
- `roles/storage.objectViewer`
- `roles/bigquery.dataEditor`
- `roles/run.invoker`

### Cloud Scheduler

Deve possuir:
- `roles/cloudscheduler.jobRunner`

---

## 📊 Monitoramento

### Logs

```bash
gcloud logging read "resource.type=cloud_run_job AND resource.labels.job_name=etl-job" --limit 50
```

### Métricas

Disponíveis no Cloud Monitoring:
- Latência
- Execuções bem-sucedidas
- Falhas

---

## 🧪 Teste Final

Após o deploy completo:

```bash
gcloud run jobs execute etl-job --region southamerica-east1
```

Verifique:
- Arquivo gerado no bucket RAW
- Logs no Cloud Logging
- Métricas no Monitoring

---

## 📬 Contato

Mario Jorge de Abreu Busch (mariojorgebusch@icloud.com)

Rio de Janeiro, Brasil

GitHub: https://github.com/mariojbusch