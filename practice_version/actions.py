# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from datetime import datetime

import logging
import requests
import json
from rasa_core_sdk import Action

logger = logging.getLogger(__name__)

class ApiAction(Action):
	def name(self):
		return "action_match_news"

	def run(self, dispatcher, tracker, domain):
		return []