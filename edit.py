import moviepy
import start

st = start.Start()

class Editor:

    def __init__(self, topic):
        self.topic = st.return_topic()
    
    def get_folder(self):
        path = 'Pictures/' + self.topic 
        return path
