import pandas as pd
#load dataset
file_path = "C:/Users/Sandeep/Desktop/data_powerbi/datas.csv"
df = pd.read_csv(file_path, low_memory=False)
print("First 5 Rows")
print(df.head())

print("\nDataset Info")
print(df.info())
#remove extra column
if "Unnamed: 9" in df.columns:
    df = df.drop(columns=["Unnamed: 9"])
#convert datatype
df["Data_Value"] = pd.to_numeric(df["Data_Value"], errors="coerce")
df["YearStart"] = pd.to_numeric(df["YearStart"], errors="coerce")
#check missing data
print("\nMissing Values:")
print(df.isnull().sum())
#remove imp null rows
df = df.dropna(subset=["YearStart","Age","Gender","Data_Value"])
#clean age group
df["Age"] = df["Age"].replace({
    "65-84": "65+",
    "85+": "65+"
})
#basic data analysis
print("\nAverage Vision Problem by Age:")
age_analysis = df.groupby("Age")["Data_Value"].mean()
print(age_analysis)

print("\nAverage Vision Problem by Gender:")
gender_analysis = df.groupby("Gender")["Data_Value"].mean()
print(gender_analysis)

print("\nAverage Vision Problem by Question:")
question_analysis = df.groupby("Question")["Data_Value"].mean()
print(question_analysis)

#save dataset to new file
clean_file = "C:/Users/Sandeep/Desktop/data_powerbi/clean_vision_data.csv"
df.to_csv(clean_file, index=False)
print("\nClean dataset saved successfully!")
