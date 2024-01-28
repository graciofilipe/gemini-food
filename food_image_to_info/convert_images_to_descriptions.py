from gemini_functions import generate_from_vision, convert_file_to_image, image_to_description
from aux_functions import list_files
import json
import os
import argparse


def run():

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

    for image_path in list_of_files:
        print(image_path)

        # check if corresponding description file already exists
        description_path = 'descriptions/'+image_path.split('/')[1].split('.')[0] +'_description.txt'
        if os.path.exists(description_path):
            print("image already described")
        else:
            try:
                response = image_to_description(
                    pre_prompt, image_path, post_prompt, config
                    )
            except:
                print("could not handle", image_path)
                continue


if __name__ == "__main__":
    run()
