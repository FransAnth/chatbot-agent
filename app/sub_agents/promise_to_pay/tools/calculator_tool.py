from datetime import datetime

from agents import function_tool


@function_tool
def calculate_total_amount_due(outstanding_amount: int, ptp_date: str):
    """Calculates the total amount to be paid by the user upon promised pay

    Args:
        outstanding_amount (int): The remaining amount to be paid
        ptp_date (str): The promised date by the customer to pay the outstanding amount in 'MM/DD/YYYY' format.
    """
    print("Calculator tool running...")

    ptp_date = datetime.strptime(ptp_date, "%m/%d/%Y")
    today = datetime.now()

    date_difference = ptp_date - today
    number_of_days = date_difference.days + 1

    print(f"number of days: {number_of_days}")
    print(f"outstanding amount: {outstanding_amount}")

    if number_of_days > 15:
        return "Number of days should not exceed 15 days. Please ask the user to move the promise to pay date to an earlier date."
    elif number_of_days < 0:
        return "The PTP date the user provided is in the past. Please ask the user to choose a future date that reflects when they intend to make the payment and does not exceed 15 days from today."

    total_amout_due = int(outstanding_amount) + number_of_days * 20

    return total_amout_due
