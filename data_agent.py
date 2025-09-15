import os
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory

from tools import DataAnalysisTools
import config

class DataAnalysisAgent: 
    def __init__(self, aki_key: str): 
        # initialize the LLM 
        self.llm = ChatOpenAI(
            temperature=0, 
            openai_api_key= config.API_KEY, 
            model_name="gpt-5-nano"#"gpt-4o"
        )
        # Initialize tools 
        self.data_tools = DataAnalysisTools()

        # Create tool definitions for the agent self.tools
        self.tools=[
            Tool(
                name="Load CSV", 
                func=self.data_tools.load_csv, 
                description="Load a CSV file. Input should be the file path."
            ),
            Tool(
                name="Get Summary Stats", 
                func=self.data_tools.get_summary_stats, 
                description="Get summary statistics for the loaded dataset."
            ),
            Tool(
                name="Create Visualization", 
                func=lambda input_str: self._parse_viz_input(input_str), 
                description="Create a visualization. Input format: 'chart_type, x_column, y_column'"
            )
        ]

        #Initialize Memory
        self.memory= ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )

       

        #Create Agent
        self.agent=initialize_agent(
            self.tools,
            self.llm,
            agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
            memory=self.memory,
            verbose=True
        )

    def _parse_viz_input(self, input_str:str)->str:
        parts= input_str.split(',')
        if len(parts)>=2:
            chart_type=parts[0].strip()
            x_column=parts[1].strip()
            y_column=parts[2].strip() if len(parts)>2 else None
            return self.data_tools.create_visualization(chart_type,x_column,y_column)
        return "Invalid input format. Use: 'chart_type, x_column, y_column"
    
    def chat(self, message:str)->str:
        try:
            response=self.agent.run(input=message)
            return response
        except Exception as e:
            return f"Error: {str(e)}"