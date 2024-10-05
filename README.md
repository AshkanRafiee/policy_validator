
# Policy Validator

Policy Validator is a Python package that leverages OpenAI GPT models to validate text against predefined content policies.

## Features
- Uses OpenAI GPT to validate text against content moderation policies.
- Supports retry mechanisms to ensure reliability when calling the GPT API.
- Provides logging for tracking and debugging.
- Policies can be provided either as a tuple or via a file, depending on developer preference.

## Installation

You can install the package using `pip`:

```bash
pip install policy_validator
```

## Usage

You can provide policies either directly as a tuple or load them from a file. The `PolicyValidator` class supports both approaches.

### Example: Passing policies as a tuple

```python
from policy_validator import PolicyValidator

# Define policies directly as a tuple
policies = (
    "No abusive language.",
    "No personal information sharing.",
    "No inappropriate content."
)

api_key = "your_openai_api_key"
validator = PolicyValidator(api_key=api_key, model="gpt-4o-mini", max_tokens=100, temperature=0.3, policies=policies)

# Validate user input
result = validator.validate("Who is John Doe?")
print(result)
```

### Example: Passing policies via a file

Create a `policies.txt` file in the directory where you're using `policy_validator`.

```plaintext
Policy 1: No abusive language.
Policy 2: No personal information sharing.
Policy 3: No inappropriate content.
```

You can then load the policies from this file:

```python
from policy_validator import PolicyValidator

api_key = "your_openai_api_key"
validator = PolicyValidator(api_key=api_key, model="gpt-4o-mini", max_tokens=100, temperature=0.3, policy_file="policies.txt")

# Validate user input
result = validator.validate("Some inappropriate message")
print(result)
```

### Important: Securely Managing API Keys

It's recommended to **avoid hardcoding your API key** in your code as shown in the above examples. Instead, use a more secure method, such as:

- **Environment variables**: Store the API key in an environment variable and access it via `os.getenv()`.
  
  ```python
  import os
  api_key = os.getenv("OPENAI_API_KEY")
  ```

- **Secret management systems**: Use secure secret management tools such as AWS Secrets Manager, Azure Key Vault, or HashiCorp Vault to securely store and access the API key in a managed way.

### Logging

The package includes a built-in logging mechanism to help with debugging and tracking the behavior of the validation process. By default, logging is set to `INFO` level, and logs are printed to the console.

## License

This project is licensed under the MIT License.
