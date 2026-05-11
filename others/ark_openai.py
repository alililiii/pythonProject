#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Common OpenAI/Ark client helper for scripts in others/.
"""

import os
from openai import OpenAI

DEFAULT_ARK_BASE_URL = "https://ark.cn-beijing.volces.com/api/v3"
DEFAULT_ARK_MODEL = "ep-20250217173345-877sm"


def get_openai_client():
    api_key = os.getenv("ARK_API_KEY") or os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "Missing Ark/OpenAI API key. Set ARK_API_KEY or OPENAI_API_KEY."
        )
    base_url = os.getenv("ARK_BASE_URL", DEFAULT_ARK_BASE_URL)
    return OpenAI(api_key=api_key, base_url=base_url)


def get_model_name():
    return os.getenv("ARK_MODEL", DEFAULT_ARK_MODEL)
