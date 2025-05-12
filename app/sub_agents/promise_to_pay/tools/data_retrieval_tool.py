from agents import function_tool


@function_tool
def retrieve_user_data(user_name: str) -> str:
    """
    Retrieves user data from database based on the provided user name.

    Args:
        user_name (str): The name of the user whose data is to be retrieved.
    """
    print("Data retrieval tool running...")

    user_info_dataset = [
        {
            "name": "kim",
            "outstanding_amount": 1000,
            "currency": "PHP",
            "due_date": "April 1, 2025",
        },
        {
            "name": "ivan",
            "outstanding_amount": 16000,
            "currency": "PHP",
            "due_date": "December 1, 2024",
        },
    ]

    user_data = None
    for user_info in user_info_dataset:
        if user_info.get("name") == user_name.lower():
            user_data = user_info
            break

    print("User name:", user_data.get("name"))
    print("Outstanding amount:", user_data.get("outstanding_amount"))
    print("Due Date:", user_data.get("due_date"))

    if user_data == None:
        return "There are no information retrieved for this user."

    return user_data
