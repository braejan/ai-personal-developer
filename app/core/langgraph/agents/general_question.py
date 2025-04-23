from langgraph.prebuilt import create_react_agent

from app.core.langgraph.llm.llm import get_basic_model


_model = get_basic_model()


def general_question_answer(question: str):
    """
    Used for answer general questions when no needed to go to the internet.

    Args:
        question (str): _description_

    Returns:
        str: response from the llm
    """
    response = _model.invoke(question)
    return response.content


# Create general Q&A agent
general_question_answer_agent = create_react_agent(
    _model,
    tools=[general_question_answer],
    name="general_question_answer_agent",
    prompt=(
        "You are a general question answer expert. "
        "Always use the one tool general_question_answer to answer the question."
        "Do not mention any internal toughts or transfering steps. Just do it."
    ),
)
