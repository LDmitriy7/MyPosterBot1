from groof import on

from assets import kbs

photo = on.photo()
animation = on.animation()
choice_channel = on.button(kbs.Channels.channel, state='NewPost')
choice_publication_time = on.text(state='NewPost:publication_time')
choice_publication_time_now = on.button(kbs.PublicationTime.now, state='NewPost:publication_time')
