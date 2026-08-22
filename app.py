import streamlit as st

# 1. تهيئة الصفحة
st.set_page_config(
    page_title="المكتبة المساحية للكباري", page_icon="🌉", layout="centered"
)

# 2. تنسيق الواجهة لتكون من اليمين لليسار (RTL)
st.markdown(
    """
    <style>
    .stApp {
        direction: rtl;
        text-align: right;
    }
    div[data-baseweb="select"] {
        direction: rtl;
        text-align: right;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# 3. العنوان الرئيسي
st.title("🌉 نظام المكتبة المساحية - الكباري")
st.write("اختر الكوبري والعنصر الإنشائي للوصول المباشر لملفات الرسم والإحداثيات")
st.divider()

# 4. قاعدة بيانات الكباري والعناصر الإنشائية
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

# 5. اختيار الكوبري والعنصر
selected_category = st.selectbox(
    "📌 1. اختر نوع الكوبري:", list(bridge_categories.keys())
)
selected_bridge = st.selectbox(
    "🌉 2. اختر رقم الكوبري:", bridge_categories[selected_category]
)
selected_element = st.selectbox(
    "🏗️ 3. اختر العنصر الإنشائي:", structural_elements
)

st.divider()

# 6. عرض النتيجة
st.success(f"🎯 **الطلب المحدد:** {selected_bridge}  ➡️  {selected_element}")

# ⚠️ استبدل الرابط داخل علامات التنصيص برابط مجلد Google Drive الخاص بك:
drive_folder_url = (
    "https://drive.google.com/drive/folders/ضع_رابط_الفولدر_هنا"
)

st.markdown("### 📥 الوصول للملفات:")
st.link_button(
    "📂 فتح مجلد الملفات على Google Drive",
    drive_folder_url,
    use_container_width=True,
)
