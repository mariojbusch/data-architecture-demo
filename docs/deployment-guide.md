# Guia de Deploy — Data Architecture Demo

Este documento descreve o processo completo de deploy do pipeline ETL em produção.

---

## 🚀 Visão Geral
O deploy é dividido em:
1. Provisionamento (Terraform)
2. Build da imagem (Cloud Build)
3. Deploy do Cloud Run Job
4. Agendamento via Cloud Scheduler

---

## 🧱 1. Provisionamento (Terraform)
```bash
cd infra/terraform
terraform init
terraform apply
```

---

## 🏗️ 2. Build da Imagem Docker (Cloud Build)
```bash
gcloud builds submit --tag gcr.io/$PROJECT_ID/data-etl
```

---

## 🏃 3. Deploy do Cloud Run Job
```bash
gcloud run jobs create data-etl-job \
  --image gcr.io/$PROJECT_ID/data-etl \
  --region southamerica-east1
```

---

## ⏰ 4. Agendamento com Cloud Scheduler
```bash
gcloud scheduler jobs create http data-etl-schedule \
  --schedule="0 3 * * *" \
  --uri="https://southamerica-east1-run.googleapis.com/apis/run.googleapis.com/v1/namespaces/$PROJECT_ID/jobs/data-etl-job:run" \
  --http-method=POST
```

---

## 🔐 Permissões Necessárias
- Storage Object Creator
- Storage Object Viewer
- BigQuery Data Editor
- Run Invoker

---

## 📊 Monitoramento
```bash
gcloud logging read "resource.type=cloud_run_job AND resource.labels.job_name=data-etl-job" --limit 50
```

---

## 🧪 Teste Final
```bash
gcloud run jobs execute data-etl-job --region southamerica-east1
```

---

## 📬 Contato
Mario Jorge de Abreu Busch — Rio de Janeiro, Brasil
GitHub: https://github.com/mariojbusch

