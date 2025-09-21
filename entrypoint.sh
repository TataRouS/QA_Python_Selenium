#!/bin/bash
pytest /app/tests/Part_1/test_cataloge_page.py --base_url=$BASE_URL --alluredir=/app/allure-results --browser=remote --headless --selenoid_url=$SELENOID_URL
