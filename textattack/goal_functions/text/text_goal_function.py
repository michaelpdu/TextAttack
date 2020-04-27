from textattack.goal_functions import GoalFunction

class TextGoalFunction(GoalFunction):
    """"" A goal function defined on a model that outputs text.
        
        model: The PyTorch or TensorFlow model used for evaluation.
        original_output: the original output of the model
    """
    def __init__(self, model):
        super().__init__(model)
        
    def _process_model_outputs(self, _, outputs):
        """ Processes and validates a list of model outputs. 
        
            Flatten list of lists to a single list.
        """
        return [output for batch in outputs for output in batch]
        
    def _get_displayed_output(self, raw_output):
        return raw_output