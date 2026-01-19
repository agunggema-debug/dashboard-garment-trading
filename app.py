import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Konfigurasi Halaman
st.set_page_config(page_title="ITAM Dashboard - Garment & Trading", layout="wide")

# 1. Simulasi Data Aset
def load_data():
    data = {
        'Asset_ID': ['AST001', 'AST002', 'AST003', 'AST004', 'AST005', 'AST006', 'AST007', 'AST008'],
        'Asset_Name': ['MacBook Pro 14', 'Zebra Barcode Scanner', 'Server Dell R740', 'Industrial PC - Sewing', 
                        'iPad Air (Sales)', 'ThinkPad X1', 'Label Printer', 'Cisco Switch'],
        'Category': ['Laptop', 'Warehouse Tool', 'Infrastructure', 'Production Tool', 
                      'Mobile', 'Laptop', 'Warehouse Tool', 'Infrastructure'],
        'Department': ['Trading/Sales', 'Logistics', 'IT', 'Factory Floor', 
                        'Trading/Sales', 'Admin', 'Logistics', 'IT'],
        'Status': ['Active', 'Active', 'Active', 'Maintenance', 'Active', 'In Storage', 'Repair', 'Active'],
        'Purchase_Value': [2500, 450, 8000, 1200, 800, 1800, 300, 1500]
    }
    return pd.DataFrame(data)

df = load_data()

# --- SIDEBAR FILTERS ---
st.sidebar.header("Filter Aset")
selected_dept = st.sidebar.multiselect("Pilih Departemen:", options=df['Department'].unique(), default=df['Department'].unique())
selected_status = st.sidebar.multiselect("Pilih Status:", options=df['Status'].unique(), default=df['Status'].unique())

df_filtered = df[(df['Department'].isin(selected_dept)) & (df['Status'].isin(selected_status))]

# --- MAIN DASHBOARD ---
st.title("🧵 IT Asset Management - Garment & Trading")
st.markdown("Monitor dan kelola aset IT di seluruh lini produksi dan perdagangan.")

# 2. KPI Metrics (Ringkasan Cepat)
total_assets = len(df_filtered)
total_value = df_filtered['Purchase_Value'].sum()
maintenance_count = len(df_filtered[df_filtered['Status'].isin(['Maintenance', 'Repair'])])

col1, col2, col3 = st.columns(3)
col1.metric("Total Aset", f"{total_assets} Unit")
col2.metric("Total Nilai Aset", f"${total_value:,}")
col3.metric("Perlu Perhatian", f"{maintenance_count} Unit", delta_color="inverse")

st.divider()

# 3. Visualisasi
left_column, right_column = st.columns(2)

with left_column:
    st.subheader("Distribusi Kategori Aset")
    fig_pie = px.pie(df_filtered, names='Category', values='Purchase_Value', 
                     hole=0.4, color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig_pie, use_container_width=True)

with right_column:
    st.subheader("Aset per Departemen")
    fig_bar = px.bar(df_filtered, x='Department', y='Purchase_Value', color='Status',
                     barmode='group', color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig_bar, use_container_width=True)

# 4. Tabel Data Detail
st.subheader("Daftar Inventaris Lengkap")
st.dataframe(df_filtered, use_container_width=True)

# Footer
st.caption("Dashboard dikembangkan untuk Monitoring Aset Real-time v1.0")