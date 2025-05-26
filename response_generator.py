from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

class ResponseGenerator:
    """Genera respuestas usando ChatterBot."""
    def __init__(self, name="My ChatBot"):
        self.name = name
        self.bot = ChatBot(self.name, read_only=True)
        trainer = ChatterBotCorpusTrainer(self.bot)
        trainer.train("chatterbot.corpus.spanish")

    def get_response(self, prompt: str) -> str:
        response = self.bot.get_response(prompt)
        return str(response)
