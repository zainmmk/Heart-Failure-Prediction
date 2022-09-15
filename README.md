# LHL Final Project: Heart Failure Prediction
## The Problem
- Ischaemic heart disease is the number 1 cause of death globally, it accounts for 16% of worlds total deaths
- Heart disease is becoming an increasingly prevalent problem, from 2000-2019, the number of people worldwide who died as a result of ischaemic heart disease rose by over 2 million
- The second and third worldwide leading causes of death are also related to cardiovascular health
## Project Goals
- Using a dataset obtained from Kaggle, identify the features that play a significant role in correctly identifying heart disease in individuals
- Create a model that can predict an individuals risk of heart disease
- Test the model on local clinic data 
- Deploy the developed model so it can predict a probability that an individual has heart disease (help assess the risk an individual is at) 
## Process
### EDA + Data Cleaning
Identify relationships between target variable and other features in the data. Some main ones that stuck out were ST Slope, which looks at the slope at the ST section of an ECG reading, which had values of Up, Down and Flat. The values of down and flat in this feature had a much higher prevalence of positive for heart disease while Up seemed to indicate a healthy reading. Old peak, another measure obtained from reading the ECG seemed to be a signficant predictor with higher values more likely resulting in a positive heart disease classification. I also used PCA dimensionality reduction to plot the data in 2-Dimensions so I could get a visual idea of how the positive and negative classifications for heart disease looked on the same plot. There were values of 0 present in the cholesterol and resting blood pressure features, which is not possible in reality. Instead these 0 values were converted to null and then filled in using KNN (Nearest Neighbor) imputation.
### Identifying Metric To Maximize
In classification problems, typically one metric is chosen to try and maximize depending on the context. In the case of heart disease, all positive occurences must be identified as missing them can have disasterous consequences. So, in this case, recall is the metric chosen to be maximized. Recall is calculated by taking all true positives and dividing that number by all true positives + all false negatives (in other words, all positive occurences in the data).
### Baseline Model Creation
A baseline model was created using a basic logistic regression model, in which one-hot encoding was used on categorical variables to allow them to be used in the model. This baseline model achieved a recall score of 87.5%.
### Model Selection
After creating the baseline, several other models were tested in grid searches that tuned their hyperparameters to find the best performance. SVC, naive bayes, and random forest classifier were all tested and it was found that the random forest classifier performed the best. It achieved a recall score of 91%, so it served to be a decently better performing model than the baseline. 
### Feature Selection
With the random forest classifier that was created, feature importance values were extracted to view what the classifier was deeming to be the most important in its decision making. Forward sequential feature selection was also done with the random forest classifier to determine which features should be kept. I approached the feature selection from here in two ways, one that used the features that forward sequential feature selection identified as the most important, and the other was looking at the graph of feature importance extracted from the model and using my own discretion to cut features.
### Final Model Comparison
The model created out of the features selected from sequential forward selection turned out to have a recall score of 91.3%, performing similar to the random forest classifier created earlier with significantly less features. On the other hand, the model I created out of the feature importances extracted earlier kept more features, but had a recall score of 97.6%.This was a great improvement over the initial random forest classifier and significant compared to the baseline model created, showing a 10% improvement in recall. This was the model chosen to be the final one.
### Deploying The Model
Using streamlit, an app was created to deploy the final model. The app takes in the features of: Age, Chest Pain Type, Resting BP, Cholesterol, MaxHR, Exercise Angina, Old peak, and ST Slope. It returns a prediction in the form of percentage for what it believes is your chance of having heart disease.
## Future Goals
In the future, I would like to add a neural network that can have an ECG input, and would return the ST Slope value and the old peak measurement. This would be a great step in making the model easier to use, as analyzing ECG graphs can be tedious and even confusing sometimes. 






