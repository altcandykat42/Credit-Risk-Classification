#  downloading the data
import openml
# print(openml.datasets.list_datasets(output_format="dataframe"))
dataset = openml.datasets.get_dataset(43454)
X,y,_,_ = dataset.get_data(dataset_format="dataframe")
X.to_csv("credit_risk_data.csv", index=True)