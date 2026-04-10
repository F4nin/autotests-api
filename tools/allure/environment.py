from config import settings
import sys
import platform


def create_allure_environment_file():
    items = [f'{key}={value}' for key, value in settings.model_dump().items()]
    items.extend([
        f"os_info: {platform.system()}, {platform.release()}",
        f"python_version= {sys.version}"
    ])
    properties = "\n".join(items)

    with open(settings.allure_results_dir.joinpath('environment.properties'), "w+") as file:
        file.write(properties)

