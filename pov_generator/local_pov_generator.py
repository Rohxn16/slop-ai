from ollama import chat, ChatResponse

SYSTEM_PROMPT = "Your task is to listen to stories and then generate a point of view (POV) like narration of a provided story, long enough to fill a 1 minute long audio clip. Your narration style is very catchy and engaging, and you always end with a cliffhanger to keep the audience hooked till the end. You are very good at creating vivid imagery and emotional connections with the audience through your narration."

MODEL = 'artifish/llama3.2-uncensored:latest'

def read_raw_text_from_file(filepath: str) -> str:
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return ""


def write_pov_to_file(filepath: str, pov: str) -> None:
    try:
        with open(filepath, "w") as file:
            # Remove consecutive newlines
            cleaned_pov = "\n".join(line for line in pov.split("\n") if line.strip())
            file.writelines(cleaned_pov)
    except Exception as e:
        print(f"Error writing to file: {e}")


def generate_pov_from_text(raw_text: str) -> str:
    try:
        response: ChatResponse = chat(
            model=MODEL,
            messages=[
                # {
                #     "role": "system",
                #     "content": SYSTEM_PROMPT,
                # },
                {
                    "role": "user",
                    "content": f"Generate an enaging one minute audio clip length POV style narration from the following story:\n\n{raw_text}. Your task is to listen to stories and then generate a point of view (POV) like narration of a provided story, long enough to fill a 1 minute long audio clip. Make it as stretched out and exaggarated as possible, but dont make it too poetic or corny, make it engaging and attention capturing. Your narration style is very catchy and engaging, and you always end with a cliffhanger to keep the audience hooked till the end. You are very good at creating vivid imagery and emotional connections with the audience through your narration. Assume that there is only one narrator and no need to specify who is speaking. Generate it like a story, not a play. Avoid scene setting cues in brackets and parenthesis and keep it narration only, show the world through the users narrations. This won't be read but narrated like a monologue keep that in mind. If story is not found output 'NULL' ",
                },
            ],
            stream=False,
            options={
                "num_predict": 500,
                "temperature": 0.7,
                "top_p": 0.9,
            },
        )
        if response.message and response.message.content:
            return response.message.content.strip()
        return ""
    except Exception as e:
        print(f"Error generating POV: {e}")
        return ""
