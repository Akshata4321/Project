import torch
from yolov5 import detect

def run_car_crash_detection(image_path):
    print(f"Running car crash detection on: {image_path}")
    
    detect.run(
        weights='yolov5s.pt',
        source=image_path,
        conf_thres=0.4,
        classes=[2, 5, 7],
        save_txt=True,
        save_conf=True,
        save_crop=True
    )

if __name__ == "__main__":
    # Use raw string or forward slashes
    image_path = video_path = 'C:\\Users\\padti\\OneDrive\\Desktop\\yolo_car_fall_project\\video\\carcrash.jpg'
    run_car_crash_detection(image_path)
