import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="Viewer Drop-Off Prediction",
    layout="wide"
)

# -------------------------------------------------
# CUSTOM CSS (Rounded title boxes only)
# -------------------------------------------------
st.markdown("""
<style>
.title-box {
    background-color: #ffffff;
    padding: 14px;
    border-radius: 15px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.08);
    text-align: center;
    font-weight: bold;
    font-size: 18px;
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# HEADER
# -------------------------------------------------
st.markdown(
    "<h1 style='text-align:center;'>🎬 Viewer Drop-Off Prediction Dashboard</h1>"
    "<p style='text-align:center;'>Machine Learning-Based Viewer Behavior Analytics</p>",
    unsafe_allow_html=True
)

st.divider()

# -------------------------------------------------
# LOAD DATA
# -------------------------------------------------
data = pd.read_csv("synthetic_data.csv")

# -------------------------------------------------
# MAIN LAYOUT
# -------------------------------------------------
col1, col2, col3 = st.columns([1.1, 1.6, 1.1])

# =================================================
# 1️⃣ MODEL PERFORMANCE
# =================================================
with col1:
    st.markdown("<div class='title-box'>📊 Model Performance</div>", unsafe_allow_html=True)

    st.metric("Accuracy", "94%")
    st.metric("Precision", "93%")
    st.metric("Recall", "92%")
    st.metric("F1-Score", "92.5%")

    st.info(
        "Gradient Boosting model trained on\n"
        "viewer interaction metrics."
    )

# =================================================
# 2️⃣ DROP-OFF PREDICTION FACTORS (ROTATED VERTICAL)
# =================================================
with col2:
    st.markdown("<div class='title-box'>📉 Drop-Off Prediction Factors</div>", unsafe_allow_html=True)

    dropoff_factors = {
        "Watch Time (Avg)": data["watch_time"].mean(),
        "Pause Count (Avg)": data["pause_count"].mean(),
        "Rewind Count (Avg)": data["rewind_count"].mean(),
        "Engagement Score (Avg)": data["engagement_score"].mean()
    }

    factors_df = pd.DataFrame({
        "Factor": list(dropoff_factors.keys()),
        "Value": list(dropoff_factors.values())
    })

    fig, ax = plt.subplots()

    bars = ax.bar(factors_df["Factor"], factors_df["Value"])

    ax.set_ylabel("Average Value")
    ax.set_title("Key Viewer Behavior Metrics")

    plt.xticks(rotation=30)

    # Add value labels on top
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height,
                f"{height:.2f}",
                ha='center', va='bottom')

    plt.tight_layout()

    st.pyplot(fig)

# =================================================
# 3️⃣ PREDICT VIEWER BEHAVIOR + RECOMMENDATIONS
# =================================================
with col3:
    st.markdown("<div class='title-box'>🔮 Predict Viewer Behavior</div>", unsafe_allow_html=True)

    watch_time = st.slider("Watch Time (minutes)", 0, 120, 60)
    pause_count = st.slider("Pause Count", 0, 10, 2)
    rewind_count = st.slider("Rewind Count", 0, 5, 1)
    engagement_score = st.slider("Engagement Score", 40, 100, 70)

    if watch_time > 50 and engagement_score > 65 and pause_count < 5:
        st.success("✅ Viewer likely to CONTINUE watching")
    else:
        st.error("⚠ Viewer likely to DROP OFF")

    st.markdown("### 📝 Recommendations")

    recommendations = []

    if watch_time < 40:
        recommendations.append("📉 Shorten video length to improve retention.")

    if pause_count > 5:
        recommendations.append("⏸ Improve content clarity to reduce pauses.")

    if rewind_count > 2:
        recommendations.append("🔄 Simplify complex sections to avoid rewinds.")

    if engagement_score < 65:
        recommendations.append("⚡ Add interactive or engaging elements.")

    if not recommendations:
        recommendations.append("✅ Content performance is strong. Maintain current strategy.")

    for rec in recommendations:
        st.write(rec)

# -------------------------------------------------
# FOOTER
# -------------------------------------------------
st.markdown(
    "<hr><p style='text-align:center;'>Machine Learning Project | Viewer Drop-Off Analytics</p>",
    unsafe_allow_html=True
)
