## Health Insurance Cost Predictor

## All files to be graded are located inside of the notebook folder

## Project structure

notebook folder -> contains data in a csv file, eda and model training notebooks: https://github.com/RezaP117/Health_Insurance_Cost_Predictor/tree/main/notebook

src folder and other files -> ignore (for personal purposes)

1. Why should anyone care about this question?
   Understanding these types of costs can greatly help patients and business owners. By making a machine learning model that predicts these values, business owners can allocate the proper resources financially to ensure that workers are getting the healthcare that they need. This can also help with making health insurance more accessible to people who have lower income.
2. What question am I trying to answer?
   Can a machine learning model accurately predict health care costs for patients based on certain characteristics?
3. What data will I use to answer this question?
   I will use publically available datasets (Kaggle, UCI, etc.) which contain features such as age, sex, smoker status, # of children, etc. in order to make the model.
4. What methods am I using to answer this question?
   Data Preprocessing, EDA, Feature Selection, Feature Engineering, Various ML model implementations (Regression models), and model evaluation.
5. What did your research find?
   I found that the trait most associated with the charges a person would face is their smoking status, smokers on average have a much higher amount of charges than non-smokers. I also found that the patients in the south-east region have the most cost and highest average cost of insurance.
6. Next steps?
   If I were to keep iterating on this problem, I would source more data from other sources where it is allowed to get more variation in data, I would try to add more specific features such as state/city so that I can a more comprehensive understanding of the charge distribution.
7. Outline of project
   Notebook folder contains eda.ipynb, model_training.ipynb, and a data folder with the csv file

## Important EDA findings (also metioned in eda.ipynb)

1. None of the numerical features had a high amount of correlation, so no features were removed for multicollinearity
2. Smoking has the biggest impact on health insurance prices for patients
   - Clear patterns are seen when comparing other features and having smoking be the color hue
3. Cost for insurance in general goes up as the age of the patients go up (slight upward trend)
4. For this data, the number of children didn't seem to show any patterns in terms of costs (my initial thought was that the higher the number of children, the higher the insurance charges)
5. The Southeast region had the highest average cost of insurance compared to the Northeast, Northwest, and Southwest regions

## Important notes to be taken based on EDA findings 
1. Businesses and healthcare providers in the Southeast region should be more accomodating towards making health care more affordable as this is the region with the highest mean of insurance costs. (This should be a rule that is followed in general, but for the purposes of this data set specifically, the Southeast region should be looke at more intently)
2. If patients who smoke were to eliminate it from their habits, then they would most likely see a decrease in their health care costs. 

## Next steps

If I were to continue working on this problem, I would invest into getting more data and engineer more features that I think would be impactful in determining the costs. I would also collberate with experts in the healthcare field which could help in my understanding of these features and why they might have the importance that they do. I would also try and get this model to be used with a variety of businesses and datasets so that I can effeciently evaluate its performace. The most important part post-implementation would be the constant reevaluation and tuning of the model so that it can better predict these prices.
