from app.core.langgraph.llm.llm import get_basic_model
from googlesearch import search
from langgraph.prebuilt import create_react_agent

_model = get_basic_model()


def google_search(query: str):
    """Used for answer questions when is needed to go to the internet.

    Args:
        query (str): the query to search in the internet

    Returns:
        list: return the first 5 list results
    """
    return list(search(query, num_results=5))


# Create Google search agent
google_search_agent = create_react_agent(
    _model,
    tools=[google_search],
    name="google_search_agent",
    prompt=(
        "You are a Google search expert. "
        "Always use the one tool google_search to search the internet."
    ),
)
