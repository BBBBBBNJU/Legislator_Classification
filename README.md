# Legislator_Classification
Results for Legislator Classification project
We have two folders here: `separate` and `together`.

`together` folder contains that experiment results that we consider Congress 
people's Congressional Record and Press Releases as two virtual people. For 
example, Alice's Congressional Record and Press Releases are actually Alice1 
and Alice2. Then we run one bootstrap experiment with both Alice1 and Alice2.

`separate` folder is different. We run two bootstrap experiments with Congressional 
Record and Press Releases, respectively.

In each folder, there is a `figures` folder, two `.csv` files: `congress_people_info.csv` and `non-overlap.csv`.

`figures` folder contains all bootstrap experiments results and histogram figures.

`congress_people_info.csv` contains the 97.5 and 2.5 percentile interval results.

`non-overlap.csv` shows those Congress people whose Congressional Record and Press Releases 97.5-2.5 
percentile intervals are disjoint.

test

