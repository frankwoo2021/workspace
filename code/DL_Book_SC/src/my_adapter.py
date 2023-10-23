from chatterbot.logic import LogicAdapter

class MyLogicAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
     super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        if statement.text.find('订位') >= 0:
            return True
        return False

    def process(self, input_statement, additional_response_selection_parameters):
        import random
        from chatterbot.conversation import Statement
        
        # Randomly select a confidence between 0 and 1
        confidence = random.uniform(0, 1)
        
        # 
        answers = ['订位日期、时间及人数?', '哪一天? 几点? 人数呢?']
        selected_statement = Statement(text=random.choice(answers))
        selected_statement.confidence = confidence

        return selected_statement