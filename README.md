Housing Affordability Simulation in Los Angeles (Python)

This project uses Python to simulate housing affordability for six working-class families in Los Angeles, based on income scenarios and rent expectations. Inspired by a Math & Social Justice class assignment, the analysis applies the 30% rent-to-income affordability rule to assess whether California’s minimum wage of $16/hour supports fair housing in LA’s high-cost environment.

Financial Models Used
30% Rule: Rent is affordable if it does not exceed 30% of monthly income

Wage Conversion: Monthly income calculated using hourly wage × weekly hours × 4.33

Affordability Check: Compared required affordable rent (30% of income) to actual expected rent

Work Hours Estimation: Calculated weekly hours needed at $16/hour to afford rent per the 30% guideline

Data Source
This project uses realistic synthetic data created from:

California minimum wage (2024): $16/hour

Family income profiles and rent expectations: Based on classroom scenarios reflecting tipped workers, dual-income households, part-time workers with scholarships, and wage inequality

Fair Market Rent estimates in LA County (e.g., studio = $1,777; 2-bedroom = $2,544)

Family Outcomes & Metrics
Based on the simulation, here’s how each family fares under the 30% rule:

🔴 Red Family: $2,560/mo income
▸ Affordable rent = $768
▸ Expected rent = $1,777 → Unaffordable
▸ Needs ~86 hours/week at $16/hr to afford

🟢 Green Family: $3,040/mo income (wages + tips)
▸ Affordable rent = $1,011
▸ Expected rent = $1,777 → Unaffordable
▸ Needs ~103 hours/week

🔵 Blue Family: $5,120/mo income (father earns 2× min wage)
▸ Affordable rent = $1,538
▸ Expected rent = $2,544 → Unaffordable
▸ Needs ~138 hours/week if only one parent works

🟡 Yellow Family: $2,560/mo income (64% of typical wage)
▸ Affordable rent = $820
▸ Expected rent = $1,777 → Unaffordable
▸ Needs ~93 hours/week

🟠 Orange Family: $2,960/mo (part-time + scholarship)
▸ Affordable rent = $888
▸ Expected rent = $1,777 → Unaffordable
▸ Needs ~103 hours/week

🟣 Purple Family: $5,520/mo (2 adults @ $17.25/hr)
▸ Affordable rent = $1,656
▸ Expected rent = $2,544 → Unaffordable, but closest
▸ Needs ~92 hours/week

Key Metric: 0 out of 6 families could afford rent while working full-time at or near minimum wage, based on the 30% rule.

Observations from the Chart
Using the generated bar chart, it’s visually clear that all families would need to work well over 40 hours/week to afford rent — some requiring 80 to 140 hours/week. The Blue Family and Yellow Family show the highest burden due to single-income dependency and wage disparities.

Conclusion
This simulation highlights the severe mismatch between minimum wage levels and housing costs in Los Angeles. Even with two earners or supplemental income (like tips or scholarships), families are unable to meet the 30% affordability rule without extreme work schedules.

This analysis supports the conclusion that California’s current minimum wage does not meet the housing demands of its working families. Without wage increases, housing subsidies, or broader systemic reforms, the cost of living in high-demand areas like LA will continue to be unsustainable for low- and middle-income households.

