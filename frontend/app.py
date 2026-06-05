import requests
import streamlit as st

API_URL = "http://api:8000/process"

st.set_page_config(page_title="Monte Carlo Distribuído", layout="centered")
st.title("Simulador de Processamento Paralelo e Distribuído")
st.write("Cálculo de Pi por Monte Carlo executado em workers Celery distribuídos via Redis.")

iterations = st.number_input("Quantidade de iterações", min_value=10_000, max_value=100_000_000, value=1_000_000, step=100_000)
workers = st.slider("Quantidade de workers/chunks", min_value=1, max_value=16, value=4)

if st.button("Executar processamento"):
    with st.spinner("Processando... aguarde a finalização dos workers."):
        response = requests.post(API_URL, json={"iterations": int(iterations), "workers": int(workers)}, timeout=700)
    if response.ok:
        data = response.json()
        st.success("Processamento finalizado com sucesso!")
        st.metric("Estimativa de Pi", f"{data['pi_estimate']:.6f}")
        st.metric("Tempo de execução", f"{data['elapsed_seconds']} s")
        st.write("Detalhes do processamento:")
        st.json(data)
    else:
        st.error("Erro ao executar o processamento.")
        st.write(response.text)
