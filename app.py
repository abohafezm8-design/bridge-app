import streamlit as st

st.set_page_config(page_title="منظومة ملفات المساحة - مشروع الكباري", layout="centered", page_icon="🏗️")

st.title("🏗️ بوابة استلام ملفات المساحة")
st.write("اختر نوع الكوبري والرقم والعنصر الإنشائي للوصول للملفات المتاحة:")

# 1. قائمة نوع الكوبري
bridge_type = st.selectbox(
    "1️⃣ اختر نوع الكوبري:",
    ["IC Bridges", "UB Bridges (Underpass)", "OB Bridges (Overpass)", "FB Bridges (Footbridges)"]
)

# 2. توليد قائمة أرقام الكباري ديناميكياً حسب النوع
bridge_numbers = []

if "IC" in bridge_type:
    bridge_numbers = [f"IC {i}" for i in range(13, 21)]  # IC 13 إلى IC 20
elif "UB" in bridge_type:
    bridge_numbers = [f"UB {i}" for i in range(1, 7)]    # UB 1 إلى UB 6
elif "OB" in bridge_type:
    bridge_numbers = [f"OB {i}" for i in range(72, 81)]  # OB 72 إلى OB 80
elif "FB" in bridge_type:
    bridge_numbers = [f"FB {i}" for i in range(1, 15)]   # FB 1 إلى FB 14

selected_bridge = st.selectbox("2️⃣ اختر رقم الكوبري:", bridge_numbers)

# 3. قائمة العناصر الإنشائية الثابتة لكل الكباري
structural_elements = [
    "الخوازيق (Piles)",
    "القواعد (Pile Caps)",
    "الأعمدة (Columns)",
    "الفريمات (Pier Caps)",
    "الركائز (Bearings)",
    "الكمر (Girders)",
    "الدايفرامات (Diaphragms)",
    "البلاطات (Deck Slabs)",
    "النيوجيرسي (New Jersey Barriers)"
]

selected_element = st.selectbox("3️⃣ اختر العنصر الإنشائي:", structural_elements)

st.divider()

# عرض النتيجة وزر التحميل
st.success(f"📌 **الطلب المحدد:** {selected_bridge} ⬅️ {selected_element}")

# هنا يتم وضع رابط مجلد Google Drive الخاص بالعنصر المختار أو زر التحميل
st.markdown("### 📥 الملفات المتاحة للتحميل:")

# مثال لعرض الملفات (يمكن ربطه بـ Drive API أو روابط مباشرة)
st.info(f"اضغط أسفله للوصول لملفات ({selected_element}) الخاصة بـ ({selected_bridge}):")

# رابط مباشر لفتح الفولدر المطلوب على Google Drive
drive_folder_url = "https://drive.google.com" # يتم استبدال الرابط برابط المجلد الخاص بك
st.link_button("📂 فتح مجلد الملفات على Google Drive", drive_folder_url)
