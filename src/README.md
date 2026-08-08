# 📁 Pasta src — Código-Fonte do Pipeline ETL

A pasta `src/` contém toda a lógica do pipeline ETL, organizada de forma modular em três etapas principais:

1. **Ingestão** (`ingestion/`)
2. **Transformação** (`transformation/`)
3. **Carga** (`load/`)

O arquivo `main.py` orquestra essas etapas e define o fluxo completo do ETL.

---

## 🧠 Estrutura da pasta
```
src/
├── ingestion/
│   └── ingest_api.py
├── transformation/
│   └── transform.py
├── load/
│   └── load.py
└── main.py
```

Cada módulo é responsável por uma parte específica do pipeline.

---

# 🚀 main.py — Orquestrador do ETL

O arquivo `main.py` é o ponto de entrada do pipeline ETL. Ele coordena as três etapas principais:

1. **Ingestão de dados via API**
2. **Transformação dos dados**
3. **Upload do resultado para o Cloud Storage**

---

## 🔍 Fluxo detalhado

### 1. Ingestão
```python
data_path = run_ingestion()
```
- Chama `ingestion.ingest_api.run_ingestion()`
- Baixa dados de uma API externa
- Salva o arquivo bruto localmente
- Retorna o caminho do arquivo salvo

### 2. Transformação
```python
transformed_path = run_transformation(data_path)
```
- Chama `transformation.transform.run_transformation()`
- Lê o arquivo bruto
- Aplica limpeza e padronização
- Gera um novo arquivo transformado
- Retorna o caminho do arquivo transformado

### 3. Carga no Cloud Storage
```python
bucket = "data-architecture-demo-raw"
destination = transformed_path.split("/")[-1]
upload_to_gcs(transformed_path, bucket, f"raw/{destination}")
```
- Chama `load.load.upload_to_gcs()`
- Envia o arquivo transformado para o bucket RAW
- Usa o prefixo `raw/` para manter a organização Medallion

---

## 🧩 Função principal
```python
def main():
    print("ETL started")

    data_path = run_ingestion()
    transformed_path = run_transformation(data_path)

    bucket = "data-architecture-demo-raw"
    destination = transformed_path.split("/")[-1]
    upload_to_gcs(transformed_path, bucket, f"raw/{destination}")

    print("ETL finished")
```

### Responsabilidades
- Orquestrar o pipeline
- Garantir a ordem correta das etapas
- Definir o bucket de destino
- Registrar logs simples no console

---

## 🧪 Como testar

### Execução local
```
python src/main.py
```

### Testes unitários
Os testes ficam na pasta `tests/`. Cada módulo pode ser testado individualmente.

---

## 🏗️ Como estender

### Para adicionar novas etapas:
- Criar um novo módulo em `src/<nova-etapa>/`
- Implementar a função principal
- Importar e chamar no `main.py`

### Para mudar o bucket:
Alterar:
```python
bucket = "data-architecture-demo-raw"
```

### Para mudar o prefixo:
Alterar:
```python
f"raw/{destination}"
```

---

## 🎯 Resumo
A pasta `src/` contém o núcleo do pipeline ETL. O arquivo `main.py` é o orquestrador que integra ingestão, transformação e carga, garantindo que os dados fluam corretamente até o Cloud Storage.

