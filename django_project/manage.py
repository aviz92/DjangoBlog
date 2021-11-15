#!/usr/bin/env python
import os
import sys

from Logger_Infrastructure.Projects_Logger import ProjectsLogging

if __name__ == '__main__':
    logger = ProjectsLogging('DjangoBlog').project_logging()
    logger.info("Start DjangoBlog program")

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
