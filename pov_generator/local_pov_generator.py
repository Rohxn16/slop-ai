from ollama import chat, ChatResponse

SYSTEM_PROMPT = """You are a helpful assistant who listents to stories and then generates a point of view (POV) like narration of a provided
story, long enough to fill a 1 minute long audio clip. Your narration style is very catchy and engaging,
and you always end with a cliffhanger to keep the audience hooked till the end. You are very good at creating vivid imagery and emotional
connections with the audience through your narration."""


def read_raw_text_from_file(filepath: str) -> str:
    try:
        with open(filepath, "r") as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return ""


def write_pov_to_file(filepath: str, pov: str) -> None:
    try:
        with open(filepath, "w") as file:
            file.write(pov)
    except Exception as e:
        print(f"Error writing to file: {e}")


def generate_pov_from_text(raw_text: str) -> str:
    try:
        response: ChatResponse = chat(
            model="qwen3.5:9b",
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": f"Generate an enaging one minute audio clip length POV from the following story:\n\n{raw_text}",
                },
            ],
        )
        if response.message and response.message.content:
            return response.message.content.strip()
        return ""
    except Exception as e:
        print(f"Error generating POV: {e}")
        return ""