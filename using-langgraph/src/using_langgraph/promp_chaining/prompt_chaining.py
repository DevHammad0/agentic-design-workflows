from langgraph.func import entrypoint, task




@task
def step1(hello: str):
    return f"{hello} I am"

@task
def step2(input:str):
    return input + " Happy"


@entrypoint()
def run_flow(name: str):
    # result = step1(name).result()
    # result = step2(result).result()
    
    result1 = step1(name).result()
    result2 = step2(result1).result()
    
    return {"step1_output": result1, "step2_output": result2}


def main():
    repsonse = run_flow.invoke(input="Hello")
    return repsonse









