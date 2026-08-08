# 📁 Pasta src/transformation — Módulo de Transformação

A pasta `src/transformation` contém o módulo responsável pela **transformação dos dados** no pipeline ETL. Esta é a etapa intermediária entre ingestão e carga.

O arquivo principal é `transform.py`, que implementa a função `run_transformation()`.

---

## 📄 Arquivo: transform.py

Este arquivo contém a função responsável por transformar os dados brutos gerados pela etapa de ingestão.

### 🎯 Objetivo
Aplicar transformações nos dados ingeridos, como:
- limpeza
- normalização
- padronização
- enriquecimento
- validação

Atualmente, o módulo funciona como um *placeholder*, retornando o próprio arquivo de entrada.

---

## 🔍 Fluxo detalhado da função `run_transformation()`

### 1. Log inicial
```python
print(f"Transforming data from {data_path}")
```
Indica qual arquivo está sendo transformado.

### 2. Transformação (placeholder)
```python
# Aqui você pode transformar o JSON, limpar, normalizar, etc.
```
Este comentário indica onde a lógica real de transformação deve ser implementada.

### 3. Retorno
```python
return data_path
```
Atualmente, retorna o mesmo arquivo recebido.

---

## 📦 Estrutura atual da pasta
```
src/transformation/
└── transform.py
```

---

## 🧪 Como testar

### Execução isolada
```bash
python -c "from transformation.transform import run_transformation; print(run_transformation('/tmp/test.json'))"
```

### Testes unitários
- Criar testes em `tests/test_transformation.py`.
- Mockar leitura de arquivos.
- Validar que a função retorna o caminho esperado.

---

## 🏗️ Como estender

### Para implementar transformação real
Adicionar lógica como:
```python
import json
with open(data_path) as f:
    data = json.load(f)

# aplicar transformações

output_path = data_path.replace('api_data', 'transformed_data')
with open(output_path, 'w') as f:
    json.dump(data, f)

return output_path
```

### Exemplos de transformações possíveis
- Remover campos desnecessários
- Converter tipos
- Normalizar strings
- Criar novas colunas
- Validar estrutura

### Para salvar em outro diretório
Alterar o caminho de saída:
```python
output_path = f"/tmp/staged/{timestamp}.json"
```

---

## 🎯 Resumo
O módulo `transformation` é responsável por:
- receber dados brutos
- aplicar transformações
- preparar os dados para a carga no Data Lake

Atualmente, funciona como um placeholder, mas está pronto para receber qualquer lógica de transformação necessária.

