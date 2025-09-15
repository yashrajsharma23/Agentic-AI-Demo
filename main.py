import os
from dotenv import load_dotenv
from data_agent import DataAnalysisAgent
import config

load_dotenv()

def main():
    print("OPEN AI Key::"+config.API_KEY)
    api_key = os.getenv(config.API_KEY)

    # if not api_key:
    #     print("Please set your OPENAI_API_KEY environment variable")
    #     return
    
    agent = DataAnalysisAgent(api_key)

    print("Data Analysis Agent initialized!") 
    print("Commands you can try:") 
    print("- Load a CSV file: 'Load the CSV file data.csv'") 
    print("- Get statistics: 'Show me summary statistics'")
    print("- Create charts: :'Create a histogram the sales column'")
    print("- Ask questions: `What are the trends in this data?'")
    print("InType 'quit' to exit.In")
    while True:
        user_input = input ("You: ") 
        if user_input.lower() in ['quit', 'exit']: 
            break
        response = agent.chat(user_input) 
        print(f"Agent: {response}\n")

if __name__== "__main__": 
    main()

#https://www.youtube.com/watch?v=AofaDJ0OUq4