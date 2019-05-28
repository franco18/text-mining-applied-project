import scrapy
import subprocess

class NIPSSpider(scrapy.Spider):
    name = 'nips_spider'

    def start_requests(self):
        baseurl = 'http://papers.nips.cc/book'
        url = "{}/advances-in-neural-information-processing-systems-{}-{}".format(baseurl, self.number, self.year)
        yield scrapy.Request(url, self.parse_list)


    def parse_list(self, response):
        for li in response.css('li'):
            paper_page = li.css('a::attr(href)').extract_first()
            yield response.follow(paper_page, callback=self.parse_paper)

    def parse_paper(self, response):
        pdf_url = response.css('a[href$=".pdf"]::attr(href)').extract_first()
        yield response.follow(pdf_url, callback=self.save_pdf)

    def save_pdf(self, response):
        path = response.url.split('/')[-1]
        pdf_path = "pdfs/{}".format(path)
        txt_path = "txts/{}.txt".format(path)
        self.logger.info("Saving pdf: {}".format(pdf_path))

        with open(pdf_path, 'wb') as pdf:
            pdf.write(response.body)

        self.logger.info("Saving txt: {}".format(txt_path))
        subprocess.call(['pdftotext', pdf_path, txt_path])
