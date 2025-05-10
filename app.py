import streamlit as st
from parse_dataset import get_oee_from_query

st.set_page_config(page_title="OEE Smart Factory Assistant", page_icon="📦")
st.title("📦 OEE Query Assistant")
st.markdown("Ask me: *e.g., `OEE of Device_2 in Ahmedabad in July`*")

query = st.text_input("🗨️ Enter your query:")

if query:
    with st.spinner("Thinking..."):
        results = get_oee_from_query(query)

    if results:
        st.success("**Result:**")
        for r in results:
            st.markdown(f"🔹 {r}")
    else:
        st.warning("No matching data found.")
