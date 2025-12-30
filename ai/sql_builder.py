from ai.llm_client import call_llm

def build_sql(user_prompt, schema_metadata):
    prompt = f"""
You are an analytics engineer.
Available tables and columns:
{schema_metadata}

User request:
{user_prompt}

Generate Snowflake SQL only.
"""
    return call_llm(prompt)
