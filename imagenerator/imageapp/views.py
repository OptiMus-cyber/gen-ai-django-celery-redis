from django.shortcuts import render
from django.http import JsonResponse
from .tasks import generate_image

def generate_images(request):
    prompts = ["A red flying dog", "A piano ninja", "A footballer kid"]
    tasks = [generate_image.delay(prompt, i) for i, prompt in enumerate(prompts)]

    return JsonResponse({"status": "Tasks started", "task_ids": [task.id for task in tasks]})
