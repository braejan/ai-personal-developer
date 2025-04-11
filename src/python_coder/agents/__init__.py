TEAM_MEMBER_CONFIGURATIONS = {
    "tech_lead": {
        "name": "tech_lead",
        "desc": (
            "Responsible for planning, architecture, and design of the software system"
        ),
        "desc_for_llm": (
            "Plans, designs, and architects the software system. "
            "Outputs a Markdown report summarizing findings. Software Architect can not do math or programming."
        ),
        "is_optional": False,
    },
    "coder": {
        "name": "coder",
        "desc": (
            "Responsible for code implementation, debugging and optimization, handling technical programming tasks"
        ),
        "desc_for_llm": (
            "Executes Python or Bash commands, performs mathematical calculations, and outputs a Markdown report."
        ),
        "is_optional": False,
    },
    "qa_tester": {
        "name": "qa_tester",
        "desc": (
            "Responsible for code testing, debugging and optimization, handling quality assurance tasks"
        ),
        "desc_for_llm": (
            "Executes Python scripts by adding unit tests, integration tests, debugging, validating coverage and usecases tests."
        ),
        "is_optional": False,
    },
}

TEAM_MEMBERS = list(TEAM_MEMBER_CONFIGURATIONS.keys())