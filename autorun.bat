cd scripts/
python youtube_m3ugrabber.py > ../youtube.m3u

cd ..
git add .
git commit -m "updated link"
git push