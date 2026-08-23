import streamlit as st
import os

st.set_page_config(page_title="مكتبة كوبري الغيران", layout="centered")
st.title("🌉 نظام تصفح ملفات كوبري الغيران")

# مسار المشروع (يجب أن يكون المجلد في نفس مكان ملف app.py)
root_dir = "00 GHYRAN BRIDGE"

# دالة لجلب المجلدات
def get_folders(path):
    return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]

# القوائم المنسدلة
ramps = get_folders(root_dir)
selected_ramp = st.selectbox("اختر الـ Ramp:", ramps)

work_path = os.path.join(root_dir, selected_ramp, "00 WORK")
if os.path.exists(work_path):
    elements = get_folders(work_path)
    selected_element = st.selectbox("اختر العنصر الإنشائي:", elements)
    
    files_path = os.path.join(work_path, selected_element)
    files = [f for f in os.listdir(files_path) if os.path.isfile(os.path.join(files_path, f))]
    
    st.write("---")
    for file in files:
        file_full_path = os.path.join(files_path, file)
        with open(file_full_path, "rb") as f:
            st.download_button(label=f"📥 تحميل: {file}", data=f, file_name=file)
else:
    st.error("المجلد غير موجود!")
