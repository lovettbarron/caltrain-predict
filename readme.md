# Predictive Model of Caltrain Delays
### GA Data Science certificate course
This project is an attempt to analyze twitter (and other) datas to understand whether I can detect disruption within the Caltrain system, and map (with some degree of accuracy) the probability that something will go wrong.
![Render](https://raw.githubusercontent.com/readywater/caltrain-predict/5a2ff7302e717b3f3b8df3611df4bfc914f9ad18/render.png)

### Use (all ipython notebooks)
1. **00getdata** - Download and transform twitter data
2. **01sepEvents** - Separate tweets into unique events
3. **03explore** - Initial poking around
4. **03merge_hand_truth** - Merge in hand truth data, _truth\_tweets.csv_
5. **04fill_in_positives** - Take _all\_stops\_in\_pa.csv_ and transform into positives data set
6. **05merge_with_positives** - Merge in positives set
7. **06initial_analysis** - Sketchpad for early interprtetive models
8. **07focus_decision_tree** - Complete analysis: Decision trees and gradient boosting, as well as multiple predictive approaches and tuning.

