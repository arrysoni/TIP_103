"""
The deli counter is busy, and orders have piled up. To serve the last customer first, you need to reverse the order of the deli orders. Given a string orders where each individual order is separated by a single space, write a recursive function reverse_orders() that returns a new string with the orders reversed.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def reverse_orders(orders):
    pass
Example Usage:

print(reverse_orders("Bagel Sandwich Coffee"))
Example Output:

Coffee Sandwich Bagel
"""

def reverse_orders(orders):
    words = orders.split()
    if not words:
        return ""

    def helper(i):
        if i == 0:
            return words[0]
        return words[i] + " " + helper(i - 1)

    return helper(len(words) - 1)

str = "Bagel Sandwich Coffee"
print(reverse_orders(str))