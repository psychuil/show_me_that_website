# Show me that website

This tool allows you to capture a screenshot of a webpage, with the option of uploading it to an s3 bucket.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

You're not gonna need much, just python 3.6+ installed.

### Installing

Download the files enclosed and installed the required modules:

```
pip install -r Requirements.txt
```

## Using the tool

This is a CLI tool, you can run it using:
```
python show_me_that_website 'http://url.of.your.choice'
```
This will create a png file in the same folder of the URL in question.
If you would like to upload it to an s3 bucket, simply use the -b or --bucket argument like so:

```
python show_me_that_website 'http://url.of.your.choice' -b my-bucket
```

For more help use:

```
python show_me_that_website -h
```

## Built With

* [Selenium](https://www.seleniumhq.org/)
* [Boto3](https://github.com/boto/boto3) - AWS SDK for Python

## Authors

* **Anton Nosovitsky** - *Initial work* - [psychuil](https://github.com/psychuil)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


