# 📁 Pasta src/load — Módulo de Carga (Load)

A pasta `src/load` contém o módulo responsável pela **carga dos dados transformados** no Google Cloud Storage (GCS). Esta é a última etapa do pipeline ETL.

O arquivo principal é `load.py`, que implementa a função `upload_to_gcs()`.

---

## 📄 Arquivo: load.py

Este arquivo contém a função responsável por enviar arquivos locais para um bucket do Google Cloud Storage.

### 🎯 Objetivo
Realizar o upload do arquivo transformado para o Data Lake, seguindo a organização definida pela arquitetura Medallion.

---

## 🔍 Fluxo detalhado da função `upload_to_gcs()`

### 1. Log inicial
```python
print(f"Uploading {local_path} to gs://{bucket_name}/{destination_path}")
```
Indica qual arquivo está sendo enviado e para onde.

### 2. Criação do cliente GCS
```python
client = storage.Client()
```
- Usa credenciais padrão do ambiente (ADC).
- Funciona automaticamente no Cloud Run.

### 3. Seleção do bucket
```python
bucket = client.bucket(bucket_name)
```
Carrega o bucket onde o arquivo será armazenado.

### 4. Criação do blob (objeto no GCS)
```python
blob = bucket.blob(destination_path)
```
Define o caminho final dentro do bucket.

### 5. Upload do arquivo
```python
blob.upload_from_filename(local_path)
```
- Envia o arquivo local para o GCS.
- Mantém o nome definido em `destination_path`.

### 6. Log final
```python
print("Upload completed.")
```
Confirma que o upload foi concluído.

---

## 📦 Estrutura atual da pasta
```
src/load/
└── load.py
```

---

## 🧪 Como testar

### Execução isolada
```bash
python -c "from load.load import upload_to_gcs; upload_to_gcs('/tmp/test.json', 'meu-bucket', 'raw/test.json')"
```

### Testes unitários
- Criar testes em `tests/test_load.py`.
- Mockar `storage.Client()` para evitar uploads reais.

---

## 🏗️ Como estender

### Para mudar o bucket
Alterar o parâmetro `bucket_name` no `main.py`.

### Para adicionar compressão
Antes do upload:
```python
import gzip
```

### Para adicionar metadados
```python
blob.metadata = {"source": "etl", "stage": "raw"}
blob.patch()
```

### Para enviar para outras camadas (staged/curated)
Alterar o prefixo:
```python
f"staged/{destination}"
```

---

## 🎯 Resumo
O módulo `load` é responsável por:
- conectar ao Google Cloud Storage
- criar objetos dentro do bucket
- enviar arquivos transformados para o Data Lake

Ele é a última etapa do pipeline ETL e garante que os dados fiquem disponíveis para processamento posterior.

