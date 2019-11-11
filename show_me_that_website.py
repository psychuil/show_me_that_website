from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import argparse, boto3, time

parser = argparse.ArgumentParser(description='Screenshot a webpage, and maybe throw it to S3')
parser.add_argument('url', type=str, metavar='', help='which page to screenshot')
parser.add_argument('-b', '--bucket', type=str, metavar='', help='which bucket to upload to')
args = parser.parse_args()
s3 = boto3.resource('s3')


def getScreenshot(link):
    options = Options()
    options.headless = True
    with webdriver.Firefox(options=options, executable_path="geckodriver.exe") as driver:
        driver.get(link)
        height = driver.execute_script("return document.body.scrollHeight")
        width = driver.execute_script("return document.body.scrollWidth")
        driver.set_window_size(width, height)
        time.sleep(2)
        driver.save_screenshot(f"{link[7:]}.png")
    return f"{link[7:]}.png"


def throwToS3(file, bucket):
    data = open(file, 'rb')
    s3.Bucket(bucket).put_object(Key=file, Body=data)


filename = getScreenshot(args.url)
if args.bucket is not None:
    throwToS3(filename, args.bucket)
