from ollama import ChatResponse, chat

class ChatPOVGenerator:

    def __init__(self, model: str, system_prompt: str) -> None:
        self.model = model
        self.system_prompt = system_prompt

    def generate_pov_from_text(self, raw_text: str) -> str:
        try:
            response: ChatResponse = chat(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": self.system_prompt,
                    },
                    {
                        "role": "user",
                        "content": f"Generate an engaging one minute audio clip length POV style narration from the following story:\n\n{raw_text}. Your task is to listen to stories and then generate a point of view (POV) like narration of a provided story, long enough to fill a 1 minute long audio clip. Make it as stretched out and exaggerated as possible, but don't make it too poetic or corny, make it engaging and attention capturing. Your narration style is very catchy and engaging, and you always end with a cliffhanger to keep the audience hooked till the end. You are very good at creating vivid imagery and emotional connections with the audience through your narration. Assume that there is only one narrator and no need to specify who is speaking. Generate it like a story, not a play. Avoid scene setting cues in brackets and parenthesis and keep it narration only, show the world through the users narrations. This won't be read but narrated like a monologue keep that in mind. If story is not found output 'NULL' ",
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