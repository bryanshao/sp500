import time

import parsekit
from parsekit import core
import requests

URL_BASE = 'http://download.finance.yahoo.com/d/quotes.csv?s={0}&f=d1ohgpv&ignore=.csv'

class TickerURL(parsekit.Step):

    def run(self, record, metadata):
        # Replace "." by "-" in all ticker codes.
        ticker = record[0].replace('.', '-')

        # Assemble URL
        ticker_url = URL_BASE.format(ticker)

        # Fetch CSV
        self.log.info('fetching %s' % ticker_url)
        r = requests.get(ticker_url)
        if r.status_code != 200:
            raise Exception('invalid response')
        return r.text, metadata
