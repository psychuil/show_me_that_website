from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import argparse, boto3, time

parser = argparse.ArgumentParser(description='Screenshot a webpage, and maybe throw it to S3')
parser.add_argument('url', type=str, metavar='', help='which page to screenshot')
parser.add_argument('-b', '--bucket', type=str, metavar='', help='which bucket to upload to')
args = parser.parse_args()
s3 = boto3.resource('s3')
DRIVER_PATH="./geckodriver"


def getScreenshot(link):
    options = Options()
    options.headless = True
    screenshot_fn = f"{link.split('://')[1]}.png"
    with webdriver.Firefox(options=options, executable_path=DRIVER_PATH) as driver:
        driver.get(link)
        height = driver.execute_script("return document.body.scrollHeight")
        width = driver.execute_script("return document.body.scrollWidth")
        driver.set_window_size(width, height)
        time.sleep(2)
        driver.save_screenshot(screenshot_fn)
    return screenshot_fn


def throwToS3(file, bucket):
    data = open(file, 'rb')
    s3.Bucket(bucket).put_object(Key=file, Body=data)


filename = getScreenshot(args.url)
if args.bucket is not None:
    throwToS3(filename, args.bucket)
