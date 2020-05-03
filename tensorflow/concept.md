# Supervised ML
Combine input to produce useful predictions on never-before-seen data.

- Label - **y**
  - Output we're predicting
  - eg: Is a spam email or not
- Faeture - **{x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>n</sub>}**
  - Input variables describing our data
  - eg: Email sender, email title, time of day the email was sent, ...
- Example - **x**
  - A particular instance of data
- Labeled example - **{features, label} : (x, y)**
  - Used to train the model
- Ublabeled exmaple - **{features, ?} : (x, ?)**
  - Used for making predictions on new data
- Model - **y'**
  - Defined by internal paramters, which are learned

Descending - Linear Regression 

- y<sup>'</sup> = b + w<sub>1</sub>x<sub>1</sub> + w<sub>2</sub>x<sub>2</sub> + ... + + w<sub>n</sub>x<sub>n</sub>
- **L<sub>2</sub> Loss**\
= square of the difference between prediction and label\
= (observation - presiction)<sup>2</sup>\
= (y - y<sup>'</sup>)<sup>2</sup>
- **L<sub>2</sub> Loss** on a data set: summing over all examples in the trrainning set then average over all exmaples

Reducing Lose - Gradient Descent
- Repeatedly take small steps in the direction that minimizes loss

