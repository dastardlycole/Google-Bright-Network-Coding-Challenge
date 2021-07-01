"""A video player class."""

from .video_library import VideoLibrary

isplayin=1
t=0
paused=0
class VideoPlayer:
    """A class used to represent a Video Player."""
    def __init__(self):
        self._video_library = VideoLibrary()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        show_videos = self._video_library.get_all_videos()
        print("Here's a list of all available videos: ")
        listy=[]
        for i in show_videos:
            title_vid= i.title
            id_vid= i.video_id
            tags_vid=i.tags
            if not tags_vid:
                tags_vid= '' 
                listy.append(f"\t{title_vid} ({id_vid}) [{tags_vid}] ")
            else:    
                listy.append(f"\t{title_vid} ({id_vid}) [{tags_vid[0]} {tags_vid[1]}] ")
        
        first = listy.pop(0)  
        listy.insert(2, first) 
        for item in listy:
            print(item)   
         
        """Returns all videos."""

     
    def play_video(self, video_id):
        play_videos = self._video_library.get_all_videos()
        diction={}
        for i in play_videos:
            title_vid= i.title
            id_vid= i.video_id
            diction[id_vid] = title_vid
        if video_id in diction:    
            global isplayin  
            global t  
            global paused
            if isplayin==0:        
                print(f"Stopping video: {t}")
                isplayin=1
            print(f"Playing video: {diction[video_id]}")
            t=diction[video_id]
            isplayin=0    
            paused=0  
        else: 
            print('Cannot play video: Video does not exist')    
            
        
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
       

    def stop_video(self):
        """Stops the current video."""
        global isplayin  
        global t    
        global paused
        if isplayin==0:        
                print(f"Stopping video: {t}")
                isplayin=1  
                paused=0  
        else:
            print('Cannot stop video: No video is currently playing')                

    def play_random_video(self):
        """Plays a random video from the video library."""
        import random
        play_videos = self._video_library.get_all_videos()
        diction={}
        for i in play_videos:
            title_vid= i.title
            id_vid= i.video_id
            diction[id_vid] = title_vid
        val_list=list(diction.values())    
        val = random.choice(val_list)
        global isplayin  
        global t  
        global paused
        if diction == '':
            print('No videos available')
        else:      
            if isplayin==0:        
                    print(f"Stopping video: {t}")
                    isplayin=1  
            print(f"Playing video: {val}")
            t=val
            isplayin=0  
            paused=0  

     

    def pause_video(self):
        """Pauses the current video."""
        global isplayin  
        global t    
        global paused
        if isplayin==0:
            if paused==1:
                print(f'Video already paused: {t}') 
            else:           
                print(f"Pausing video: {t}")
                paused=1  
        else:
            print('Cannot pause video: No video is currently playing')    

    def continue_video(self):
        """Resumes playing the current video."""
        global isplayin  
        global t    
        global paused
        if isplayin==0:
            if paused==1:
                print(f'Continuing video: {t}') 
                paused=0
            else:           
                print(f"Cannot continuue video: Video is not paused")  
        else:
            print('Cannot continue video: No video is currently playing')    


    def show_playing(self):
        """Displays video currently playing."""
        global isplayin  
        global t    
        global paused
        play_videos = self._video_library.get_all_videos()
        listy=[]
        for i in play_videos:
            title_vid= i.title
            id_vid= i.video_id
            tags_vid=i.tags
            if not tags_vid:
                tags_vid= '' 
                listy.append(f"{title_vid} ({id_vid}) [{tags_vid}] ")
            else:    
                listy.append(f"{title_vid} ({id_vid}) [{tags_vid[0]} {tags_vid[1]}] ")

        first = listy.pop(0)  
        listy.insert(2, first) 
        for item in listy:
            if t in item:
                if isplayin==0:
                    if paused==0:
                        print(f'Currently playing: {item}')           
                    else:
                        print(f'Currently playing: {item}- PAUSED')
                else:
                    print('No video is currently playing')
    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
