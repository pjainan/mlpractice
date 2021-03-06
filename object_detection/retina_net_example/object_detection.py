from imageai.Detection import ObjectDetection
import os

path = os.getcwd()
detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath(os.path.join(path,'resnet50_coco_best_v2.0.1.h5'))
detector.loadModel()

custom_objects = detector.CustomObjects(person=True, car=True)

detections = detector.detectCustomObjectsFromImage(input_image=os.path.join(path,'sample_image.png'),output_image_path=os.path.join(path,'new_image.png'), custom_objects=custom_objects, minimum_percentage_probability=65)

for eachObject in detections:
   print(eachObject)
   print("--------------------------------")

