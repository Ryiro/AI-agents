# Mock tool implementation
import datetime
from google.adk.agents.llm_agent import Agent  # type: ignore


def get_utc_time() -> str:
    """Returns the current universal time (UTC)."""
    # We just give the AI the 'anchor' time.
    # The AI knows the offsets for London, Tokyo, NYC, etc.
    return datetime.datetime.now(datetime.timezone.utc).strftime(
        "%Y-%m-%d %H:%M:%S UTC"
    )


root_agent = Agent(
    model="gemini-2.5-flash",
    name="time_agent",
    description="An agent that tells the time for any city.",
    instruction="""You are a helpful assistant. 
    1. When asked for the time in a city, ALWAYS call 'get_utc_time' first.
    2. Use the returned UTC time and your internal knowledge of global timezones 
       to calculate the current local time for the requested city.
    3. Account for Daylight Savings if applicable based on the date provided.""",
    tools=[get_utc_time],
)
