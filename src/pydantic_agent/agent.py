from google.genai.types import HarmBlockThreshold, HarmCategory
from pydantic_ai import Agent
from pydantic_ai.models.google import GoogleModel, GoogleModelSettings
from pydantic_ai.providers.google import GoogleProvider

from .utils import get_token

API_KEY = get_token("GEMINI_API_KEY")

MODEL = "gemini-2.5-pro"

provider = GoogleProvider(api_key=API_KEY)


settings = GoogleModelSettings(
    temperature=0.2,
    google_safety_settings=[
        {
            "category": HarmCategory.HARM_CATEGORY_HATE_SPEECH,
            "threshold": HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        }
    ],
)
model = GoogleModel(MODEL, provider=provider)
agent = Agent(
    model,
    model_settings=settings,
    instructions="Be concise, reply with one sentence.",
)


async def run_agent(prompt: str):
    result = await agent.run(prompt)
    return result.output
