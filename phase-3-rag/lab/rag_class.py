import os
from dotenv import load_dotenv
from openai import OpenAI, APIConnectionError, RateLimitError

class DublinAssistant:
    def __init__(self):
        self.client: OpenAI = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.knowledge_base: str | None = None
        self.history: list[dict[str, str]] = []
        self.instruction: str = ""

    def load_knowledge(self, file_path: str) -> bool:
        try:
            with open(file_path, "r") as file:
                self.knowledge_base = file.read()
                self.instruction = f"""You are an assistant that will answer 
                                    using this info: {self.knowledge_base}"""

        except FileNotFoundError:
            print(f"'{file_path}' not found")
            return False

        except Exception as e:
            print(f"Unexpected error loading knowledge: {e}")
            return False
        
        print("Knowledge loaded successfully from file.")
        return True

    def ask(self, question: str) -> str:
        if not self.knowledge_base:
            raise  NoKnowledgeBaseError("Error: No knowledge loaded.")
        
        self.history.append({"role": "user", "content": question})

        try:
            res = self.client.responses.create(
                model="gpt-4o-mini",
                input=self.history,
                instructions=self.instruction
            )

            answer = res.output_text

            self.history.append({"role": "assistant", "content": answer})

            return answer
        
        except (APIConnectionError, RateLimitError) as e:
            self.history.pop()
            raise type(e)(f"Error with API: {e}") from e
        
        except Exception as e:
            self.history.pop()
            raise Exception(f"Unexpected error while asking: {e}") from e
        

class NoKnowledgeBaseError(Exception):
    """Exception raised when the assistant doesn't have it's knowledge base"""
    pass

def main():
    load_dotenv()

    assistant = DublinAssistant()

    if not assistant.load_knowledge("../data/dublin_info.txt"):
        return
    
    greet(["Hi, I'm your assistant for your Dublin trip, how can I help you?",
           "(Write 'q', 'quit' or 'exit' to stop the conversation)"])
    
    while True:

        try:
            user_question = get_user_question("\nWhat's your question: ")

        except SystemExit:
            return

        if not user_question:
            print("Please enter a valid question.")
            continue
            
        if check_conversation_ending(user_question):
            print("\n-----Conversation ended-----")
            return
        
        try:
            answer = assistant.ask(user_question)

            print(f"Answer: {answer}")
        
        except Exception as e:
            print(f"Error: {e}")
            print("\nPlease try again.")
            continue

def greet(messages: list[str]) -> None:
    for message in messages:
        print(message)

def get_user_question(message: str) -> str:
    try:
        user_question = input(message).strip()

        return user_question

    except KeyboardInterrupt as e:
        print("\nConversation forcefully ended.")
        raise SystemExit(e)

def check_conversation_ending(input: str) -> bool:    
    if input.lower() in ['q', 'quit', 'exit']:
        return True
    
    return False

if __name__ == "__main__":
    main()