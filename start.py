import research as rs
import edit
import upload as up

class Start:

    def __init__(self, topic=rs.query):
        self.topic = topic
    
    def return_topic(self):
        return self.topic

# run start
if __name__ == "__main__":
    edit = edit.Editor()
    st = Start(rs.query)
    edit.open_json()
    edit.path_array()
    edit.edit_clip_img()
    edit.concatenate()
    up.upload_me()
