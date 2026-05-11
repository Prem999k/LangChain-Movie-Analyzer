from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import Optional,List
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()
from langchain_mistralai import ChatMistralAI
model = ChatMistralAI(model="mistral-small-2603")



class Movie(BaseModel):
    title: Optional[str]
    director: Optional[str]
    release_year: Optional[str]
    genre: Optional[str]
    cast: Optional[List[str]]
    imdb_rating: Optional[str]
    story_theme: Optional[str]
    summary: Optional[str]


parser=PydanticOutputParser(pydantic_object=Movie)


prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """Extract movie details from the given paragraph
        {format_instructions}
"""),
("human",
        "{movie_paragraph}")]
        )

movie_paragraph = input("Enter Movie Paragraph:\n\n")

final_prompt = prompt.invoke({
    "movie_paragraph": movie_paragraph,
    "format_instructions": parser.get_format_instructions()
})
response = model.invoke(final_prompt)
movie_data = parser.parse(response.content)


print(response.content)