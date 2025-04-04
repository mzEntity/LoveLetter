from common.logger import Logger

class InteractManager:
    
    def __init__(self):
        pass
    
    @staticmethod
    def askForChoice(prompt, available_choices):
        choice_count = len(available_choices)
        if choice_count == 0:
            Logger().warning("你的询问必须存在可选项......")
            return
        print(prompt)
        for key, choice in available_choices.items():
            print(f"{key}: {choice}")
        user_choice = input("> ")
        while user_choice not in available_choices:
            Logger().info("请在提供的选项中选择")
            user_choice = input("> ")
        return user_choice
    
    @staticmethod
    def askToChooseNumber(prompt, available_numbers):
        choice_count = len(available_numbers)
        if choice_count == 0:
            Logger().warning("你的询问必须存在可选项......")
            return
        print(prompt)
        for num in available_numbers:
            print(num, end="\t")
        print()
        user_choice = InteractManager._number_input("> ")
        while user_choice not in available_numbers:
            Logger().info("请在提供的选项中选择")
            user_choice = InteractManager._number_input("> ")
        return user_choice
    
    @staticmethod
    def _number_input(prompt):
        try:
            num = int(input(prompt))
        except ValueError as e:
            num = 0
        return num
    
    
def askForChoice(prompt, available_choices):
    return InteractManager.askForChoice(prompt, available_choices)

def askForNumber(prompt, available_numbers):
    return InteractManager.askToChooseNumber(prompt, available_numbers)