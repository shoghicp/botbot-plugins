#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='botbotme_plugins',
    version='1.0',
    description="Plugins and service integrations for BotBot.me",
    author="Lincoln Loop",
    author_email='info@lincolnloop.com',
    url='https://github.com/lincolnloop/botbotme_plugins',
    packages=find_packages(),
    install_requires=(
        'pytest==2.3.5',
        'mock==1.0.1',
        'requests==1.2.3',
        'defusedxml==0.4.1',
    ),
    scripts=['bin/botbotme_shell'],
)
