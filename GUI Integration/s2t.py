import transcribe
import record

def speechToTextFn():

    record.recordFn()
    return transcribe.transcribeFn()

