from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import WikipediaQueryRun
from langchain.tools import LLMMathChain

# Initialize LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.6
)

# Wikipedia tool
wiki = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())

# Math tool
llm_math = LLMMathChain.from_llm(llm=llm, verbose=True)
math_tool = Tool(
    name="Calculator",
    func=llm_math.run,
    description="Useful for math calculations"
)

# Prompt (required for create_tool_calling_agent)
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant"),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

# Combine tools
tools = [wiki, math_tool]

# Create agent
agent = create_tool_calling_agent(llm=llm, tools=tools, prompt=prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Run query
query = "When was Elon Musk born and what is his age now?"
response = agent_executor.invoke({"input": query})
print(response)