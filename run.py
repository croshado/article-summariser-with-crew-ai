from crewai import Crew,Process
from tasks import r_task,w_task
from agents import n_researcher,n_writer

# Forming the crew with some enhanced configuration
crew=Crew(
    agents=[n_researcher,n_writer],
    tasks=[r_task,w_task],
    process=Process.sequential,

)

# starting the task execution process wiht enhanced feedback

result=crew.kickoff(inputs={'topic':input("enter topic- ")
                         })
print(result)