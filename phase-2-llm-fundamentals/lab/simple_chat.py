import os
from dotenv import load_dotenv
from  openai import OpenAI, APIConnectionError, RateLimitError

def main():
    load_dotenv()

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    try:
        print("-----Sending request to OpenAI-----")

        response = client.responses.create(
            model="gpt-4o-mini",
            input="Explain what an API is to a 5 year old"
        )
    
    except APIConnectionError:
        print("Error: Couldn't connect to the API.")

    except RateLimitError:
        print("Error: Account quota excedeed")

    except Exception as e:
        print(f"Unexpected exception: {e}")

    else:
        print("\n-----AI response-----")
        print(response.output_text)
if __name__ == "__main__": 
    main()