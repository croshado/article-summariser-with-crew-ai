from crewai import Agent
from tools import tool
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
import os


## call the gemini models
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                           verbose=True,
                           temperature=0.5,
              # create your google gemini api and store in .env file with variable GOOGLE_API_KEY
                           google_api_key=os.getenv("GOOGLE_API_KEY"))

# Creating a senior researcher agent with memory and verbose mode

n_researcher=Agent(
    role="Senior Researcher",
    goal='Unccover ground breaking reports in {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity, lead the way in"
        "innovation, eager to explore and share knowledge that could change"
        "the world."

    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True

)

## creating a write agent with custom tools responsible in writing news blog

n_writer = Agent(
  role='Writer',
  goal='Narrate stories about {topic}',
  verbose=True,
  memory=True,
  backstory=(
    "have a knack for making difficult subjects easy to understand"
    "create engaging narratives that captivate and educate, introducing new ideas."
    "bring discoveries to light in an accessible manner.."
  ),
  tools=[tool],
  llm=llm,
  allow_delegation=False
)
