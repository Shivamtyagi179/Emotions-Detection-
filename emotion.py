import cv2
import numpy as np

# Simple face detection without cascade files
cap = cv2.VideoCapture(0)

print("🎭 EMOTION DETECTOR START! Smile/Frown karo - Press 'q' to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Camera issue!")
        break
    
    # Simple face region (upper center of frame)
    h, w = frame.shape[:2]
    face_region = frame[int(h*0.2):int(h*0.6), int(w*0.3):int(w*0.7)]
    
    if face_region.size > 0:
        # Mouth area analysis (lower part of face region)
        fh, fw = face_region.shape[:2]
        mouth_area = face_region[int(fh*0.6):, int(fw*0.2):int(fw*0.8)]
        
        if mouth_area.size > 0:
            # Analyze brightness for emotion
            mouth_bright = np.mean(mouth_area)
            face_bright = np.mean(face_region)
            
            if mouth_bright > face_bright + 20:
                emotion = "😊 HAPPY"
                color = (0, 255, 0)
            elif mouth_bright < face_bright - 20:
                emotion = "😢 SAD"
                color = (0, 0, 255)
            else:
                emotion = "😐 NEUTRAL"
                color = (0, 255, 255)
            
            # Draw face rectangle
            cv2.rectangle(frame, (int(w*0.3), int(h*0.2)), 
                         (int(w*0.7), int(h*0.6)), color, 4)
            cv2.putText(frame, emotion, (int(w*0.35), int(h*0.15)), 
                       cv2.FONT_HERSHEY_SIMPLEX, 1.5, color, 3)
        else:
            cv2.putText(frame, "📹 Face camera properly", (50, 50), 
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    
    # Instructions
    cv2.putText(frame, "EMOTION DETECTOR v1.0 - Press Q to Quit", (10, h-20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    
    cv2.imshow('Emotion Detector', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("✅ PROJECT 100% COMPLETE! 🎉")
