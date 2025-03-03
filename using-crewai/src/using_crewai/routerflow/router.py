from crewai.flow.flow import Flow, start, listen, router,or_,and_  #type: ignore
from dotenv import load_dotenv
from pydantic import BaseModel
import random


load_dotenv()


# Router flow without llm

class ExampleState(BaseModel):
    success_flag: bool = False

class RouterFlow(Flow[ExampleState]):
    
    @start()
    def step1(self):
        print("Starting the structured flow")
        random_boolean = random.choice([True, False])
        self.state.success_flag = random_boolean
    
    @router(step1)
    def step2(self):
        if self.state.success_flag:
            return "success"
        else:
            return "failed"
        
    @listen("success")
    def step3(self):
        print("Step 3 Executed - Success")
        
    @listen("failed")
    def step4(self):
        print("Step 4 Executed -  Failed ")
        
        
        
def kickoff():
    flow = RouterFlow()
    flow.kickoff()
    

