# 📁 Pasta src/ingestion — Módulo de Ingestão

A pasta `src/ingestion` contém o módulo responsável pela **ingestão de dados** no pipeline ETL. Aqui ficam todas as funções que coletam dados de fontes externas, como APIs, arquivos ou sistemas internos.

Atualmente, o módulo implementa ingestão via API pública.

---

## 📄 Arquivo: ingest_api.py

Este arquivo contém a função principal de ingestão do pipeline ETL: `run_ingestion()`.

### 🎯 Objetivo
Coletar dados de uma API externa, validar a resposta, salvar temporariamente no container e retornar o caminho do arquivo para as próximas etapas do ETL.

---

## 🔍 Fluxo detalhado da função `run_ingestion()`

### 1. Log inicial
```python
print("Starting ingestion...")
```
Indica o início da etapa de ingestão.

### 2. Definição da API
```python
url = "https://jsonplaceholder.typicode.com/posts"
```
- API pública usada como exemplo.
- Pode ser substituída por qualquer endpoint real.

### 3. Requisição HTTP
```python
response = requests.get(url, timeout=30)
```
- Timeout de 30 segundos.
- Se a API não responder, a execução falha.

### 4. Validação da resposta
```python
if response.status_code != 200:
    raise Exception(f"API returned status {response.status_code}")
```
Garante que somente respostas bem-sucedidas são processadas.

### 5. Conversão para JSON
```python
data = response.json()
```
Transforma o payload da API em uma lista/dicionário Python.

### 6. Log da quantidade de registros
```python
print(f"Fetched {len(data)} records from API")
```
Útil para monitoramento e auditoria.

### 7. Geração do nome do arquivo
```python
timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
output_path = f"/tmp/api_data_{timestamp}.json"
```
- Gera um nome único baseado no timestamp.
- Salva no diretório `/tmp`, padrão para containers.

### 8. Salvando o arquivo
```python
with open(output_path, "w") as f:
    json.dump(data, f)
```
Cria o arquivo bruto que será transformado na próxima etapa.

### 9. Retorno
```python
return output_path
```
Retorna o caminho do arquivo para o módulo de transformação.

---

## 📦 Estrutura atual da pasta
```
src/ingestion/
└── ingest_api.py
```

---

## 🧪 Como testar

### Execução isolada
```bash
python -c "from ingestion.ingest_api import run_ingestion; print(run_ingestion())"
```

### Testes unitários
- Criar testes em `tests/test_ingestion.py`.
- Mockar `requests.get` para evitar chamadas reais.

---

## 🏗️ Como estender

### Para trocar a API
Alterar:
```python
url = "<nova-api>"
```

### Para salvar em outro diretório
Alterar:
```python
output_path = f"/tmp/<novo_nome>.json"
```

### Para adicionar autenticação
Adicionar headers:
```python
response = requests.get(url, headers={"Authorization": "Bearer <token>"})
```

---

## 🎯 Resumo
O módulo `ingestion` é responsável por:
- acessar APIs externas
- validar respostas
- salvar dados brutos
- preparar a entrada para a transformação

Ele é o primeiro passo do pipeline ETL.

