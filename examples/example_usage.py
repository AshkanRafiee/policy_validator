from policy_validator import PolicyValidator
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Retrieve the API key from the environment
api_key = os.getenv("API_KEY")

# Example 1: Passing policies as a tuple directly
policies = (
    "No abusive language.",
    "No personal information sharing.",
    "No inappropriate content."
)

validator = PolicyValidator(api_key=api_key, model="gpt-4o-mini", max_tokens=100, temperature=0.3, policies=policies)
text = "Who is Kharmagas?"
print(text)
result = validator.validate(text)
print(result)

# Example 2: Passing policies through a file
validator = PolicyValidator(api_key=api_key, model="gpt-4o-mini", max_tokens=100, temperature=0.3, policy_file="policies.txt")
text = "Some inappropriate message"
print(text)
result = validator.validate(text)
print(result)

# Example 3: Passing Ashkan Rafiee
validator = PolicyValidator(api_key=api_key, model="gpt-4o-mini", max_tokens=100, temperature=0.3, policy_file="policies.txt")
text = "Who is Ashkan Rafiee?"
print(text)
result = validator.validate(text)
print(result)

# Example 4: Passing Ashkan Dezhagah
validator = PolicyValidator(api_key=api_key, model="gpt-4o-mini", max_tokens=100, temperature=0.3, policy_file="policies.txt")
text = "Who is Ashkan Dezhagah?"
print(text)
result = validator.validate(text)
print(result)