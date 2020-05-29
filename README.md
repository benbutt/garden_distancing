# garden_distancing
Python scripts to simulate social distancing in your very own (or anyone else's) back garden

Written in response to Boris Johnson's announcement on 28/05/20 that up to six people will be allowed to meet in their back garden provided "strict social distancing guidelines are followed": https://www.gov.uk/government/news/pm-six-people-can-meet-outside-under-new-measures-to-ease-lockdown.

Uses a rejection method to distribute points in rectangular area with customisable exclusion distance. Requires matplotlib.

--- How many friends can I fit in my garden while maintaining "strict social distancing guidelines"? ---

max_occupancy.py calculates the maximum occupancy for a given (rectangular) garden, and suggests a distribution to acheieve this occupancy.

--- How big does my garden need to be to invite my five (or more, when restrictions ease) friends round while maintaining "strict social distancing guidelines"? ---

garden_size.py calculates the minimum (square) garden size required to fit the requested occupancy, and suggests a distribution to achieve this occupancy.


Basic and expert parameters are highlighted at the top of the code.

Ben Butt, May 2020
