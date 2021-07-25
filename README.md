

# Credit-Risk-Modeling
Credit risk is the risk that a borrower will not reimburse all or part of its credit on the due dates stipulated in the contract signed between the borrower and the lender.
##
The purpose of measuring credit risk is to assess the probability of default by a borrower. 
![image](https://user-images.githubusercontent.com/53350981/126901091-fcf7d09e-eefd-450f-b564-7d71a0dbeb23.png)
##
Technique allows to transform qualitative information (age, address, income, marital status ...) into quantified and quantified data. The scoring allows to give a precise idea of the repayment capacity of an individual through the note which is produced and qualifies as information-result as opposed to the information which is entered for processing.
##

I Create a LightGBM model for credit risk classification for an individual.
#
Light GBM is a gradient boosting framework that uses tree based learning algorithm.
#
How lightGBM differs from other tree based algorithm?
#
**Light GBM grows tree vertically while other algorithm grows trees horizontally meaning that Light GBM grows tree leaf-wise while other algorithm grows level-wise.<br/>
**It will choose the leaf with max delta loss to grow.<br/>
**When growing the same leaf, Leaf-wise algorithm can reduce more loss than a level-wise algorithm.<br/>
##
# Architecture

![image](https://user-images.githubusercontent.com/53350981/126901216-cb1af053-9b46-4e69-8953-dbc47525ba9a.png)

# Data Distribution

![image](https://user-images.githubusercontent.com/53350981/126901260-b6b49738-8add-40ae-b425-ce257bb2648e.png)

# Annual income and jobs

![image](https://user-images.githubusercontent.com/53350981/126901303-1f39f83c-d737-4484-8068-033d4b9bd60d.png)

#Distribution of Annual Income (Test and Training data)
![image](https://user-images.githubusercontent.com/53350981/126901378-17b281fd-d5df-4b7e-9571-791f03000692.png)

# Model’s results

![image](https://user-images.githubusercontent.com/53350981/126901488-85b7007f-eeb9-4583-8f93-96edbb49f47d.png)

https://user-images.githubusercontent.com/53350981/126900734-24b7adb7-35ef-4c39-a31b-b47f3d107436.mp4


