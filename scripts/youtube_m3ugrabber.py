#! /usr/bin/python3

banner = r'''
#EXTM3U x-tvg-url="https://weareblahs.github.io/epg/mytv.xml" url-tvg="https://weareblahs.github.io/epg/compressed/mytv.xml.gz" refresh="1440" max-conn="1" refresh="24"

#EXTINF:-1 group-title="myFreeview: TV" ch-number="101" tvg-id="101" tvg-chno="101" tvg-logo="https://astrocontent.s3.amazonaws.com/Images/ChannelLogo/Neg/101.png",TV1
https://d25tgymtnqzu8s.cloudfront.net/smil:tv1/chunklist_b4596000_slENG.m3u8

#EXTINF:-1 group-title="myFreeview: TV" ch-number="102" tvg-id="102" tvg-chno="102" tvg-logo="https://astrocontent.s3.amazonaws.com/Images/ChannelLogo/Neg/102.png",TV2
https://d25tgymtnqzu8s.cloudfront.net/smil:tv2/chunklist_b4596000_slENG.m3u8

#EXTINF:-1 group-title="myFreeview: TV" ch-number="108" tvg-id="108" tvg-chno="108" tvg-logo="https://astrocontent.s3.amazonaws.com/Images/ChannelLogo/Neg/148.png",8TV'''

remaining = r'''
#EXTINF:-1 group-title="myFreeview: TV" ch-number="110" tvg-id="110" tvg-chno="110" tvg-logo="https://astrocontent.s3.amazonaws.com/Images/ChannelLogo/Neg/146.png",OKEY
https://d25tgymtnqzu8s.cloudfront.net/smil:okey/chunklist_b4596000_slENG.m3u8

#EXTINF:-1 group-title="myFreeview: TV" ch-number="111" tvg-id="111" tvg-chno="111" tvg-logo="https://i.ibb.co/JcTZMLX/image.png",Sukan RTM
https://d25tgymtnqzu8s.cloudfront.net/smil:sukan/chunklist_b4596000_slENG.m3u8

#EXTINF:-1 group-title="myFreeview: TV" ch-number="113" tvg-id="113" tvg-chno="113" tvg-logo="https://i.ibb.co/vHcWdsP/image.png",TV6
https://d25tgymtnqzu8s.cloudfront.net/smil:tv6/chunklist_b4596000_slENG.m3u8

#EXTINF:-1 group-title="myFreeview: TV" ch-number="114" tvg-id="114" tvg-chno="114" tvg-logo="https://astrocontent.s3.amazonaws.com/Images/ChannelLogo/Neg/114.png",TV Alhijrah
https://172048-castr.akamaized.net/61e0e9a88ecf869e0a595bfa/live_7284c6607dcb11ec8005ad1f1e0e9f60/index.m3u8

#EXTINF:-1 group-title="myFreeview: TV" ch-number="116" tvg-id="116" tvg-chno="116" tvg-logo="https://static.wikia.nocookie.net/logopedia/images/e/eb/SUKE_TV_Logo.png/revision/latest/scale-to-width-down/300",Suke TV
http://free.fullspeed.tv/iptv-query?streaming-ip=https://www.youtube.com/channel/UCzh6SMSWad2934rgoq_cNkg/live

#EXTINF:-1 group-title="myFreeview: TV" ch-number="122" tvg-id="122" tvg-chno="122" tvg-logo="https://astrocontent.s3.amazonaws.com/Images/ChannelLogo/Neg/122.png",TVS
https://v-t-e-r.github.io/Umbrella/Playlist/Ch/TVSwak.m3u8

#EXTINF:-1 group-title="myFreeview: TV" ch-number="123" tvg-id="123" tvg-chno="123" tvg-logo="https://berita.rtm.gov.my/images/logobes.jpg",Berita RTM
https://d25tgymtnqzu8s.cloudfront.net/smil:berita/chunklist_b4596000_slENG.m3u8

#EXTINF:-1 group-title="myFreeview: TV" ch-number="128" tvg-id="128" tvg-chno="128" tvg-logo="https://www.channelnewsasia.com/sites/default/themes/mc_cna_theme/images/logo.png",CNA
https://mediacorp-videosbclive.akamaized.net/dd724cfb0e8e4cdc921bbc4ac94614bf/ap-southeast-1/6057994443001/profile_2/chunklist.m3u8
'''

import requests
import os
import sys
import json

windows = False
if 'win' in sys.platform:
    windows = True

