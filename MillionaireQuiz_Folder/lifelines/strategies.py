from abc import ABC, abstractmethod


class LifelineStrategy(ABC):
    @abstractmethod
    def apply(self, options, correct_answer, lifeline_available):
        pass


class FiftyFiftyStrategy(LifelineStrategy):
    def apply(self, options, correct_answer, lifeline_available):
        if not lifeline_available:
            return {
                "visible_options": options,
                "lifeline_available": False,
                "message": "50/50 lifeline has already been used."
            }

        if correct_answer not in options or len(options) != 4:
            return {
                "visible_options": options,
                "lifeline_available": lifeline_available,
                "message": "Invalid question data."
            }

        wrong_answers = [option for option in options if option != correct_answer]

        if len(wrong_answers) < 3:
            return {
                "visible_options": options,
                "lifeline_available": lifeline_available,
                "message": "Invalid answer options."
            }

        visible_options = [correct_answer, wrong_answers[0]]

        return {
            "visible_options": visible_options,
            "lifeline_available": False,
            "message": "50/50 lifeline used successfully."
        }


class LifelineContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def use_lifeline(self, options, correct_answer, lifeline_available):
        return self.strategy.apply(options, correct_answer, lifeline_available)
