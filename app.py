import urllib.parse
import streamlit as st

st.set_page_config(
    page_title="المكتبة المساحية للكباري", page_icon="🌉", layout="centered"
)

st.markdown(
    """
    <style>
    .stApp { direction: rtl; text-align: right; }
    div[data-baseweb="select"] { direction: rtl; text-align: right; }
    .main-btn {
        display: inline-block;
        width: 100%;
        background-color: #28a745;
        color: white;
        padding: 12px;
        text-align: center;
        text-decoration: none;
        font-weight: bold;
        border-radius: 8px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

st.title("🌉 نظام المكتبة المساحية - مشروع الكباري")
st.write("اختر الكوبري والعنصر الإنشائي للوصول المباشر لملفات العمل:")
st.divider()

bridge_categories = {
    "كباري IC Bridges": [f"IC_{i}" for i in range(13, 21)],
    "كباري UB Bridges": [f"UB_{i}" for i in range(1, 7)],
    "كباري OB Bridges": [f"OB_{i}" for i in range(72, 81)],
    "كباري FB Bridges": [f"FB_{i}" for i in range(1, 15)],
}

structural_elements = [
    "01_Piles (الخوازيق)",
    "02_Pile_Caps (القواعد)",
    "03_Columns (الأعمدة)",
    "04_Pier_Caps (الفريمات)",
    "05_Bearings (الركائز)",
    "06_Girders (الكمر)",
    "07_Diaphragms (الدايفرامات)",
    "08_Deck_Slabs (البلاطات)",
    "09_New_Jersey (النيوجيرسي)",
]

selected_category = st.selectbox(
    "📌 1. اختر فئة الكوبري:", list(bridge_categories.keys())
)
selected_bridge = st.selectbox(
    "🌉 2. اختر رقم الكوبري:", bridge_categories[selected_category]
)
selected_element = st.selectbox(
    "🏗️ 3. اختر العنصر الإنشائي:", structural_elements
)

st.divider()

st.success(f"🎯 **الطلب المحدد:** {selected_bridge} ⬅️ {selected_element}")

# المعرف الرئيسي لمجلد Drive
MAIN_FOLDER_ID = "1jibSpf7obK4z0ZC1zkDK9GNgU2GCjTDa"

# البحث المباشر داخل المجلد
search_query = f"{selected_bridge} {selected_element.split()[0]}"
encoded_query = urllib.parse.quote(search_query)

# رابط الفلترة المباشرة داخل Drive
direct_search_url = f"https://drive.google.com/drive/u/0/search?q=parent:{MAIN_FOLDER_ID}%20{encoded_query}"

st.markdown("### 📥 تنزيل الملفات:")
st.markdown(
    f"""
    <a href="{direct_search_url}" target="_blank" class="main-btn">
        ⬇️ تحميل ملفات {selected_bridge} - {selected_element.split()[0]} فوراً
    </a>
""",
    unsafe_allow_html=True,
)
