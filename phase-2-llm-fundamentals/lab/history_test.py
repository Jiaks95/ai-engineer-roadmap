import os
from dotenv import load_dotenv
from openai import OpenAI, APIConnectionError, RateLimitError

def main():
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("Error: Key not found.")
        return
    
    client = OpenAI(api_key=api_key)

    messages = []

    print("Write 'q' to stop the conversation.")

    while True:

        try: 
            user_message = input("\nYou: ").strip()

        except KeyboardInterrupt:
            print("\n-----Conversation forcefully ended-----")
            return

        else:    
            if user_message.lower() == 'q':
                print("\n-----Conversation ended-----")
                return
                
            messages.append(create_message("user", user_message))

        try:
            res = client.responses.create(
                model="gpt-4o-mini",
                input=messages,
                instructions="You are a helpful assistant that answers briefly"
            )

        except APIConnectionError:
            print("Error: Couldn't connect to the API.")
            return

        except RateLimitError:
            print("Error: Account quota exceeded.")
            return

        except Exception as e:
            print(f"Unexpected error: {e}")
            return
        
        else:
            ai_response = res.output_text

            print(f"\nAssistant: {ai_response}")
            
            messages.append(create_message("assistant", ai_response))

def create_message(role, message):
    return {"role": role, "content": message}

if __name__ == "__main__":
    main()