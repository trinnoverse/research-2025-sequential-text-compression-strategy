def text_abbreviation(text: str) -> str:
    """Contracts common phrases in the input text to their abbreviations.

    Args:
        text (str): The input string in which phrases will be contracted.

    Returns:
        str: The text after contracting specified phrases.
    """
    # Define the dictionary for common contractions
    contractions = {
        # days of the week
        "Monday": "Mon",
        "Tuesday": "Tue",
        "Wednesday": "Wed",
        "Thursday": "Thu",
        "Friday": "Fri",
        "Saturday": "Sat",
        "Sunday": "Sun",

        # professions
        "doctor": "Dr.",
        "professor": "Prof.",
        "engineer": "Eng.",
        "manager": "Mgr.",
        "assistant": "Asst.",
        "accountant": "Acct.",
        "nurse": "Nrs.",

        # actions
        "appointment": "appt.",
        "schedule": "sched.",
        "meeting": "mtg.",
        "confirmation": "conf.",
        "cancellation": "canc.",
        "available": "avail.",
        "reminder": "remind.",
        "follow-up": "f/up",
        "preparation": "prep.",

        # common prhases
        "as soon as possible": "ASAP",
        "please confirm": "Pls. conf.",
        "looking forward to": "LFT",
        "let me know": "LMK",
        "see you later": "CUL",
        "thank you": "Thx",
        "have a nice day": "HND",
        "take care": "TC",
    }

    # Iterate over the contractions and substitute in the text
    for full, abbr in contractions.items():
        text = text.replace(full, abbr)

    return text
