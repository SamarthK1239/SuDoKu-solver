# SuDoKu-solver
Yes I know that that's not how it's supposed to be capitalized, no I don't really care.

## Primary Dataset
Found on Kaggle <https://www.kaggle.com/datasets/rohanrao/sudoku?resource=download>, uploaded on Google Drive for my own Convenience and ease of access within Colab. 

Created by *Rohan Rao*, aka [*Vopani*](https://www.kaggle.com/rohanrao) on Kaggle

## Attempts
- Regression
  - I had a feeling this wouldn't work, but it was worth a shot. It's pretty interesting just how far off it really was

## Learnings
For starters, this dataset is massive, and that's... not a lot of fun. Colab kinda hates those super large files and forces you to optimize for memory as much as you can. As it stands, I can only really train the regression model on a dataset that contains 3.5 million datapoints without running out of memory on colab. I'm considering running this with GPU acceleration locally but we'll see about that some other time. As far as I can tell, regression won't work for a problem this complex.

The next possible approach is an RNN (and specifically an LSTM). Considering this is a task almost tailor made for an LSTM, I have much higher hopes. The issue lies in how to format this data so that the LSTM uses updated states.

Another approach I got started on was using a CSP Solver (Constraint Satisfaction Problem Solver) since sudoku is essentially just a set of constraints that you've got to work around. Now the issue lies in the fact that when constraints are set, there really isn't much you can do with a constraint solver alone. I think the key lies with combining a CSP with an RNN, allowing both the constraints to be used in addition intelligently picking which number to fill in next.


Sorry for stealing your idea [@ranjani-suraj](https://github.com/Ranjani-Suraj), it was just really interesting lmao
