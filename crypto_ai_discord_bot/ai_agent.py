import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_chart(symbol, price_data, indicators_summary):
    prompt = f"""
    You are a crypto analyst AI. Analyze the chart for {symbol}.
    Data: {price_data}
    Indicators: {indicators_summary}

    Provide:
    1. Risk assessment
    2. Setup ideas (long/short)
    3. Key price levels
    4. Any chart patterns
    """

    response = openai.ChatCompletion.create(
        model='gpt-4',
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
