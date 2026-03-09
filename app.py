import streamlit as st
import pandas as pd

st.set_page_config(page_title="Endüstriyel Anomali Tespit Sistemi", layout="wide")

st.title("Endüstriyel Enerji Verimliliği ve Anomali Tespit Sistemi")
st.write("Bu panel, üretim hattı verileri üzerinden anomali tespiti ve enerji tüketimi analizini görselleştirir.")

df = pd.read_csv("analyzed_production_data.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])

total_records = len(df)
anomaly_count = len(df[df["anomaly_pred"] == "anomaly"])
normal_count = len(df[df["anomaly_pred"] == "normal"])
avg_power = df["power_w"].mean()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Toplam Kayıt", total_records)
col2.metric("Anomali Sayısı", anomaly_count)
col3.metric("Normal Kayıt", normal_count)
col4.metric("Ortalama Güç (W)", f"{avg_power:.2f}")

st.subheader("Sıcaklık Grafiği")
st.line_chart(df.set_index("timestamp")["temperature_c"])

st.subheader("Güç Tüketimi Grafiği")
st.line_chart(df.set_index("timestamp")["power_w"])

st.subheader("Anomali İçeren Kayıtlar")
st.dataframe(df[df["anomaly_pred"] == "anomaly"])
