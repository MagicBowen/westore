from datetime import datetime
import  currency

def __get_million_seconds_elapsed__(start, end):
    delta = end - start
    return (delta.days * 24 * 60 * 60 + delta.seconds) * 1000 + delta.microseconds / 1000.0

def __get_respond_time__(converter, repeat_count):
    start = datetime.now()
    for i in range(0, repeat_count):
        converter.get_exchange_rate()
    end = datetime.now()    
    print 'avarage time is %d million second' %(__get_million_seconds_elapsed__(start, end)/repeat_count)

def test_availability(repeat_count):
    print "get currency from fixer"
    __get_respond_time__(currency.FixerProvider("USD", "EUR", 5), repeat_count)  
    print "get currency from yahoo"
    __get_respond_time__(currency.YahooProvider("USD", "EUR", 5), repeat_count)

if __name__ == '__main__': 
    try:
        test_availability(10)
        currency.convert_currency("USD", "EUR", 100)
    except currency.CurrencyUnavailableError:
        print "currency rate unavailable"
    else:
        print "success!"
