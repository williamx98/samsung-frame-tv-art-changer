#!/usr/bin/with-contenv bashio

TVIP=$(bashio::config 'tv')
URL=$(bashio::config 'wallhaven_url')

mkdir -p /media/frame
echo "Using ${TVIP} as the IP's of the Samsung Frame"

PARAMS=""

if bashio::config.true 'google_art'; then
    PARAMS="${PARAMS} --google-art"
fi
if bashio::config.true 'wallhaven_wallpapers'; then
    PARAMS="${PARAMS} --wallhaven-wallpapers"
fi
if bashio::config.true 'media_folder'; then
    PARAMS="${PARAMS} --media-folder"
fi
if bashio::config.true 'download_high_res'; then
    PARAMS="${PARAMS} --download-high-res"
fi
if bashio::config.true 'same_image'; then
    PARAMS="${PARAMS} --same-image"
fi

python3 art.py --tvip ${TVIP} ${PARAMS} --wallhavenURL ${URL}

echo "done, closing now!"
kill -s SIGHUP 1
