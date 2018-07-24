from mycroft import MycroftSkill, intent_file_handler


class BenchAssistant(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('assistant.bench.intent')
    def handle_assistant_bench(self, message):
        self.speak_dialog('assistant.bench')


def create_skill():
    return BenchAssistant()

