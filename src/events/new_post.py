from groof import events

from assets import kbs

photo = events.photo()
animation = events.animation()
choice_channel = events.button(kbs.Channels.channel, state='NewPost')
choice_publication_time = events.text(state='NewPost:publication_time')
choice_publication_time_now = events.button(kbs.PublicationTime.now, state='NewPost:publication_time')
