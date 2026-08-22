import streamlit as st

# 1. إعدادات الصفحة الرئيسية
st.set_page_config(
    page_title="المكتبة المساحية للكباري",
    page_icon="🌉",
    layout="centered"
)

# 2. تنسيق الواجهة لتكون باللغة العربية (من اليمين إلى اليسار)
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
    </style>
""", unsafe_allow_html=True)

# 3. العنوان ورأس الصفحة
st.title("🌉 نظام المكتبة المساحية - مشروع الكباري")
st.write("اختر الكوبري والعنصر الإنشائي للوصول المباشر إلى ملفات الـ DXF والإحداثيات:")
st.divider()

# 4. بيانات الكباري والعناصر الإنشائية
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

# 5. القوائم المنسدلة للاختيار
selected_category = st.selectbox("📌 1. اختر فئة الكوبري:", list(bridge_categories.keys()))
selected_bridge = st.selectbox("🌉 2. اختر رقم الكوبري:", bridge_categories[selected_category])
selected_element = st.selectbox("🏗️ 3. اختر العنصر الإنشائي:", structural_elements)

st.divider()

# 6. عرض الاختيار الحالي
st.success(f"🎯 **الطلب المحدد:** {selected_bridge} ⬅️ {selected_element}")

# 7. رابط Google Drive المباشر والزر الخاص بالفتح
drive_folder_url = "https://drive.google.com/drive/folders/1jibSpf7obK4z0ZC1zkDK9GNgU2GCjTDa?usp=sharing"

st.markdown("### 📥 تنزيل الملفات:")
st.link_button("📂 فتح مجلد الملفات على Google Drive", drive_folder_url, use_container_width=True)
