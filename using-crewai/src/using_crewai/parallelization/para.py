
from crewai.flow.flow import Flow, start, listen, or_  # type: ignore
from litellm import completion
from dotenv import load_dotenv
import os

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")


class ParallelFlow(Flow):
    model:str = "gemini/gemini-1.5-flash"

    @start()
    def generate_variant_1(self):
        response = completion(
            model=self.model,
            api_key=gemini_api_key,
            messages=[{"role": "user", "content": "Generate a creative blog topic variant #1.Output only the blog topic name."}]
        )
        variant = response["choices"][0]["message"]["content"].strip()
        print(f"Variant 1: {variant}")
        return variant

    @start()
    def generate_variant_2(self):
        response = completion(
            model=self.model,
            api_key=gemini_api_key,
            messages=[{"role": "user", "content": "Generate a creative blog topic variant #2. Output only the blog topic name."}]
        )
        variant = response["choices"][0]["message"]["content"].strip()
        print(f"Variant 2: {variant}")
        return variant

    @listen(or_(generate_variant_1, generate_variant_2))
    def aggregate_variants(self, variant):
        # For simplicity, print the first variant received.
        print("Aggregated Variant:")
        print(variant)
        return variant

def kickoff():
    flow = ParallelFlow()
    final = flow.kickoff()
    print("Final Aggregated Output:")
    print(final)
