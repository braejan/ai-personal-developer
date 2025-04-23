from app.core.langgraph.llm.llm import get_basic_model
import requests
import html2text
from langgraph.prebuilt import create_react_agent

_model = get_basic_model()


def read_url(url: str):
    """Used for reading a url and returning the page in a single markdown document.

    Args:
        link (str): the link to be oppened

    Returns:
        srt: retunr the page in markdown text.
    """
    ### get html content from url
    response = requests.get(url)
    # you can check the response.status_code first if you like (see comment)
    html_content = response.text
    converter = html2text.HTML2Text()
    converter.ignore_links = False  # preserve hyperlinks

    # Convert the HTML to Markdown
    return converter.handle(html_content)


# Create Google search agent
text_web_browser_agent = create_react_agent(
    _model,
    tools=[read_url],
    name="text_web_browser_agent",
    prompt=(
        "You are a Web Browser that use only text. "
        "Always use the one tool read_url to read a specific url"
    ),
)
