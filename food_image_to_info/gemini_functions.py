import base64
import vertexai
from vertexai.preview.generative_models import GenerativeModel, Part, Image


def convert_file_to_image(filepath):
    '''
    filepath: str a string that points to image in png format
    '''
    img = Image.load_from_file(filepath)
    return img


def generate_from_vision(prompt, config={
        "max_output_tokens": 2048,
        "temperature": 0.6,
        "top_p": 1,
        "top_k": 32
    }):
  model = GenerativeModel("gemini-pro-vision")
  response = model.generate_content(
    prompt,
    generation_config=config,
  stream=False,
  )
  return response

  print(response.text)
  


def image_to_description(pre_prompt, image_path, post_prompt, config):
  '''
  pre_prompt: str
  image: str a string that points to image in png format
  post_prompt: str
  '''
  img = convert_file_to_image(image_path)
  content =[pre_prompt, img, post_prompt]
  response = generate_from_vision(content, config)

  response_text = response.text
  
  # write response_text to file
  with open('descriptions/' + image_path.split('/')[-1].split('.')[0] + '_description.txt', 'w') as f:
    f.write(response_text)

  return response_text



def turn_descriptions_into_json(description_file_path, extraction_prompt, config):
  '''
  description_path: str
  '''
  model = GenerativeModel("gemini-pro")

  ## open file in description_path and read in text
  with open(description_file_path, 'r') as f:
    text = f.read()

  ## generate json from text
  response = model.generate_content(
    contents=[extraction_prompt, text],
    generation_config=config,
  stream=False,
  )

  #write the corresponding json
  with open('jsons/' + description_file_path.split('/')[-1].split('.')[0] + '.json', 'w') as f:
      f.write(response.text.strip("```").strip("json"))

