import os

from rodan.jobs.base import RodanTask
from celery.utils.log import get_task_logger

class ContrastCorrection(RodanTask):

    name = 'Contrast Correction'
    author = 'Wanyi Lin and Khoi Nguyen'
    description = "Corrects contrast and brightness"
    logger = get_task_logger(__name__)

    enabled = True
    category = 'Contrast and brightness correction'
    interactive = False

    input_port_types = [{
        'name': 'PNG Image',
        'resource_types': lambda mime: mime.startswith('image/'),
        'minimum': 1,
        'maximum': 1
    }]
    output_port_types = [{
        'name': 'RGB PNG image',
        'resource_types': ['image/rgb+png'],
        'minimum': 1,
        'maximum': 1
    }]

    settings = {
        'title': 'Contrast Correction',
        'type': 'object',
        'job_queue': 'Python3',

        'properties': {
            'contrast': {
                'type': 'number',
                'default': 127
            },
            'brightness': {
                'type': 'number',
                'default': 0
            }
        }
    }

    def run_my_task(self, inputs, settings, outputs):
        from . import contrast_correction_engine as Engine

        load_image_path = inputs['PNG image'][0]['resource_path']
        image = Engine.load_image(load_image_path)

        # Remove background here.
        image_processed = Engine.contrast_and_brightness(image, settings["contrast"], settings["brightness"])

        save_image_path = "{}.png".format(outputs['RGB PNG image'][0]['resource_path'])
        Engine.save_image(save_image_path, image_processed)
        os.rename(save_image_path,outputs['RGB PNG image'][0]['resource_path'])
        return True

    def my_error_information(self, exc, traceback):
        return
