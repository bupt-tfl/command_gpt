import open_ai_bot
import sys

input = sys.argv[1]

print("Res: " + open_ai_bot.OpenAIBot().reply(input))

