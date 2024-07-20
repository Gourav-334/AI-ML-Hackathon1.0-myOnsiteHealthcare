import pandas as pd
from statsmodels.tsa.api import VAR
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pickle










def TrainOnVAR(filename, trained_pickle, fitted_pickle):
    # Importing CSV file
    file_path = filename
    data = pd.read_csv(file_path)

    # Set 'Date' as the index
    data.set_index('Date', inplace=True)

    # Ensure the data is in datetime format
    data.index = pd.to_datetime(data.index)

    # 'Confirmed' is the only dependent variable
    data = data[['Confirmed', 'Recovered', 'Deceased']]

    # 70:30 ratio splitting
    train_data, test_data = train_test_split(data, test_size=0.3, shuffle=False)

    # Model fitting on VAR regression
    model = VAR(train_data)

    # Time lags of 15 units, ic (information criterion) avoids overfitting
    fitted_model = model.fit(maxlags=15, ic='aic')

    # Gujarat_train_data.xlsx
    with open(trained_pickle, 'wb') as file:
        pickle.dump(train_data, file)

    # Gujarat_fitted_model.xlsx
    with open(fitted_pickle, 'wb') as file:
        pickle.dump(fitted_model, file)

    # Make predictions on the test data
    lag_order = fitted_model.k_ar
    forecast_input = train_data.values[-lag_order:]
    forecast = fitted_model.forecast(y=forecast_input, steps=len(test_data))

    # Convert forecasted values to a DataFrame for comparison
    forecast_df = pd.DataFrame(forecast, index=test_data.index, columns=test_data.columns)

    # Calculate Mean Squared Error for the forecasts
    mse = mean_squared_error(test_data, forecast_df)
    print(f'Mean Squared Error: {mse}')


    # Sample from training & summary
    print("Training Data:")
    print(train_data.head())

    print("\nModel Summary:")
    print(fitted_model.summary())










# Training individual dataset
TrainOnVAR("Ahmedabad.csv", "Ahmedabad_trained.pkl", "Ahmedabad_fitted.pkl")
TrainOnVAR("Amreli.csv", "Amreli_trained.pkl", "Amreli_fitted.pkl")
TrainOnVAR("Anand.csv", "Anand_trained.pkl", "Anand_fitted.pkl")
TrainOnVAR("Aravali.csv", "Aravali_trained.pkl", "Aravali_fitted.pkl")
TrainOnVAR("Baruch.csv", "Baruch_trained.pkl", "Baruch_fitted.pkl")
TrainOnVAR("Bhavnagar.csv", "Bhavnagar_trained.pkl", "Bhavnagar_fitted.pkl")
TrainOnVAR("Dahod.csv", "Dahod_trained.pkl", "Dahod_fitted.pkl")
TrainOnVAR("Gandhinagar.csv", "Gandhinagar_trained.pkl", "Gandhinagar_fitted.pkl")
TrainOnVAR("Gujarat.csv", "Gujarat_trained.pkl", "Gujarat_fitted.pkl")
#TrainOnVAR("India.csv", "India_trained.pkl", "India_fitted.pkl")


