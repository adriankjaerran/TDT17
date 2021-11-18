cd darknet
for file in ../data/YOLO_format/intensity_data/data/*.PNG; do
    stem_ext=${file##*/data/}
    stem=${stem_ext%%.PNG}
    echo $stem.jpg
    # "${var##*/}"
    # export file_stem="$file | awk -F'[_.]' '{print ${NF-1}}'"
    # export lalala=$file | awk -F'[_.]' '{print $(NF-1)}'
    ./darknet detect cfg/yolov3-tiny.cfg yolov3-tiny.weights $file
    mv ./predictions.jpg ../exports_test_self_trained/$stem.jpg
done
cd ..

