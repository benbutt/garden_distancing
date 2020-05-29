# garden_distancing
Python script to simulate social distancing in your very own (or anyone else's) back garden

Written in response to Boris Johnson's announcement on 28/05/20 that up to six people will be allowed to meet in their back garden provided "strict social distancing guidelines are followed": https://www.gov.uk/government/news/pm-six-people-can-meet-outside-under-new-measures-to-ease-lockdown.

But how big does my garden need to be to invite my five friends round while still maintaining "strict social distancing guidelines"?
And how many friends can I invite round given the size of my garden when restrictions ease further?

Uses a rejection method to distribute points in rectangular area with fixed exclusion distance.
Important parameters are highlighted at the top of the code. Currently only works for square/rectangular gardens.
Requires matplotlib, datetime

Ben Butt, May 2020
