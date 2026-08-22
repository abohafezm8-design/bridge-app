import os
import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(
    page_title="المكتبة المساحية للكباري", page_icon="🌉", layout="centered"
)

# 2. تنسيق الواجهة عربي (RTL)
st.markdown(
    """
    <style>
    .stApp { direction: rtl; text-align: right; }
    div[data-baseweb="select"] { direction: rtl; text-align: right; }
    .stDownloadButton button { width: 100%; background-color: #28a745; color: white; font-weight: bold; }
    </style>
""",
    unsafe_allow_html=True,
)

st.title("🌉 نظام المكتبة المساحية - مشروع الكباري")
st.write("اختر الكوبري والعنصر الإنشائي لتنزيل الملفات مباشرة على جهازك:")
st.divider()

# 3. القوائم المنسدلة للكباري والعناصر
bridge_categories = {
    "كباري IC Bridges": (
        [f"IC_{i}" for i in range(13, 21)],
        "IC_Bridges",
    ),
    "كباري UB Bridges": ([f"UB_{i}" for i in range(1, 7)], "UB_Bridges"),
    "كباري OB Bridges": ([f"OB_{i}" for i in range(72, 81)], "OB_Bridges"),
    "كباري FB Bridges": ([f"FB_{i}" for i in range(1, 15)], "FB_Bridges"),
}

structural_elements = [
    ("01_Piles (الخوازيق)", "01_Piles"),
    ("02_Pile_Caps (القواعد)", "02_Pile_Caps"),
    ("03_Columns (الأعمدة)", "03_Columns"),
    ("04_Pier_Caps (الفريمات)", "04_Pier_Caps"),
    ("05_Bearings (الركائز)", "05_Bearings"),
    ("06_Girders (الكمر)", "06_Girders"),
    ("07_Diaphragms (الدايفرامات)", "07_Diaphragms"),
    ("08_Deck_Slabs (البلاطات)", "08_Deck_Slabs"),
    ("09_New_Jersey (النيوجيرسي)", "09_New_Jersey"),
]

selected_cat_label = st.selectbox(
    "📌 1. اختر فئة الكوبري:", list(bridge_categories.keys())
)
bridges_list, cat_folder = bridge_categories[selected_cat_label]

selected_bridge = st.selectbox("🌉 2. اختر رقم الكوبري:", bridges_list)

selected_elem_tuple = st.selectbox(
    "🏗️ 3. اختر العنصر الإنشائي:",
    structural_elements,
    format_func=lambda x: x[0],
)
elem_folder = selected_elem_tuple[1]

st.divider()

# 4. مسار المجلد داخل المستودع
target_path = os.path.join(
    "Survey_Bridges_Database", cat_folder, selected_bridge, elem_folder
)

st.success(f"🎯 **المحدد:** {selected_bridge} ⬅️ {selected_elem_tuple[0]}")
st.markdown("### 📥 الملفات المتاحة للتحميل المباشر:")

# 5. قراءة الملفات وعرض زر التحميل المباشر لكل ملف
if os.path.exists(target_path):
  files = [
      f
      for f in os.listdir(target_path)
      if not f.startswith(".") and not f.startswith("~$")
  ]

  if files:
    for file_name in files:
      file_full_path = os.path.join(target_path, file_name)

      with open(file_full_path, "rb") as fp:
        file_bytes = fp.read()

      col1, col2 = st.columns([3, 1])
      with col1:
        st.write(f"📄 **{file_name}**")
      with col2:
        st.download_button(
            label="⬇️ تحميل مباشر",
            data=file_bytes,
            file_name=file_name,
            mime="application/octet-stream",
            key=file_name,
        )
      st.divider()
  else:
    st.info("ℹ️ لا توجد ملفات مرفوعة داخل هذا العنصر حالياً.")
else:
  st.warning("⚠️ هذا المجلد لم يتم رفعه بعد على GitHub.")
