#!/bin/bash
poetry config virtualenvs.in-project true
poetry install
echo 'export $(cat /workspaces/accout-maker/.env.local | xargs)' >> ~/.bashrc
