from common.singleton import singleton
from common.pretty import colored_text

@singleton
class Logger:
    def __init__(self):
        pass
    
    def info(self, message):
        print(colored_text(message, font_color="green"))
        
    def warning(self, message):
        print(colored_text(message, font_color="yellow"))
        
    def error(self, message):
        print(colored_text(message, font_color="red"))
        
        
if __name__ == "__main__":
    Logger().info("info...")
    Logger().warning("warning...")
    Logger().error("error...")