from typing import Any
from crewai.flow.flow import Flow, start, listen, or_  #type: ignore
from litellm import completion
import os
from dotenv import load_dotenv
from pydantic import BaseModel


#Simple PromptChaining FLow without LLM with Unstructured State
class PromptChaining(Flow):
    @start()
    def step1(self):
        self.state["message"] = "We are learning"
        return self.state["message"]
        
    @listen(step1)  
    def step2(self,step1_output):
        self.state["message"] += "Crewai & implementing Agentic Design Patterns."
        return self.state["message"]
    
    @listen(or_(step1,step2))
    def logger(self,result):
        print(f"Logger result: {result}")
        return self.state
       
def kickoff():
    obj = PromptChaining()
    res = obj.kickoff()
    print(res)
    print("Final Message Output:")
    print(res["message"])


#----------------------------------------------------------



# Simple PromptChaining FLow without LLM with Structured State


# class MyState(BaseModel):
#     message: str = ""


# class PromptChaining(Flow[MyState]):
#     @start()
#     def step1(self):
#         self.state.message = "We are learning"
#         return self.state.message
        
#     @listen(step1)  
#     def step2(self,step1_output):
#         self.state.message += " Crewai & implementing Agentic Design Patterns."
#         return self.state.message
    
#     @listen(or_(step1,step2))
#     def logger(self,result):
#         print(f"Logger result: {result}")
#         return self.state
       
# def kickoff():
#     obj = PromptChaining()
#     res = obj.kickoff()
#     print(res)
#     print("Final Message Output:")
#     print(res.message)




#----------------------------------------------------------

# load_dotenv()
# gemini_api_key = os.getenv("GEMINI_API_KEY")

# # Simple PromptChaining with LLM
# class TopicOutlineFlow(Flow):
#     model:str = "gemini/gemini-1.5-flash"
    
#     @start()
#     def generate_topic(self):
#         res = completion(
#             model= self.model,
#             api_key=gemini_api_key,
#             messages=[{
#                 "role": "user",
#                 "content": "Generate a Top Tech trend blog topic for 2025. Only give topic name."
#             }]
#         )
#         topic = res["choices"][0]["message"]["content"].strip()
#         print(f"Generated Topic: {topic}")
#         return topic 
        
#     @listen(generate_topic)  
#     def generate_outline(self,topic):
#         res = completion(
#             model=self.model,
#             api_key=gemini_api_key,
#             messages=[{
#                 "role": "user",
#                 "content": f"Based on the topic '{topic}', create a concise outline for a blog post."
#             }]
#         )
#         outline = res["choices"][0]["message"]["content"].strip()
#         print(f"Generated Outline:\n{outline}")
#         return outline
       
# def kickoff():
#     flow = TopicOutlineFlow()
#     final_outline = flow.kickoff()
#     print("-------Final Output---------\n")
#     print(final_outline)
    
    
