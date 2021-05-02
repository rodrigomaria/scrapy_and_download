# Scrapy and Download files

This project is about scraping websites in search by urls for download files.

This project use python version 3 and Selenium.

## Instructions:
1. Install virtual env
```bash
$ pip install virtualenv
```

2. Create virtual enviroment
```bash
$ virtualenv -p python3 scrapy_and_download
```

3. Activate virtual enviroment in MacOS or Linux
```bash
$ source scrapy_and_download/bin/activate
```

4. Install the packages in virtual enviroment
```bash
$ pip install -r requirements.txt
```

5. When or if necessary, deactivate the virtual enviroment
```bash
$ deactivate
```

## How to use:
In the `execute` folder, we have two files: `scrapy.py` and `download.py`.

The file `scrapy.py` we executed scrapping in the site `https://www.flickr.com` how an example.

In the file `download.py` we download the files hosted in the urls in `url.csv`, created earlier.