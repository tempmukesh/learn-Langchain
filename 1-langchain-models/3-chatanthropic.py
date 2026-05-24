from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(
    model_name = "claude-sonnet-4-5-20250929",
    temperature=0.0,
    timeout = 10,
    stop = ["none"]
)