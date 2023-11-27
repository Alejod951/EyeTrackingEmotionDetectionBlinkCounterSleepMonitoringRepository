from setuptools import setup

package_name = 'EyeTrackingEmotionDetectionBlinkCounterSleepMonitoringRepository'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='alejo',
    maintainer_email='alejo@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'img_publi = EyeTrackingEmotionDetectionBlinkCounterSleepMonitoringRepository.img_publisher:main',
            'img_microdreams = EyeTrackingEmotionDetectionBlinkCounterSleepMonitoringRepository.img_microdreams:main',
            'img_emo = EyeTrackingEmotionDetectionBlinkCounterSleepMonitoringRepository.img_emotion:main',
            'img_tracking = EyeTrackingEmotionDetectionBlinkCounterSleepMonitoringRepository.img_eyes_tracking:main',
            'img_displa = EyeTrackingEmotionDetectionBlinkCounterSleepMonitoringRepository.img_display:main',
        ],
    },
)
