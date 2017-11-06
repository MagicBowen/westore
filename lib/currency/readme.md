# currency converter
Using online data from fixer and yahoo to convert currency
## currency code
flollwing the defination of ISO4217
http://en.wikipedia.org/wiki/ISO_4217

## usage
### generic API
convert_currency(from_code, to_code, amount_of_money[, connection_time_out])
for example:
`convert_currency("USD", "EUR", 100)`

It would:
1. try to get exchange rate from fixer
2. connect to yahoo in case fixer is unavailable

### API connect to fixer
convert_currency_using_fixer(from_code, to_code, amount_of_money[, connection_time_out])

### API connect to yahoo
convert_currency_using_yahoo(from_code, to_code, amount_of_money[, connection_time_out])
