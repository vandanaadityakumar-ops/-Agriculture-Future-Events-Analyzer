import streamlit as st
import pandas as pd
import data_processor
import model
import visuals

st.set_page_config(page_title="Future Yield Analyzer", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #1e2130; padding: 15px; border-radius: 10px; border: 1px solid #3e4250; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌾 Agriculture Future Events Analyzer")
st.write("---")

with st.sidebar:
    st.header("📂 Data Center")
    uploaded_file = st.file_uploader("Upload Farm Excel", type=["xlsx"])
    if st.button("🚀 Train AI Brain"):
        if uploaded_file:
            df = data_processor.prepare_data(uploaded_file)
            acc = model.train_and_save_model(df)
            st.success(f"AI Trained! Accuracy: {acc:.1%}")
        else:
            st.error("Upload a file first!")

if uploaded_file:
    df = data_processor.prepare_data(uploaded_file)
    
    stats = data_processor.get_summary_stats(df)
    m1, m2, m3 = st.columns(3)
    m1.metric("Total Harvest", f"{stats['Total Yield']:,} kg", "Yield")
    m2.metric("Avg Climate", f"{stats['Avg Temp']:.1f}°C", "Temp")
    m3.metric("Peak Rain", f"{stats['Max Rain']} mm", "Rain")

    st.markdown("### 📊 Interactive Farm Insights")
    t1, t2, t3 = st.tabs(["🌧️ Rain Impact", "📈 Timeline", "🔗 Relationships"])
    
    with t1:
        st.plotly_chart(visuals.plot_weather_vs_yield(df), use_container_width=True)
        with st.expander("🔍 Understanding the Rain Graph"):
            st.write("This scatter plot shows if your yield grows when it rains. The **Red Line** is the trend—if it points up, your farm is water-dependent. Hover over any dot to see the date and yield for that specific day.")

    with t2:
        st.plotly_chart(visuals.plot_yield_timeline(df), use_container_width=True)
        with st.expander("🔍 Understanding the Timeline"):
            st.write("This shows your growth history. Use the **Slider** at the bottom to zoom into specific months where you had high or low production.")

    with t3:
        st.plotly_chart(visuals.plot_correlation_heatmap(df), use_container_width=True)

    st.markdown("### 🔮 Future Scenario Simulator")
    with st.container(border=True):
        c1, c2 = st.columns(2)
        f_temp = c1.slider("Forecasted Temp (°C)", 0, 50, 25)
        f_rain = c2.slider("Forecasted Rain (mm)", 0, 500, 100)
        
        if st.button("Predict Future Yield"):
            pred = model.make_prediction(f_temp, f_rain)
            if pred:
                st.subheader(f"Estimated Result: :green[{pred:.2f} kg]")
            else:
                st.warning("Please train the model using the sidebar first!")
else:
    st.image("https://images.unsplash.com/photo-1523348837708-15d4a09cfac2?auto=format&fit=crop&q=80&w=1000", caption="Prepare for the future of farming.")


# streamlit run app.py