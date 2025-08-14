from ultralytics import YOLO

model = YOLO('models/best.pt') #v8x is largest model for highest accuracy but high cpu and ram usage
# keypoints detecs joints
# boxes is boxes
# names, 0 = person

results = model.predict('input_videos/08fd33_4.mp4', save=True)
print(results[0])
print("=================================")
for box in results[0].boxes:
    print(box)
