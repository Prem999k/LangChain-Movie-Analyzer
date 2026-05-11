import streamlit as st
import json

from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate

from langchain_mistralai import ChatMistralAI

from pydantic import BaseModel
from typing import Optional, List

# Load ENV Variables
load_dotenv()

# Streamlit Page Config
st.set_page_config(
    page_title="Movie Analyzer AI",
    page_icon="🎬"
)

st.title("🎬 Movie Analyzer AI")

st.write(
    "Paste any movie paragraph and extract movie details instantly."
)

# Load Model
model = ChatMistralAI(
    model="mistral-small-2603"
)

# Pydantic Model
class Movie(BaseModel):

    title: Optional[str]

    director: Optional[str]

    release_year: Optional[str]

    genre: Optional[str]

    cast: Optional[List[str]]

    imdb_rating: Optional[str]

    story_theme: Optional[str]

    summary: Optional[str]

# Structured Output Model
structured_model = model.with_structured_output(Movie)

# Prompt Template
prompt = ChatPromptTemplate.from_messages([

    (
        "system",
        """
Extract movie details from the given paragraph.
"""
    ),

    (
        "human",
        "{movie_paragraph}"
    )
])

# Text Area
movie_paragraph = st.text_area(
    "Enter Movie Paragraph",
    height=250
)

# Analyze Button
if st.button("Analyze Movie"):

    if movie_paragraph.strip() == "":

        st.warning(
            "Please enter a movie paragraph."
        )

    else:

        with st.spinner(
            "Analyzing Movie..."
        ):

            # Create Prompt
            final_prompt = prompt.invoke({

                "movie_paragraph":
                movie_paragraph

            })

            # Structured Output Response
            response = structured_model.invoke(
                final_prompt
            )

        # Display Results
        st.subheader("🎥 Movie Details")

        st.write(
            f"**Title:** {response.title}"
        )

        st.write(
            f"**Director:** {response.director}"
        )

        st.write(
            f"**Release Year:** {response.release_year}"
        )

        st.write(
            f"**Genre:** {response.genre}"
        )

        st.write(
            f"**Cast:** {response.cast}"
        )

        st.write(
            f"**IMDb Rating:** {response.imdb_rating}"
        )

        st.write(
            f"**Story Theme:** {response.story_theme}"
        )

        st.write(
            f"**Summary:** {response.summary}"
        )

        # JSON Output
        st.subheader("📦 JSON Output")

        st.json(
            json.loads(
                response.model_dump_json()
            )
        )