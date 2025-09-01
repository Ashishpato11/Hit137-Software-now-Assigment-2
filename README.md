# S225 – HIT137 Software Now – Assignment 2 (S1 2025)

## Structure
```
HIT137_Assignment2_S1_2025/
├─ q1_cipher.py
├─ q2_temps.py
├─ q3_turtle_pattern.py
├─ temperatures/            # put all stations_group_*.csv here
├─ github_link.txt
└─ README.md
```
Assignment2/
│
├── q1.py
├── q2.py
├── q3.py
│
├── inputs/
│   └── dataset.csv
│
├── outputs/
│   ├── encrypted.txt
│   ├── decrypted.txt
│   ├── results.csv
│   └── tree.png
│
├── docs/
│   └── report.docx
│
├── tests/
│   └── test_q1.py
│
├── README.md
├── requirements.txt
├── AI_Usage_Declaration.txt
├── .gitignore
└── CONTRIBUTING.md   (optional)


## Quickstart
### Q1 – Cipher
```
python q1_cipher.py
```
Enter two integers when prompted (e.g., 3 and 5). Note: due to rule collisions, verification may fail for some pairs. To demo a pass, use 0 and 0.

### Q2 – Temperatures (monthly station CSVs)
```
pip install pandas numpy
python q2_temps.py
```
Outputs:
- average_temp.txt
- largest_temp_range_station.txt
- temperature_stability_stations.txt
Also saves tidy_temperatures.csv

### Q3 – Recursive Pattern (turtle)
```
python q3_turtle_pattern.py
```
Enter sides / length / depth and a window will draw the pattern.

## Publish to GitHub
```
bash push_to_github.sh "https://github.com/<your-user>/hit137-assignment2-software-now-s1-2025.git"
```
Then paste your repo URL into github_link.txt, commit, and push.
