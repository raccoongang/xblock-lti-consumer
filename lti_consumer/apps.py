"""
Plugin configuration for integration settings in edx-platform.
"""
from __future__ import unicode_literals

from django.apps import AppConfig


class ApiConfig(AppConfig):
    name = "lti_consumer"
