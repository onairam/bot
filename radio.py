from mplayer import Player, CommandPrefix

#import mplayer
# Set default prefix for all Player instances
Player.cmd_prefix = CommandPrefix.PAUSING_KEEP
#print(path)

#Player.path ="/usr/bin/mplayer"

#Since autospawn is True by default, no need to call player.spawn() manually
player = Player()

# Play a file
#player.loadfile('http://retransmisorasenelpais.cienradios.com.ar:8000/la100.aac')
player.loadfile('audio.mp3')

# Pause playback
#player.pause()

# Get title from metadata
##metadata = player.metadata or {}
##print metadata.get('Title', '')

# Print the filename
##print player.filename

# Seek +5 seconds
##player.time_pos += 5

# Set to fullscreen
##player.fullscreen = True

# Terminate MPlayer
##player.quit()