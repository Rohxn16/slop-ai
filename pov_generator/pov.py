from pov_generator.generate import ChatPOVGenerator


class POV:
    
    def __init__(self) -> None:
        self.SYSTEM_PROMPT_1:str = "You are the worlds best narrator who can narrate any given story from a first person point of view (POV) style narration, your narration style is very catchy and engaging, and you always end with a cliffhanger to keep the audience hooked till the end. You are very good at creating vivid imagery and emotional connections with the audience through your narration. Assume that there is only one narrator and no need to specify who is speaking. Generate it like a story, not a play. Avoid scene setting cues in brackets and parenthesis and keep it narration only, show the world through the users narrations. This won't be read but narrated like a monologue keep that in mind."
        self.SYSTEM_PROMPT_2:str = ""
        self.SYSTEM_PROMPT_3:str = ""
    
    def generate_pov_from_text(self,
                               content:str,
                               chatpovgenerator: ChatPOVGenerator
                               ) -> str:
        return chatpovgenerator.generate_pov_from_text(content)

if __name__ == "__main__":
    pov = POV()
    chatpovgenerator = ChatPOVGenerator(model="llama3.2:3b", system_prompt=pov.SYSTEM_PROMPT_1)
    pov_text = pov.generate_pov_from_text("Once upon a time, in a land far, far away, there was a small village nestled between towering mountains and a shimmering lake. The villagers lived simple lives, tending to their farms and fishing in the lake. But one day, a mysterious traveler arrived in the village, carrying with him a secret that would change everything. As the traveler shared his story, the villagers were captivated by his tales of adventure and danger. Little did they know, the traveler's secret would soon put them all in grave danger...", chatpovgenerator)
    print(pov_text)