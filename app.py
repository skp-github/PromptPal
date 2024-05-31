# import required packages
import streamlit as st
from streamlit.external.langchain import StreamlitCallbackHandler
from chat import configure_retrieval_chain
from utils import MEMORY, DocumentLoader

st.set_page_config(page_title="Prompt Pal", page_icon="🐨")
st.title("Prompt Pal 🐨")


uploaded_files = st.sidebar.file_uploader(
    label="Upload files",
    type=list(DocumentLoader.supported_extensions.keys()),
    accept_multiple_files=True
)
if not uploaded_files:
    st.info("Please upload documents to continue.")
    st.stop()

# use compression by default:
use_compression = st.checkbox("compression", value=False)
use_flare = st.checkbox("flare", value=False)
use_moderation = st.checkbox("moderation", value=False)

CONV_CHAIN = configure_retrieval_chain(
    uploaded_files,
    use_compression=use_compression,
    use_flare=use_flare,
    use_moderation=use_moderation
)

if st.sidebar.button("Clear message history"):
    MEMORY.chat_memory.clear()

avatars = {"You": "user", "PP": "assistant"}

if len(MEMORY.chat_memory.messages) == 0:
    st.chat_message("assistant").markdown("Ask me anything!")

for msg in MEMORY.chat_memory.messages:
    st.chat_message(avatars[msg.type]).write(msg.content)

assistant = st.chat_message("assistant")
if user_query := st.chat_input(placeholder="Give me 3 keywords for what you have right now"):
    st.chat_message("user").write(user_query)
    container = st.empty()
    stream_handler = StreamlitCallbackHandler(container)
    with st.chat_message("assistant"):
        if use_flare:
            params = {
                "user_input": user_query,
            }
        else:
            params = {
                "question": user_query,
                "chat_history": MEMORY.chat_memory.messages,
            }
        response = CONV_CHAIN.run(params, callbacks=[stream_handler])
        # Display the response from the chatbot
        if response:
            container.markdown(response)