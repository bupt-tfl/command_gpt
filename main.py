# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import open_ai_bot


def start_gpt():
    # Use a breakpoint in the code line below to debug your script.
    openai = open_ai_bot.OpenAIBot()
    while True:
        user_input = input("Enter Question: ")
        if user_input == "exit":
            break
        print("Answer: ", openai.reply(user_input))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_gpt()

