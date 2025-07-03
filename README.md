# CLIMADA Streamlit App

Este repositório contém uma aplicação [Streamlit](https://streamlit.io/) para visualização e análise de riscos com o [CLIMADA](https://github.com/CLIMADA-project/climada_python).  
A aplicação permite explorar exemplos de Hazard, Exposure, Vulnerability e Impact, com visualizações interativas de mapas e gráficos.

## Como rodar

1. **Clone este repositório:**
   ```bash
   git clone https://github.com/seu-usuario/climada-streamlit-app.git
   cd climada-streamlit-app
   ```

2. **Crie um ambiente virtual (opcional, mas recomendado):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Rode o app:**
   ```bash
   streamlit run app.py
   ```

5. **Acesse no navegador:**  
   Normalmente em http://localhost:8501

## Estrutura do projeto

```
climada-streamlit-app/
│
├── app.py               # Código principal do Streamlit
├── requirements.txt     # Dependências
├── README.md            # Este arquivo
└── data/                # (opcional) Dados de exemplo
```

## Personalização

- Os dados usados inicialmente são simulados (mock).  
- Para usar seus próprios dados, adapte o `app.py` conforme necessário.
- Se quiser conectar ao seu repositório do CLIMADA modificado, instale localmente, por exemplo:
  ```bash
  pip install -e ../climada-env
  ```

## Referências

- [CLIMADA Documentation](https://climada-python.readthedocs.io/)
- [Streamlit Documentation](https://docs.streamlit.io/)

---

Sinta-se à vontade para abrir issues ou contribuir!
