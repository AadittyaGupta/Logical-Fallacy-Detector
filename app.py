import streamlit as st
import streamlit.components.v1 as components

from agents.fallacy_agent import LogicalFallacyAgent
from config import APP_TITLE


agent = LogicalFallacyAgent()

st.set_page_config(
    page_title=APP_TITLE,
    layout="centered"
)

### Copy button component

def copy_to_clipboard_button(text):

    components.html(
        f"""
        <textarea id="copyText" style="display:none;">{text}</textarea>

        <button id="copyBtn" onclick="copyText()" 
        style="
        padding:8px 16px;
        border-radius:6px;
        border:1px solid #ccc;
        cursor:pointer;
        background-color:#f0f2f6;">
        Copy Result
        </button>

        <script>
        function copyText() {{
            var copyText = document.getElementById("copyText");
            var btn = document.getElementById("copyBtn");
            
            // Copy the text
            copyText.style.display = "block";
            copyText.select();
            document.execCommand("copy");
            copyText.style.display = "none";
            
            // Provide visual feedback on the button itself
            btn.innerHTML = "Copied!";
            setTimeout(function() {{
                btn.innerHTML = "Copy Result";
            }}, 2000);
        }}
        </script>
        """,
        height = 50,
    )

### HEADER 

st.title(APP_TITLE)

st.divider()

st.write(
"""
### What Are Logical Fallacies?

Logical fallacies are **mistakes in reasoning** that make an argument look convincing even when the logic behind it is weak or incorrect. They are very common in everyday conversations, debates, advertisements, and social media.

#### Why Do Logical Fallacies Matter?

* They can **mislead people into believing incorrect arguments**
* They weaken the **quality of discussions and decision-making**
* They contribute to the **spread of misinformation**
* Recognizing them helps build **strong critical thinking skills**

"""
)

### EXPANDABLE EXAMPLE SECTION 

with st.expander("See Example Arguments & Explanations"):
    
    st.markdown("#### 1. Ad Hominem")
    st.write("**What it is:** Attacking the person making the argument rather than addressing the argument itself.")
    st.code('"We should not trust his economic ideas because he dropped out of college."')

    st.markdown("#### 2. Hasty Generalization")
    st.write("**What it is:** Jumping to a broad conclusion based on a very small or unrepresentative piece of evidence.")
    st.code('"Two students cheated on the exam, so the entire class must be dishonest."')

    st.markdown("#### 3. Slippery Slope")
    st.write("**What it is:** Arguing that a small first step will inevitably lead to a chain of extreme, negative events.")
    st.code('"If we allow students to use calculators, soon they will stop learning math altogether."')


st.write(
"""
The goal is to help users **think more critically, evaluate arguments better, and communicate ideas more logically.**
"""
)
st.divider()
### INPUT AREA


# argument = st.text_area(
#     "Enter an Argument:",
#     height = 50
# )

### INPUT AREA

st.markdown("### Enter an Argument:")

argument = st.text_area(
    "Hidden Label String", # <- This string MUST be here, or Streamlit throws an error!
    height = 50, 
    label_visibility="collapsed" 
)


### ANALYSIS BUTTON 

if st.button("Analyze Argument"):
    if not argument.strip():
        st.warning("Please enter an argument to analyze...")

    else:
        with st.spinner("Analyzing argument...."):
            result = agent.analyzer(argument)

        st.subheader("Analysis Result")

        with st.container(border=True):

            st.markdown("### Detected Fallacy")
            st.info(result["fallacy"])

            st.markdown("### Explanation")
            st.write(result["explanation"])

            st.markdown("### Suggested Improvement")
            st.success(result["suggestion"])


        ### COPY BUTTON 


        result_text = f"""
Fallacy Type: {result['fallacy']}

Explanation: {result['explanation']}

Suggested Improvement: {result['suggestion']}
"""
        
        copy_to_clipboard_button(result_text)

        # if st.button("Confirm Copy"):
        #     st.toast("Result copied!")


        ### REASONING SECTION 

        with st.expander("Show AI Reasoning"):
            st.write(result["reasoning"])