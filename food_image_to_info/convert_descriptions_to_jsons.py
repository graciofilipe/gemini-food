from vertexai.preview.generative_models import GenerativeModel, Part, Image
from gemini_functions import turn_descriptions_into_json
import json
import os

def list_files(directory):
    for entry in os.listdir(directory):
        full_path = os.path.join(directory, entry)
        if os.path.isfile(full_path):
            yield full_path


def run():
    # import arguments from command line
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt", type=str, required=True)
    parser.add_argument("--folder_path", type=str, required=True)
    parser.add_argument("--config", type=str, required=True)
    
    args = parser.parse_args()
    prompt = args.prompt
    folder_path = args.folder_path
    config = data=json.loads(args.config)
    
    list_of_files = list_files(folder_path)

    for description_file_path in list_of_files:
        print(f"Processing {description_file_path}")
        turn_descriptions_into_json(
            description_file_path=description_file_path, 
            extraction_prompt=prompt, 
            config=config)


if __name__ == "__main__":
    run()
