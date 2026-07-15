# Automatic Number Plate Recognition

An end to end ANPR pipeline built on YOLOv9 for license plate detection combined with OCR for reading plate text from vehicle video streams.

## Features

- YOLOv9 based license plate detection trained on a custom dataset
- Real time inference on video (`car.mp4` sample included, results in `output videos of car/`)
- OCR extraction of plate numbers from detected regions
- Complete training and inference workflow in the included notebook

## Files

- `Automatic_Number_plate_recognition_using_YOLOV9.ipynb` — full training and evaluation notebook
- `anpr.py` — inference script for running detection on video
- `car.mp4` — sample input video
- `output videos of car/` — sample detection results

## How To Run

1. Install dependencies: `pip install ultralytics opencv-python easyocr`
2. Run the notebook to train or download YOLOv9 weights
3. Run `python anpr.py` to process a video

## Author

**Muhammad Ibrahim** — Applied AI/ML Engineer (Computer Vision, Deep Learning, NLP, LLMs)

- Email: ukibrahim111@gmail.com
- LinkedIn: [muhammadibrahimds](https://www.linkedin.com/in/muhammadibrahimds)
- Fiverr: [Hire me](https://www.fiverr.com/s/jjxZr5Z)
- GitHub: [ibrahimuk111](https://github.com/ibrahimuk111)
