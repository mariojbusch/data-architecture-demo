# 📁 Pasta infra — Infraestrutura e CI/CD

A pasta `infra` contém os arquivos responsáveis pela infraestrutura e automação do deploy do pipeline ETL. Atualmente, ela inclui:

- `cloudbuild.yaml` — pipeline CI/CD executado no Cloud Build
- `terraform/` — diretório reservado para provisionamento da infraestrutura (não documentado ainda)

Este diretório é essencial para garantir que o ETL seja construído, empacotado e implantado automaticamente na Google Cloud Platform.

---

# 📄 Arquivo: cloudbuild.yaml

O arquivo `cloudbuild.yaml` define o pipeline de CI/CD executado pelo **Google Cloud Build**. Ele automatiza três etapas fundamentais:

1. **Build da imagem Docker**
2. **Push da imagem para o Artifact Registry**
3. **Deploy do Cloud Run Job**

---

## 🔍 Etapas detalhadas

### 1. Build da imagem Docker
```yaml
- name: 'gcr.io/cloud-builders/docker'
  args: ['build', '-t', '$_REGION-docker.pkg.dev/$PROJECT_ID/data-architecture-demo/data-etl:latest', '.']
```
- Constrói a imagem Docker usando o `Dockerfile` na raiz do projeto.
- A imagem recebe a tag `latest`.
- O repositório é definido via substituição `_REGION`.

### 2. Push da imagem para o Artifact Registry
```yaml
- name: 'gcr.io/cloud-builders/docker'
  args: ['push', '$_REGION-docker.pkg.dev/$PROJECT_ID/data-architecture-demo/data-etl:latest']
```
- Envia a imagem construída para o Artifact Registry.
- Garante que o Cloud Run Job sempre use a versão mais recente.

### 3. Deploy do Cloud Run Job
```yaml
- name: 'gcr.io/cloud-builders/gcloud'
  args:
    [
      'run', 'jobs', 'deploy', 'data-etl-job',
      '--image', '$_REGION-docker.pkg.dev/$PROJECT_ID/data-architecture-demo/data-etl:latest',
      '--region', '$_REGION',
      '--max-retries', '0',
      '--command=python',
      '--args=src/main.py'
    ]
```
- Implanta o job `data-etl-job` no Cloud Run.
- Usa a imagem recém-enviada.
- Define o comando de execução: `python src/main.py`.
- Define `max-retries=0` para evitar reexecuções automáticas.

---

## 📦 Imagens geradas
```yaml
images:
  - '$_REGION-docker.pkg.dev/$PROJECT_ID/data-architecture-demo/data-etl:latest'
```
- Permite que o Cloud Build registre a imagem gerada.

---

## 🔧 Substituições
```yaml
substitutions:
  _REGION: 'southamerica-east1'
```
- Define a região padrão do deploy.
- Facilita reutilização do pipeline em outros ambientes.

---

## 🧪 Como testar o pipeline

### Execução manual
```bash
gcloud builds submit --config=infra/cloudbuild.yaml
```

### Logs
- Acompanhar no console do Cloud Build.
- Verificar se a imagem foi enviada ao Artifact Registry.
- Verificar se o Cloud Run Job foi atualizado.

---

## 🏗️ Como estender

### Para adicionar variáveis
```yaml
substitutions:
  _REGION: 'southamerica-east1'
  _ENV: 'production'
```

### Para adicionar testes antes do build
```yaml
- name: 'python'
  args: ['-m', 'pytest']
```

### Para adicionar validação de Terraform
```yaml
- name: 'hashicorp/terraform'
  args: ['validate']
```

---

## 🎯 Resumo
O arquivo `cloudbuild.yaml` automatiza todo o ciclo de vida do ETL:
- constrói a imagem
- publica no Artifact Registry
- implanta no Cloud Run Job

Ele é o coração do CI/CD do projeto.

