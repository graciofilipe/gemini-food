from vertexai.preview.generative_models import GenerativeModel, Part, Image
from gemini_functions import generate_from_vision, convert_file_to_image, image_to_description
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
    parser.add_argument("--pre_prompt", type=str, required=True)
    parser.add_argument("--folder_path", type=str, required=True)
    parser.add_argument("--post_prompt", type=str, required=True)
    parser.add_argument("--config", type=str, required=True)
    
    args = parser.parse_args()
    pre_prompt = args.pre_prompt
    folder_path = args.folder_path
    post_prompt = args.post_prompt
    config = data=json.loads(args.config)
    
    list_of_files = list_files(folder_path)

    for image in list_of_files:
        print(image)
        try:
            response = image_to_description(
                pre_prompt, image, post_prompt, config
                )
        except:
            print("could not handle", image)
            continue


if __name__ == "__main__":
    run()
