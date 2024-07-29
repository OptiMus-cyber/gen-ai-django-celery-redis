from celery import shared_task
import requests
import os
import base64
# from .models import GeneratedImage

# @shared_task
def generate_image(prompt, index):
    api_key = os.getenv('STABILITY_API_KEY')
    api_host = 'https://api.stability.ai'
    engine_id = "stable-diffusion-xl-1024-v1-0"

    response = requests.post(
        f"{api_host}/v1/generation/{engine_id}/text-to-image",
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {api_key}"
        },
        json={
            "text_prompts": [{"text": prompt}],
            "cfg_scale": 7,
            "height": 1024,
            "width": 1024,
            "samples": 1,
            "steps": 30,
        },
    )

    if response.status_code != 200:
        print(response.text)
        return {"error": response.text}

    data = response.json()
    image_base64 = data["artifacts"][0]["base64"]
    image_data = base64.b64decode(image_base64)

    # Ensure the output directory exists
    output_dir = './out'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save image to file
    image_filename = os.path.join(output_dir, f"image_{index}.png")
    with open(image_filename, "wb") as f:
        f.write(image_data)

    # Save to the database
    # GeneratedImage.objects.create(prompt=prompt, image_path=image_filename)

    return image_filename