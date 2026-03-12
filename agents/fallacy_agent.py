
from prompt.fallacy_prompt import Prompt_Template
from llm.llm_client import call_llm
from utils.parser import parse_response

class LogicalFallacyAgent:
    def analyzer(self, argument):
        """
            Analyze a single argument and return a structured information
        """

        # Prepare prompt for the LLM by inserting the argument
        prompt = Prompt_Template.format(argument=argument)

        # Call the llm to get the required anlysiss
        response = call_llm(prompt)
        
        #  DEBUG PRINT - to see the raw response from the llm before parsing
        # print("RAW LLM RESPONSE:\n", response) 

        # parse the response into structure fields
        parsed = parse_response(response)

        return parsed