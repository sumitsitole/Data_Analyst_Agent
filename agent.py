from google.adk.agents import LlmAgent
from google.adk.code_executors import BuiltInCodeExecutor

root_agent = LlmAgent(
    name="my_assistance",
    model="gemini-3-flash-preview",
    description="A data analyst that can write and execure Python code.",
    instruction="""You are Data analyst. you can:
    -Write python code to analyze data
    -Create calculations and statistics 
    -Solve math problems by running code
    -Generate data visualizations (describe the chart)

    Always run code to verify answers before presenting them."""
,
   code_executor=BuiltInCodeExecutor(),
)