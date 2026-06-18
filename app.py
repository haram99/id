import streamlit as st
import os
import base64

def main():
    st.set_page_config(page_title="Student File Portal", page_icon="📄")
    
    st.title("🎓 السجل الأكاديمي")
    st.write("ادخل رقم الهوية")

    # .strip() removes any accidental spaces the user might type or paste
    student_id = st.text_input("", placeholder="e.g., 10000000001").strip()

    if st.button("بحث"):
        if student_id:
            # Looks for files/1130876095.pdf
            file_path = f"files/{student_id}.pdf"
            
            if os.path.exists(file_path):
                st.success(f"الملف موجود للهوية: {student_id}")
                
                with open(file_path, "rb") as f:
                    file_bytes = f.read()
                
                st.download_button(
                    label="⬇️ Download PDF",
                    data=file_bytes,
                    file_name=f"{student_id}.pdf",
                    mime="application/pdf"
                )

                st.info("💡 To print: Open the file and use your browser's Print function (Ctrl+P).")
                
                base64_pdf = base64.b64encode(file_bytes).decode('utf-8')
                pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'
                st.markdown(pdf_display, unsafe_allow_html=True)
                
            else:
                # If the file isn't in the folder, you'll see this new error message
                st.error(f"لم يتم العثور على ملف برقم الهوية: {student_id}")
        else:
            st.warning("الرجاء إدخال رقم الهوية أولاً.")

if __name__ == "__main__":
    main()
