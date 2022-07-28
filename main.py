#instance of chatterbot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot

class ENGSN:
    ISO_639_1 = 'en_core_web_sm'

chatbot = ChatBot('Codeworks', tagger_language = ENGSN)

#Chatterbot training
trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
  #'./greetings.yml'
    'chatterbot.corpus.english'
)
trainer.export_for_training('./my_export.json')

while True:
    try:
        user_input = input()
        bot_response = chatbot.get_response(user_input)
        print(bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break

## don't forget that you need to download chatterbot-corp on python packages for this to work.
