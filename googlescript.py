#!/usr/bin/env python

# Received from 2016 Google Inc.

def run_quickstart():
    # [START google_speech]
    import io
    import os

    # Imports the Google Cloud client library
    # [START speech_python_migration_imports]
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    # [END speech_python_migration_imports]

    # Instantiates a client
    # [START speech_python_migration_client]
    client = speech.SpeechClient()
    # [END speech_python_migration_client]

    # The name of the audio file to transcribe
    file_name = '/Users/princescadorsaint/Environments/File.wav'
      
    # Loads the audio into memory
    with io.open(file_name, 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)

    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code='en-US',
        speech_contexts=[speech.types.SpeechContext(
        	phrases=[],)])
    # Detects speech in the audio file
    response = client.recognize(config, audio)

    for result in response.results:
        print('Transcript: {}'.format(result.alternatives[0].transcript))
    # [END google_speech]


if __name__ == '__main__':
    run_quickstart()
