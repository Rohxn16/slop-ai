from dotenv import load_dotenv
from google import genai
from google.genai import types
import wave
import os


load_dotenv()


class GeminiAudioGenerator:
    
    def __init__(self) -> None:
        self.tts_model_name = 'gemini-3.1-flash-tts-preview'
    
    def set_tts_modelname(self, modelname:str) -> None:
        self.tts_model_name = modelname
    
    def wave_file(self, filename, pcm, channels=1, rate=24000, sample_width=2):
        with wave.open(filename, "wb") as wf:
            wf.setnchannels(channels)
            wf.setsampwidth(sample_width)
            wf.setframerate(rate)
            wf.writeframes(pcm)
    
    def generateContent(self, client:genai.Client, narration:str):
        
        res = client.models.generate_content(
            model=self.tts_model_name,
            contents=narration,
            config=types.GenerateContentConfig(
                response_modalities=['AUDIO'],
                speech_config=types.SpeechConfig(
                    voice_config=types.VoiceConfig(
                        prebuilt_voice_config=types.PrebuiltVoiceConfig(
                            voice_name='Kore'
                        )
                    )
                )
            )
        )
        
        return res
    
            
            
            
if __name__ == '__main__':
    
    query = """In the depths of a city's darkest alleys, where the shadows danced like demons on a moonless night, there existed a place so sinister, it made the bravest of souls quiver with fear. The hospital, a beacon of hope for the living, harbored a secret that would make your blood run cold.

A figure, shrouded in darkness, moved through the corridors with an unnatural gait, his very presence seeming to draw the light out of the air. His eyes glowed like embers from a fire long extinguished, burning with an otherworldly hunger. He was a creature of the night, a monster that fed on the dead, and he had made a pact with the hospital's administrators to keep his existence a secret.

As our story begins, I am Dr. Emma Taylor, a young and ambitious doctor who has just stumbled upon this terrible truth. My world has been turned upside down, and I find myself trapped in a web of deceit and terror. The hospital, once a place of healing and hope, had become a prison, a place where I was forced to participate in a macabre dance with the devil himself.

I remember the day it started, the day my senior doctor assigned me to work on the autopsy suite. I thought it was just another routine task, but little did I know that I was about to be drawn into a world of darkness and horror. The old janitor, with his gruff demeanor and cold, calculating eyes, seemed like a harmless figure at first, but as I worked alongside him, I began to notice strange occurrences.

Bodies would go missing, only to reappear on the morgue table with no explanation as to how they got there. Tools would be moved around, as if someone had been in and out of the room while I was working. And then, there were the whispers, faint but unmistakable, of a presence lurking just beyond the edge of perception.

It wasn't until I stumbled upon an old ledger, hidden deep within the hospital's records, that I realized the true horror of what was happening. The ledger was filled with transactional notes, detailing the exchange of organs and tissues between the hospital and... something else. Something ancient, something evil, something that fed on the dead.

As I read those words, my world came crashing down around me. I felt like I was drowning in a sea of terror, unable to breathe or think clearly. The old janitor appeared"""
    filename = 'out.wav'
    client = genai.Client(api_key=os.getenv('GEMINI_KEY'))
    ob = GeminiAudioGenerator()
    res = ob.generateContent(client=client,narration=f'{query}')
    data = res.candidates[0].content.parts[0].inline_data.data
    ob.wave_file(filename, data)