from crewai import Task
from tools import tool
from agents import n_researcher,n_writer

# Research task
r_task = Task(
  description=(
    "Identify the next big trend in {topic}."
    "Focus on identifying pros and cons and the overall narrative."
    "Your final report should effectively communicate the main points in a clear and concise manner.,"
    "its market opportunities, and potential risks."
  ),
  expected_output='A comprehensive 3 paragraphs long report on the latest trends.',
  tools=[tool],
  agent=n_researcher,
)

# Writing task with language model configuration
w_task = Task(
  description=(
    "Compose an insightful article on {topic}."
    "Focus on the latest trends and how it's impacting the industry."
    "This article should be easy to understand, engaging, and positive."
  ),
  expected_output='A 4 paragraph article on {topic} advancements formatted as markdown.',
  tools=[tool],
  agent=n_writer,
  async_execution=False,
  output_file=input("file name- ")  # Example of output customization
)