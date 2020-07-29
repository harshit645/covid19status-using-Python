from covid import Covid

covid=Covid()

#total active cases
print(covid.get_total_active_cases())

#total deaths
print(covid.get_total_deaths())

#total confirmed cases
print(covid.get_total_confirmed_cases())
