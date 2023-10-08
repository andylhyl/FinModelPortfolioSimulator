import statsmodels.formula.api as smf

# For each estimate of the model, we want to save the record of the corresponding stock ticker, alpha and betas for each factors
# So that we can create a dataframe off of it.
def get_beta(model, dataset, stock):
    beta = {}

    # In this for loop, we iterating through each ticker name in our dict ("result" from above), and use the corresponding data for that stock to estimate the model
    # It will then save the estimated coefficient in to the created list above.
    for i in stock:
        data_sec = dataset[dataset["ticker"] == i] # Here, we make sure that we are only using the data for 1 specific stock ticker at a time.
    
    # As the first row of the ex_return is always NaN, we want to make sure we start on the second row
        
        if model == 'capm':
            temp_reg = smf.ols(data = data_sec[1:], formula = 'ex_return ~ mkt_ex_return').fit(cov_type = 'HC3')
        
        elif model == 'fama':
            temp_reg = smf.ols(data = data_sec[1:], formula = 'ex_return ~ mkt_ex_return + SMB + HML').fit(cov_type = 'HC3')
        
        elif model == 'momentum':
            temp_reg = smf.ols(data = data_sec[1:], formula = 'ex_return ~ mkt_ex_return + SMB + HML + Mom').fit(cov_type = 'HC3')
        
        # We then append each needed estimte into our list, for each iteration.
        beta[i] = temp_reg.params.drop('Intercept').to_dict()
    return beta




