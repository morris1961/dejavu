import argparse
import json
import sys

from dejavu import Dejavu
import dejavu.logic.decoder as decoder
from dejavu.logic.recognizer.file_recognizer import FileRecognizer

with open("dejavu.cnf.SAMPLE") as f:
    config = json.load(f)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Dejavu: Audio Fingerprinting library")
    parser.add_argument("file1", help="qq")
    parser.add_argument("file2", help="qq")
    parser.add_argument('-a',"--all", help="qq", action="store_true")
    args = parser.parse_args()
    if not args.file1 or not args.file2:
        parser.print_help()
        sys.exit(0)

    file1 = args.file1
    file2 = args.file2
    printAll = args.all

    # create a Dejavu instance
    djv = Dejavu(config)
    name = decoder.get_audio_name_from_path(file1)
    djv.fingerprint_file(file1)
    djv.fingerprint_file(file2)

    results = djv.recognize(FileRecognizer, file2)
    if printAll:
        print(results)
    else:
        for result in results['results']:
            if result['song_name'].decode() == name:
                print(result)
                break