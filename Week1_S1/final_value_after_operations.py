"""
Tigger has developed a new programming language Tiger with only four operations and one variable tigger.

bouncy and flouncy both increment the value of the variable tigger by 1.
trouncy and pouncy both decrement the value of the variable tigger by 1.
Initially, the value of tigger is 1 because he's the only tigger around! Given a list of strings operations containing a list of operations, return the final value of tigger after performing all the operations.


Example Usage:

operations = ["trouncy", "flouncy", "flouncy"]
final_value_after_operations(operations)

operations = ["bouncy", "bouncy", "flouncy"]
final_value_after_operations(operations)
Example Output:

2
4
"""


def final_value_after_operations(operations):

    tigger = 1
    for i in range(len(operations)):

        if (operations[i] == "bouncy" or operations[i] == "flouncy"):
            tigger += 1
        else:
            tigger -= 1

    return tigger


operations1 = ["trouncy", "flouncy", "flouncy"]
print(final_value_after_operations(operations1))

operations2 = ["bouncy", "bouncy", "flouncy"]
print(final_value_after_operations(operations2))
