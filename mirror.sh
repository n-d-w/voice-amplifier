#!/bin/bash

PREFIX_URL="https://hlasyagresora.eu"
DATA="osoby kategorie"
user_agent="User-agent: Voice Amplifier"

for dt in $DATA; do
	curl -X GET --silent -H "$user_agent" $PREFIX_URL/api/$dt.php \
		| jq --sort-keys . > hlasyagresora.eu/$dt.json
done

FOTOS=$( jq -r '.[].foto' hlasyagresora.eu/osoby.json )
for foto in $FOTOS; do
	if [[ "$foto" =~ ^[a-zA-Z0-9._-]+$ ]]; then
		echo "Image: '$foto'"
		if [ ! -f docs/images/$foto ]; then
			curl -X GET --silent -H "$user_agent" $PREFIX_URL/uploads/$foto > docs/images/$foto
		fi
	else
		echo "Invalid image: 'foto'"
	fi
done
	
