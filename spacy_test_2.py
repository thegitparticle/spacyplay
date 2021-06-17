import spacy
import streamlit as st

# nlp = spacy.load('en_core_web_trf')
nlp = spacy.load("en_core_web_lg")


def keyword(message):

    doc_here = nlp(message)

    x = ""

    for token in doc_here:
        if token.dep_ == "nsubj":
            # print(token.text + ' ' + 'nsubj')
            if (
                token.text == "I"
                or token.text == "i"
                or token.text == "You"
                or token.text == "you"
                or token.text == "YOU"
                or token.pos_ == "PRON"
            ):
                # print(token.text + ' ' + 'i or you')
                for token in doc_here:
                    if token.pos_ == "NOUN":
                        x = token.text
                        break
            else:
                x = token.text
                break

    if len(x) == 0:
        for token in doc_here:
            if token.pos_ == "ADJ":
                x = token.text
                break

    if len(x) == 0:
        x = message

    return x


text = st.text_area("enter your message here")

if st.button("show"):
    response = keyword(text)
    "get images and gifs for: ", response
