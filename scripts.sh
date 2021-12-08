./darknet detector test cfg/yolov4-obj.data cfg/yolov4-obj.cfg yolov4-obj.weights /Users/Adrian/code/TDT17/data/YOLO_format/all_data/data/intensity_video_17_frame_000010.PNG ext_output < data/test.txt > result.txt


./darknet detector map data/YOLO_format/intensity_data/yolov4-obj.data cfg/yolov4-obj.cfg yolov4-obj.weights > result.txt


./darknet detector test data/YOLO_format/intensity_data/yolov4-obj.data  cfg/yolov4-obj.cfg yolov4-obj.weight -dont_show -ext_output < data/train.txt > result.txt