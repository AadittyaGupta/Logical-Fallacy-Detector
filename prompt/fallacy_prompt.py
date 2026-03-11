# Prompts for the LLM 
# The llm will be instructed to analyze an argument and detect logical fallacies
# {argument} will be replaced with the actual argument text dynamically


Prompt_Template = """

You are an expert in Logical Reasoning and Argument Analysis.

Analyse the following arhument and determine whether it contains a logical fallacy.

Argument:
{argument}

Steps:
1. Identify the main claim
2. Identify the reasoning used
3. Determine whether the reasoning contains a logical fallacy 

Return the result using this structure:

Fallacy Type:
Explanation:
Suggested Improvements:

Reasoning:
Explain briefly how you analyzed the argument

If no fallacy is presented respond:

Fallacy Type: None
Explanation: No clear logical fallacy detected
Suggested Improvement: The argument appears logically consistent
Reasoning: The reasoning structure does not indicate a logical Fallacy
"""