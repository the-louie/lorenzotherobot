from src.lib.twitch import *
import globals

def uptime():
    usage = "!uptime"
    
    uptime = get_stream_uptime()
    channel = globals.channel
    
    if get_stream_status():
        
        return "The current !uptime is EXACTLY " + str(uptime)
    else:
        return "She's offline, ya dingus ;)"