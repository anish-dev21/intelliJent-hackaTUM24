from swarm import Agent, Swarm
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = Swarm()

message = """
from swarm import Agent, Swarm
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = Swarm()

message = 

def run_classes_agent(output_from_breakdown):
    response = client.run(
        agent=classes_agent,
        messages=[{"role": "user", "content": output_from_breakdown}]
    )
    return response.messages[-1]["content"]

def run_combination_agent(classes_output, dryness_output):
    content = f"Recommendations on code structure: {classes_output}\n\nRecommendations on dryness: {dryness_output}"
    response = client.run(
        agent=combination_agent,
        messages=[{"role": "user", "content": content}]
    )
    return response.messages[-1]["content"]

breakdown_agent = Agent(
    name="Breakdown Agent",
    instructions="summarize this code into a yaml file",
)

classes_agent = Agent(
    name="Classes Agent",
    instructions="Suppose you are a coding teacher, give some clear and very concise instructions of how the structure of the code could be optimized",
)
dryness_agent = Agent(
    name="Dyness Agent",
    instructions="examine this code and provide very very concise feedback on where the code is not being dry"
)
combination_agent = Agent(
    name="Combination Agent",
    instructions="You are gonna get two separate blocks of text related to improvements that a user can make to improve his code, combine this two texts into one so that it still makes sense semantically make this text as concise as possible and dont add any extra information"
)

# Run Breakdown Agent first
breakdown_response = client.run(
    agent=breakdown_agent,
    messages=[{"role": "user", "content": message}]
).messages[-1]["content"]

dryness_response = client.run(
    agent=dryness_agent,
    messages=[{"role": "user", "content": message}]
).messages[-1]["content"]

classes_response = run_classes_agent(breakdown_response)

combination_response = run_combination_agent(classes_response, 
                                             dryness_response)

# Print the final response from Classes Agent
print("***Solution***")
print(combination_response)
"""

def run_classes_agent(output_from_breakdown):
    """Run the Classes Agent with the output from Breakdown Agent."""
    response = client.run(
        agent=classes_agent,
        messages=[{"role": "user", "content": output_from_breakdown}]
    )
    return response.messages[-1]["content"]

def run_combination_agent(classes_output, dryness_output):
    content = f"Recommendations on code structure: {classes_output}\n\nRecommendations on dryness: {dryness_output}"
    response = client.run(
        agent=combination_agent,
        messages=[{"role": "user", "content": content}]
    )
    return response.messages[-1]["content"]

breakdown_agent = Agent(
    name="Breakdown Agent",
    instructions="summarize this code into a yaml file",
)

classes_agent = Agent(
    name="Classes Agent",
    instructions="Suppose you are a coding teacher, give some clear and very concise instructions of how the structure of the code could be optimized",
)
dryness_agent = Agent(
    name="Dyness Agent",
    instructions="examine this code and provide very very concise feedback on where the code is not being dry"
)
combination_agent = Agent(
    name="Combination Agent",
    instructions="You are gonna get two separate blocks of text related to improvements that a user can make to improve his code, combine this two texts into one so that it still makes sense semantically make this text as concise as possible and dont add any extra information"
)

# Run Breakdown Agent first
breakdown_response = client.run(
    agent=breakdown_agent,
    messages=[{"role": "user", "content": message}]
).messages[-1]["content"]

dryness_response = client.run(
    agent=dryness_agent,
    messages=[{"role": "user", "content": message}]
).messages[-1]["content"]

classes_response = run_classes_agent(breakdown_response)

combination_response = run_combination_agent(classes_response, 
                                             dryness_response)

# Print the final response from Classes Agent
print("***Solution***")
print(combination_response)