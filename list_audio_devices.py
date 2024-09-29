import sounddevice

def list_audio_devices():
    devices = sounddevice.query_devices()
    for item, device in enumerate(devices):
        print(f"Device {item}: {device['name']}")

if __name__ == "__main__":
    list_audio_devices()
