import streamlit as st
from logic import load_excel
from llm_utils import query_gemini
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import io
import contextlib

st.set_page_config(page_title="📊 Excel Insight Chatbot", layout="wide")
st.title("💬Excel Chatbot Assistant")

uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx"])

if uploaded_file:
    df = load_excel(uploaded_file)
    st.write("📄 Data Preview:")
    st.dataframe(df.head(10))

    
    st.markdown("""
    <div style='font-size:15px; font-weight:600; color:#555555; padding-bottom:12px;'>
        <strong>Note : </strong> Showing first 10 rows as preview. You can ask questions about the full dataset.
    </div>
    """, unsafe_allow_html=True
    )

    
    st.markdown("""
        <style>
            .question-label {
                font-size: 18px;
                font-weight: 500;
                margin-bottom: 0px;
                padding-bottom: 0px;
            }
            .stTextInput {
                margin-top: -10px; /* Reduce space between label and input */
            }
            input[type="text"] {
                border: 2px solid #4a90e2; /* Blue border */
                border-radius: 6px;
                padding: 8px;
                font-size: 16px;
            }
        </style>
        <div class="question-label">Ask your question:</div>
        """, unsafe_allow_html=True
    )

    
    user_question = st.text_input(label="")

    if user_question:
        prompt = f"""
        You are a data analyst. Based on this data:
        {df.to_csv(index=False)}
        Answer this question: {user_question}
        """
        response = query_gemini(prompt)
        st.markdown("### 🤖 Answer:")

        
        if "import matplotlib" in response or "plt.plot" in response or "sns." in response:
            match = re.search(r"```python(.*?)```", response, re.DOTALL)
            if match:
                code = match.group(1)

                
                code = (
                    code.replace("pd.compat.StringIO", "io.StringIO")
                        .replace("pd.StringIO", "io.StringIO")
                )

                local_vars = {
                    "df": df.copy(),
                    "plt": plt,
                    "sns": sns,
                    "pd": pd,
                    "io": io,
                }

                try:
                    with contextlib.redirect_stdout(io.StringIO()):
                        exec(code, {}, local_vars)
                    st.pyplot(plt.gcf())
                    plt.clf()
                except Exception as e:
                    st.error(f"⚠️ Chart execution failed: {e}")
            else:
                st.code(response)  
        else:
            st.write(response)
