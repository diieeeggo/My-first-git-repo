
class FinanceCalculator:
    
    def calculateProfit(self, revenue, expenses):
        """
        Calculates the profit based on revenue and expenses.

        Args:
            revenue (float): The total revenue generated.
            expenses (float): The total expenses incurred.

        Returns:
            float: The calculated profit.

        Raises:
            ValueError: If either revenue or expenses is negative.
        """

        # Ensure that both revenue and expenses are non-negative
        if revenue < 0 or expenses < 0:
            raise ValueError("Revenue and expenses must be non-negative.")

        # Calculate profit by subtracting expenses from revenue
        profit = revenue - expenses

        # Log the calculation for debugging purposes
        # This log statement can be helpful during development and debugging
        print(f"Profit calculation: Revenue - Expenses = {revenue} - {expenses} = {profit}")

        # Return the calculated profit
        return profit
