import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(
    page_title="المكتبة المساحية للكباري",
    page_icon="🌉",
    layout="centered"
)

# 2. تنسيق الواجهة عربي (RTL)
st.markdown("""
    <style>
    .stApp {
        direction: rtl;
        text-align: right;
    }
    div[data-baseweb="select"] {
        direction: rtl;
        text-align: right;
    }
    iframe {
        border-radius: 10px;
        border: 1px solid #ddd;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🌉 نظام المكتبة المساحية - مشروع الكباري")
st.write("اختر الكوبري والعنصر الإنشائي لاستعراض وتحميل الملفات مباشرة من الموقع:")
st.divider()

# 3. القوائم المنسدلة
bridge_categories = {
    "كباري IC Bridges": [f"IC_{i}" for i in range(13, 21)],
    "كباري UB Bridges": [f"UB_{i}" for i in range(1, 7)],
    "كباري OB Bridges": [f"OB_{i}" for i in range(72, 81)],
    "كباري FB Bridges": [f"FB_{i}" for i in range(1, 15)]
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
    "09_New_Jersey (النيوجيرسي)"
]

selected_category = st.selectbox("📌 1. اختر فئة الكوبري:", list(bridge_categories.keys()))
selected_bridge = st.selectbox("🌉 2. اختر رقم الكوبري:", bridge_categories[selected_category])
selected_element = st.selectbox("🏗️ 3. اختر العنصر الإنشائي:", structural_elements)

st.divider()

st.success(f"🎯 **العنصر المحدد:** {selected_bridge} ⬅️ {selected_element}")

# 4. Folder ID الرئيسي لقاعدة البيانات على Google Drive
FOLDER_ID = "1jibSpf7obK4z0ZC1zkDK9GNgU2GCjTDa"

st.markdown("### 📥 الملفات المتاحة للتحميل:")

# عرض مجلد Google Drive المباشر داخل شاشة الموقع
embed_url = f"https://drive.google.com/embeddedfolderview?id={FOLDER_ID}#list"

st.components.v1.html(
    f'<iframe src="{embed_url}" width="100%" height="400" frameborder="0"></iframe>',
    height=420
)