def grab(url):
    response = requests.get(url, timeout=15).text
    if '.m3u8' not in response:
        #response = requests.get(url).text
        if '.m3u8' not in response:
            if windows:
                print('https://raw.githubusercontent.com/benmoose39/YouTube_to_m3u/main/assets/moose_na.m3u')
                return
            #os.system(f'wget {url} -O temp.txt')
            os.system(f'curl "{url}" > temp.txt')
            response = ''.join(open('temp.txt').readlines())
            if '.m3u8' not in response:
                print('https://raw.githubusercontent.com/benmoose39/YouTube_to_m3u/main/assets/moose_na.m3u')
                return
    end = response.find('.m3u8') + 5
    tuner = 100
    while True:
        if 'https://' in response[end-tuner : end]:
            link = response[end-tuner : end]
            start = link.find('https://')
            end = link.find('.m3u8') + 5
            break
        else:
            tuner += 5
    
    pl_link = link[start : end]
    playlist = requests.get(pl_link, timeout=15).text
    start2 = playlist.rfind('https')

    print(playlist[start2:len(playlist) - 1])

print('#EXTM3U x-tvg-url="https://github.com/botallen/epg/releases/download/latest/epg.xml"')
print(banner)
#s = requests.Session()
with open('../youtube_channel_info.txt') as f:
    req_header={
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhaWQiOiJmMWEzNjJkMjg4YzFiOTgwOTljNyIsInJvbCI6ImNhbi1tYW5hZ2UtcGFydG5lcnMtcmVwb3J0cyBjYW4tcmVhZC12aWRlby1zdHJlYW1zIGNhbi1zcG9vZi1jb3VudHJ5IGNhbi1hZG9wdC11c2VycyBjYW4tcmVhZC1jbGFpbS1ydWxlcyBjYW4tbWFuYWdlLWNsYWltLXJ1bGVzIGNhbi1tYW5hZ2UtdXNlci1hbmFseXRpY3MgY2FuLXJlYWQtbXktdmlkZW8tc3RyZWFtcyBjYW4tZG93bmxvYWQtbXktdmlkZW9zIGFjdC1hcyBhbGxzY29wZXMgYWNjb3VudC1jcmVhdG9yIGNhbi1yZWFkLWFwcGxpY2F0aW9ucyIsInNjbyI6Im1hbmFnZV9zdWJzY3JpcHRpb25zIG1hbmFnZV92aWRlb3MgdXNlcmluZm8iLCJsdG8iOiJabnA0Y3lVSmRIdDlieGNJRGd3T0IzYzVMUTRpSVNGaUZBSlJCQSIsImFpbiI6MSwiYWRnIjoxLCJpYXQiOjE2NjgzOTkwMjgsImV4cCI6MTY2ODQzNDgyMCwiZG12IjoiMSIsImF0cCI6ImJyb3dzZXIiLCJhZGEiOiJ3d3cuZGFpbHltb3Rpb24uY29tIiwidmlkIjoiRjE5Qjg1MjA5RTMxQjMxMjZENjU4NzRCM0NGNEEwOUIiLCJmdHMiOjUwMjcwMiwiY2FkIjoyLCJjeHAiOjIsImNhdSI6Miwia2lkIjoiQUY4NDlERDczQTU4NjNDRDdEOTdEMEJBQjA3MjI0M0IifQ.HCyvVufQKRb5pLUiowbmZ5tALPMocF3PMm6xVlQJAqs',
    }
    
    response = requests.get('https://www.dailymotion.com/player/metadata/video/kdFzSYy1bHxrForBrar?embedder=https://www.xtra.com.my/&syndication=273888&locale=en-US&dmV1st=F19B85209E31B3126D65874B3CF4A09B&dmTs=502702&is_native_app=0', headers=req_header).text
    data = json.loads(response)

    # print (data)

    pl_link = data['qualities']['auto'][0]['url']
    playlist = requests.get(pl_link, timeout=15).text
    start2 = playlist.rfind('https')
    print(playlist[start2:len(playlist) - 1])
    print(remaining)

    for line in f:
        line = line.strip()
        if not line or line.startswith('~~'):
            continue
        if not line.startswith('https:'):
            line = line.split('|')
            ch_name = line[0].strip()
            grp_title = line[1].strip()
            tvg_logo = line[2].strip()
            tvg_id = line[3].strip()
            print(f'\n#EXTINF:-1 group-title="{grp_title}" tvg-logo="{tvg_logo}" tvg-id="{tvg_id}", {ch_name}')
        else:
            grab(line)
            
if 'temp.txt' in os.listdir():
    os.system('rm temp.txt')
    os.system('rm watch*')
