cd darknet
for file in ../data/YOLO_format/range_data/data/*.PNG; do
    stem_ext=${file##*/data/}
    stem=${stem_ext%%.PNG}
    echo $stem.jpg
    # "${var##*/}"
    # export file_stem="$file | awk -F'[_.]' '{print ${NF-1}}'"
    # export lalala=$file | awk -F'[_.]' '{print $(NF-1)}'
    ./darknet detector test cfg/yolov4-obj.data cfg/yolov4-obj.cfg yolov4-obj.weights $file -tresh 0.1
    mv ./predictions.jpg ../videos/range_23_11/$stem.jpg


done
cd ..

