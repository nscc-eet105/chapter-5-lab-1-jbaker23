#My name is Jacob Baker and this is Ch 5 Lab 1 and I am completing this on June 24
# Code contains four problems.
STATE_TAX_RATE = .051
COUNTY_TAX_RATE = .025
def calculate_state_tax(sales_amount, tax_rate):
	return(sales_amount * tax_rate)
	
def calculate_county_tax(amount, rate):
	return (amount * rate)# there was an error in this line because return was not used
def main():
    print('This program will calculate your taxes!')#there was an error of \n on this line

    sale =float(input('How much is the cost of your purchase? '))
    state_tax = calculate_state_tax(STATE_TAX_RATE, sale)#there is an error that occurs here because state tax was not defined
    county_tax = calculate_county_tax(COUNTY_TAX_RATE, sale)
    total_cost = float(sale) + float(state_tax) + float(county_tax)
    
    print('Sale amount: $', format(sale, '.2f'), sep = '')#there was an error of \n on this line
    print('State tax  : $', format(state_tax, '.2f'), sep = '')
    print('County tax : $', format(county_tax, '.2f'), sep = '')
    print('Total cost : $', format(total_cost, '.2f'), sep = '')



main()
