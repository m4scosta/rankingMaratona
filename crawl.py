# coding: utf8
from apscheduler.schedulers.blocking import BlockingScheduler
from crawler.utils import CrawlerDePontuacao

scheduler = BlockingScheduler()


@scheduler.scheduled_job('interval', minutes=10)
def uri_crawl():
    CrawlerDePontuacao().crawl()


scheduler.start()