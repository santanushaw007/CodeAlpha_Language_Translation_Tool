import streamlit as st
from googletrans import Translator, LANGUAGES

# Page configuration
st.set_page_config(
    page_title="GlobalSpeak |Multi-Language Translator",
    page_icon="🌐",
    layout="centered"
)

def main():
    st.title("GlobalSpeak | Multi-Language Translator")
    st.write("Translate your text from one language to another.")

    # Text input
    input_text = st.text_area("Source Text", placeholder="Enter text to translate...", height=200)

    languages = get_languages()

    target_language = st.selectbox("Select target language", languages, index=languages.index("english"))

    if st.button("Translate"):
        translated = translate(input_text, target_language)
        st.text(translated)
    else:
        st.warning("Please enter text to translate")
        
        

def get_languages():
    return list(LANGUAGES.values())

def translate(input_text, target_language):
    translator = Translator()
    # Find the code (e.g., 'en') from the name (e.g., 'english')
    target_code = [code for code, name in LANGUAGES.items() if name == target_language][0]
    translation = translator.translate(input_text, dest=target_code)
    return translation.text
    


if __name__ == "__main__":
    main()
