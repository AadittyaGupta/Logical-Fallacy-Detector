"""
This section will evaluate the Logical Fallacy Agent using a predefined dataset of arguments.
It will measure how often the LLM correctly identifies the expected logical fallacy
"""

import json
import os
from agents.fallacy_agent import LogicalFallacyAgent

def load_dataset(dataset_path):
    """
    It loads the argument dataset from JSON file
    """

    try:
        with open(dataset_path, "r", encoding="utf-8") as file:

            data = json.load(file)

        if not isinstance(data, list):
            raise ValueError("Dataset format invalid: expected a list of objects")
        
        return data
    
    except FileNotFoundError:
        print(f"\n Dataset file nor found: {dataset_path}")
        exit(1)

    except json.JSONDecodeError:
        print("\n Dataset JSON is malformed")
        exit(1)
    
    except Exception as e:
        print(f"\n Unexpected error loading dataset: {e} ")
        exit(1)



def normalize_fallacy(text):
    """
    Normalize fallacy names to improve matching between expected dataset labels and LLM outputs
    """
    
    if not text:
        return ""
    
    text = text.lower().strip()

    # Removes extra words like "fallacy" bcuz its not mentioned in our predefined dataset
    text = text.replace("fallacy", "").strip()

    return text



def run_evaluation(dataset):
    """
    
    """

    agent = LogicalFallacyAgent()

    total_test = len(dataset)
    correct_predictions = 0
    incorrect_predictions = 0
    skipped_test = 0

    print(f"\n Running Logical Fallacy Detection Evaluation:")

    for index, item in enumerate(dataset, start=1):

        argument = item.get("argument", "").strip()
        expected = item.get("expected_fallacy", "").strip()


        if not argument or not expected:
            print("\n Skipping test {index} (invalid dataset entry)")
            skipped_test += 1
            continue

        print(f"\n Test {index}")
        print("-" * 40)
        print(f" Argument: {argument}")



        try:
            result = agent.analyzer(argument)

            predicted = result.get("fallacy", "")

            normalized_expected = normalize_fallacy(expected)
            normalized_predicted = normalize_fallacy(predicted)

            print(f" Expected: {expected}")
            print(f" Predicted: {predicted}")


            ## Handles connection errors returned by parser
            if predicted == "Connection Error":
                print(f" Result: LLM Connection Error")
                skipped_test += 1
                continue

            ## For checking correctness
            if normalized_expected in normalized_predicted:
                print(f" Result: Correct")
                correct_predictions += 1
            else:
                print(f" Result: Incoorect")
                incorrect_predictions += 1

        except Exception as e:
            print(f" Error during evaluation: {e}")
            skipped_test += 1
    

    ## Final Summary
    print("\n" + "-" * 60)
    print("Evaluation Summary")
    print("-" * 60)

    evaluated_tests = total_test - skipped_test

    if evaluated_tests == 0:
        print("No valid test were evaluated")
        return
    
    accuracy = (correct_predictions / evaluated_tests) * 100

    print(f" Total Tests: {total_test}")    
    print(f" Evaluated tests: {evaluated_tests}")
    print(f" Correct Predictions: {correct_predictions}")
    print(f" Incorrect Predictions: {incorrect_predictions}")
    print(f" Skipped Tests: {skipped_test}")
    print(f"\n Model Accuracy: {accuracy:.2f}")

    



if __name__ == "__main__":

    dataset_path = os.path.join("data", "argument_dataset.json")

    dataset = load_dataset(dataset_path)

    run_evaluation(dataset)