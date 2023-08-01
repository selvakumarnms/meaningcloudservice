import requests
import papermill as pm
import schedule
import time
import os

import sys
sys.path.append("/var/task/bin")


def lambda_handler(events, handle):
    url = "http://example.com"
    pm.execute_notebook(
        "C:\TweetAnalysis\playstore_scraping.ipynb",
        "output.ipynb",
        kernel_name='python3',
        parameters=dict(
            url=url,
        )
    )
    return os.path.exists("/tmp/output.ipynb")


if __name__ == '__main__':
    schedule.every(1).minutes.do(lambda_handler)
    #schedule.every().day.at("01:00").do(lambda_handler)
    schedule.every()
    while True:
        schedule.run_pending()
        time.sleep(1)
