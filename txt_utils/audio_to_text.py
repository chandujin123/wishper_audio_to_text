import whisper
MODEL_NAME = "tiny"
class Text2Audio:
    model = whisper.load_model(MODEL_NAME)
    def __init__(self,file_name) -> None:
        self.file_name = file_name
    def transulate(self):
        result = self.model.transcribe(self.file_name)
        return result["text"]