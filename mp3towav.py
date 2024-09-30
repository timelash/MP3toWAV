import argparse
import os
from pydub import AudioSegment

def main(src):
    # Generate the destination filename by changing the extension to '.wav'
    dst = os.path.splitext(src)[0] + ".wav"

    # Convert mp3 to wav
    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format="wav")
    print(f"Converted {src} to {dst}")

if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Convert an MP3 file to WAV format.")
    parser.add_argument("src", help="The path to the source MP3 file.")
    
    args = parser.parse_args()
    main(args.src)
