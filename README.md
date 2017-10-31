# Web Crawing


## Installations

### Environments
- python 3.5.x
- elasticsearch
- kibana(options)

### Step 0. Servers 
- running elasticsearch / kibana server

### Step 1. python env (python 3.5.x)
- for mac

```
# sudo python3 -m venv elastic-env
# source elastic-env/bin/activate
# deactivate
```

- for window

```
> pip -m venv elastic-env
> ../elastic-env/Script/activate
> deactivate
```

## Sources

- [`00.elastic_input.py`](python/00.elastic_input.py)
- [`01.http_urllib_request_json.py`](python/01.http_urllib_request_json.py)
- [`01.http_urllib_use_parse.py`](python/01.http_urllib_use_parse.py)
- [`02.http_parser_bs4.py`](python/02.http_parser_bs4.py)
- [`03.http_parser_exam_weather.py`](python/03.http_parser_exam_weather.py)
- [`04_0.auth_page_crawling.py`](python/04_0.auth_page_crawling.py)
- [`04_1.requests_lib_use.py`](python/04_1.requests_lib_use.py)
- [`04_2.auth_page_using_requests.py`](python/04_2.auth_page_using_requests.py)
- [`05.auth_page_using_phantomjs.py`](python/05.auth_page_using_phantomjs.py)

## Links

- [나만의 웹 크롤러 만들기 시리즈](https://beomi.github.io/2017/02/27/HowToMakeWebCrawler-With-Selenium/)
- [crawling 도장깨기](https://askdjango.github.io/)
- [nomade.kr](https://nomade.kr/vod/automation/135/)
- [phantomjs.org](http://phantomjs.org/quick-start.html)