# EyeTrackingEmotionDetectionBlinkCounterSleepMonitoring

Este repositorio contiene un sistema de seguimiento de ojos, detección de emociones, conteo de parpadeos y monitoreo de micro sueños desarrollado en Python para la plataforma de Mindware ROS2 Foxy.

## Dependencias

Asegúrate de tener instaladas las siguientes dependencias antes de ejecutar el código:

- [MediaPipe](https://google.github.io/mediapipe/): Utilizado para el seguimiento de puntos de interés, incluyendo ojos, cejas y boca.
- [FaceMesh](https://google.github.io/mediapipe/solutions/face_mesh.html): Empleado para el seguimiento detallado de la estructura facial.
- [OpenCV](https://opencv.org/): Biblioteca de visión por computadora para procesamiento de imágenes.
- [NumPy](https://numpy.org/): Biblioteca para operaciones matemáticas en Python.
- [CvBridge](https://github.com/ros-perception/vision_opencv): Puente entre OpenCV y ROS para facilitar el intercambio de datos de imágenes.

Puedes instalar estas dependencias utilizando pip:

```bash
pip install mediapipe opencv-python numpy
```

Asegúrate de tener instalado Python en tu entorno y todas las dependencias mencionadas anteriormente.
Configuración de ROS2 Foxy

Este proyecto está diseñado para funcionar con la plataforma Mindware ROS2 Foxy. Asegúrate de tener ROS2 Foxy instalado y configurado en tu entorno antes de ejecutar el código.
Contribuciones

¡Contribuciones son bienvenidas! Si encuentras algún problema o tienes ideas para mejorar el sistema, por favor crea un issue o envía una *pull request.
