---
redirect_from:
  - "/14-pandas/edm-us-adult-census-income/questions"
interact_link: content/14_pandas/edm_us_adult_census_income/questions.ipynb
kernel_name: python3
has_widgets: false
title: 'Questions'
prev_page:
  url: /14_pandas/edm_us_adult_census_income/questions.html
  title: 'edm us adult census income'
next_page:
  url: /14_pandas/edm_us_adult_census_income/solution.html
  title: 'Solution'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-advanced-python/blob/master/content/14_pandas/edm_us_adult_census_income/questions.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




# get the data
run the following two cells below to get the data for this exercise,
then followup by reading the questions and writing your own code to answer them.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
!pip install requests

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import requests

url = "http://mlr.cs.umass.edu/ml/machine-learning-databases/adult/adult.data"
request = requests.get(url)
request.raise_for_status()
with open('adult.csv', 'w') as f:
    f.write(request.text)

### now the data is available in the file adult.csv. 
### read the questions below
# import pandas as pd
# pd.read_csv('adult.csv')    

```
</div>

</div>



# income for adults from the 1994 census
This dataset was extracted  done by Barry Becker from the 1994 Census database. 
source: http://mlr.cs.umass.edu/ml/datasets/Adult

Listing of attributes:

* age: continuous.
* workclass: Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked.
* fnlwgt: continuous.
* education: Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool.
* education-num: continuous.
* marital-status: Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse.
* occupation: Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces.
* relationship: Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried.
* race: White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black.
* sex: Female, Male.
* capital-gain: continuous.
* capital-loss: continuous.
* hours-per-week: continuous.
* native-country: United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands.
* income: >50K, <=50K.




## 1. load the data
1. extract the column names from the description and read the csv while supplying the columns names
   - rename columns with a hyphen `-` to use underscores `_` insead. example: `capital-gain --> capital_gain`
   - look at the head()
2. look at info, dtype, check for nan values
3. what are the value counts of the categorical variables: workclass, education, marital_status, occupation, relationship, race, sex, native_country, income?
   - do you notice the extra space ' ' at the beginning of each value?
   - remove the extra space
4. turn 'sex' and 'income' into 0/1 fields
   - replace the categorical 'sex' column with a numerical 'female' column with value 1 for females and 0 for males
   - replace the categorical 'income' column with a numerical 'over50k' column with value 1 for '>50k' and 0 for '<50K'
5. use `.describe()` function to get descriptive statistics for most columns
   - make sure that 'sex' and 'over50k' are now numerical fields



## 2. explore capital gains / losses
### capital_gain
1. plot the histogram for capital gains
   - verbally describe what you see
2. for people who have `capital_gain > 0` 
   - plot the histogram for capital gains
3. how many people have capital gains over 25000?
   - use `value_counts()` to look at all the values of capital_gain over 25000. 
   - what's weird about the data?
4. could the people who had capital_gain==25124 be related?
5. does capital_gain over 50k mean income is over 50k?

### capital_loss
1. plot the histogram of capital_loss
2. for people who have `capital_loss > 0` 
   - plot the histogram for capital_loss
3. how many people had both `capital_gain>0` and `capital_loss>0` ?
4. who can afford to lose money on capital investments?
   - what percent of people overall had over 50K income? 
   - what percent of people with 0 capital_loss? with capital_loss>0?

### combining and binning
1. create a new `capital_change` column that equals `capital_gain - capital_loss`
2. use the `qcut` function to quantize/bin/cut `capital_change` into a new columns called `capital_change_bin` with 10 bins of equal proportions.
   1. do not bin `capital_change==0` values as there are too many of them
   2. to simplify using this column later, use the left side of the interval created as the label
   3. label rows with `capital_change==0` as having `capital_change_bin=0`
   4. make sure you have no null values for `capital_change_bin`
3. how many people have a non-zero capital_change? 
   - lets call this 'has_capital_change'
   - plot 'has_capital_change' over 'over50k'
   - what do you learn from this diagram
4. plot `capital_change` by `over50k`
   - what do you learn from this diagram
4. plot `over50k` by `capital_change_bin`
   - what can you learn from this diagram?
   



## education
1. what is the mean education_num by education? 
  - sort the education categories by the mean_values. does it make sense
  - check out other descriptive statistics to see if anything falls out of place
  - turn education into a categorical ordered type
  - plot education VS education_num
  - what have we learned?
1. plot the distribution for `education`
2. plot over50k by education
   - what can we learn?
3. plot hours_per_week by education
   1. what can we learn from this plot?
   2. now use the hue="over50k" of seaborn to see hours_per_week by education/over50k.
      - learn anything else?
4. plot education_num by occupation
  - sort by mean education_num
4. plot education_num by workclass
  - sort by mean education_num
5. create a crosstab or a pivot_table of education VS occupation.
   - normalize it by the education rows 
     (each row X shows the conditional probability of having occupation Y by education level X) 
   - create a heatmap that shows which occpupations are most likely for each education level
   - verbally describe what you've learned
6.  create a crosstab or a pivot_table of education VS workclass.
   - normalize it by the education rows 
     (each row X shows the conditional probability of having workclass Y by education level X) 
   - create a heatmap that shows which workclass is most likely for each education level
   - verbally describe what you've learned
   - re-run this analysis without the private sector
7. plot "race" vs "education_num
8. plot "relationship" vs "education_num



## occupation / workclass
1. how many levels of occupation?
2. how many levels of worklass?
3. how many combinations? potential? actual?
4. plot `over50k` by `occupation`
   - sort by mean `over50k`
   - compare this to `over50k` by `education`. which variable more strongly predicts income?
   - compare this to `education_num` by `occupation`. are the highest paying jobs correlated with highest earning education?
5. plot `over50k` by `workclass`
6. look at combinations of occupation / workclass
   1. what are the top combinations in terms of earning over50k (mean)? how many people in that category?
   2. how many of these combinations have more than 100 people?
   3. show a heatmap of the mean over50k of occupation-vs-worklass for combinations with more than 100 people. 
      center the heatmap at the populations mean over50k for increased effect.
      what conclusions can you draw?
7. create a numerical encoding for occupation / workclass pairs
   - create a new column called "occ_class" that combines the string of the occupation and workclass
   - use the library [category_encoders](http://contrib.scikit-learn.org/categorical-encoding/), here's an [intro](https://towardsdatascience.com/smarter-ways-to-encode-categorical-data-for-machine-learning-part-1-of-3-6dca2f71b159) how to do it
   - use the weight of evidence encoder `ce.woe.WOEEncoder` here's an [article](https://towardsdatascience.com/all-about-categorical-variable-encoding-305f3361fd02#targetText=Weight%20of%20Evidence%20Encoding,-Weight%20of%20Evidence&targetText=Weight%20of%20evidence%20(WOE)%20is%20a%20measure%20of%20how%20much,P(Bads)%20%3D%201.) explaining it
   - add the encoded occ_class as a new column called `occ_class_woe` to your dataframe
      



## correlations
1. which features are most important, which correlate?
    - compute the correction matrix of features with themselves
2. draw a clustermap or heatmap of this correlation
   - center the cluster at 0
   - annotate the plot with the correlation values
3. look at the strongest correlations and draw some conclusions.
    



## TODO:
1. look at `relationship` and `marriage_status`. how meaningful are they? should we encode them?
2. look at `native_country`. how does immigration effect other variables? should we build further categories based on continent or on 1st/2nd/3rd world countries? should we add an `is_immigrant` boolean column?
3. we've done the analysis treating each row of the data as a person, when **in fact** each row represents a large group of people, with the variable `fnlwgt` counting how many people are in the group. redo some of the analysis with weighted averages
4. look further at age. should we cut this continous variable into age groups like 18-25, 25-40 etc ?
   - combine age/relationship to see if relationship effects can be explained away by age
4. `education_num` seems to be a label encoding of `education`. I think some degrees are not properly captured with that encoding, like `assoc-voc`. it would be interesting to to recode it with woe against `over50k` and see if anything changes. 
5. data quality questions: 
   - why are women under-represented in this data
   - why are there no hispanic/latin category in race?
6. compare to other interesting analysis:
   - Predicting Earning Potential using the Adult Dataset https://rpubs.com/H_Zhu/235617
   - related notebook on kaggle https://www.kaggle.com/uciml/adult-census-income
   

