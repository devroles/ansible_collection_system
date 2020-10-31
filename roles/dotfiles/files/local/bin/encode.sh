#!/bin/bash
#mencoder "$1" -quiet -fps 2997/100 -ofps 2997/50 -of lavf \
#	-lavfopts format=avi -oac faac -faacopts mpeg=4:object=2:quality=80:raw \
#	-channels 2 -srate 48000 -ovc x264 -x264encopts \
#	crf=27:keyint=300:keyint_min=30:level_idc=41:frameref=3:mixed_refs:bframes=3:b_adapt=2:nob_pyramid:weight_b:me_range=24:psy_rd=0.5,0.2:direct_pred=spatial:partitions=p8x8,b8x8,i4x4:deblock:chroma_me:cabac:8x8dct:me=hex:subq=7:trellis=1:nr=1000:threads=auto:nointerlaced:nopsnr:nossim:nofast_pskip:nodct_decimate:aud \
#	-vf yadif=3:1,framestep=2,scale=-2:480,dsize=-2:480 -o "$2"
#ffmpeg -i "$1" \
#	-vcodec libx264 -sameq \
#	-acodec aac \
#	 -threads:0 10 -threads:1 2 \
#	"$2"
#
#	-vpre hq \

set -x

if [ -n "${3}" ]; then
    FORMAT="${3}"
else
    FORMAT=libx265
fi

ffmpeg -i "$1" \
	-vcodec ${FORMAT} -level 41 \
	-crf 24 \
	-threads 0 \
	-acodec aac \
	-ab 256k \
	-ac 2 \
	-ar 48000 \
	-strict -2 \
	"$2"
