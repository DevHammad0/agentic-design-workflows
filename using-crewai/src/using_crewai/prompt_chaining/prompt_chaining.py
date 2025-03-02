from typing import Any
from crewai.flow.flow import Flow, start, listen
from crewai.flow.persistence.base import FlowPersistence
from litellm import completion
import os
from dotenv import load_dotenv


# #Simple PromptChaining FLow without LLM
# class PromptChaining(Flow):
#     @start()
#     def step1(self):
#         return f"We are learning"
        
#     @listen(step1)  
#     def step2(self,step1_output):
#         return f"{step1_output} Crewai & implementing Agentic Design Patterns."
       
# def kickoff():
#     obj = PromptChaining()
#     res = obj.kickoff()
#     print(res)


#----------------------------------------------------------

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Simple PromptChaining with LLM
class TopicOutlineFlow(Flow):
    model:str = "gemini/gemini-1.5-flash"
    
    @start()
    def generate_topic(self):
        res = completion(
            model= self.model,
            api_key=gemini_api_key,
            messages=[{
                "role": "user",
                "content": "Generate a Top Tech trend blog topic for 2025. Only give topic name."
            }]
        )
        topic = res["choices"][0]["message"]["content"].strip()
        print(f"Generated Topic: {topic}")
        return topic 
        
    @listen(generate_topic)  
    def generate_outline(self,topic):
        res = completion(
            model=self.model,
            api_key=gemini_api_key,
            messages=[{
                "role": "user",
                "content": f"Based on the topic '{topic}', create a concise outline for a blog post."
            }]
        )
        outline = res["choices"][0]["message"]["content"].strip()
        print(f"Generated Outline:\n{outline}")
        return outline
       
def kickoff():
    flow = TopicOutlineFlow()
    final_outline = flow.kickoff()
    print("-------Final Output---------\n")
    print(final_outline)
    
    
