# Task 1.2 preprocessing

## Extracted several features from the given data:
Months, mainly to represent seasons
Weekdays, represented by 0-6
is holiday, boolean/categorical value. Added manually spring, easter etc and added norwegian holidays from a libary.
'Fra time' is unchanged.
All other features are removed.

## Plotted features to find patterns
to plot, uncomment plot features() in main method.
**screenshots of plots**

Observations from plots:
There are big variations depending on the features we selected, such as weekdays 5-6 and july having lower traffic

# Task 1.3
## Modelling
Trained and tested three models:
1. Decision Tree Regressor
2. Linear Regression
3. MLP Regressor

Best model was Decision Tree Regressor with a R2 score of between 0.91 and 0.94 for the different predictions. 

We already know form plotting that the models are going to differ some, e.g. different traffic at different hours. Tried learning a model with y as 'Sentrum' using it to predict 'Danmarksplass' and got a R2 score as 0.62, proving the models differ too much to be used interchangably.

Visualized both predicted and actual data for 2020 to perform a sanity check. The model appears to sometimes guess way higher, maybe because of either covid or some holiday the model is unaware of. The model also rarely predicts 0 of some reason.

### predicting 2020

Tried using all data as training data, and then predicting the data for 2020. 
