# ebay-tech-deals
EDA Report – cleaned_ebay_deals.csv
1. What I Did

I worked on exploring a dataset of eBay tech deals. The data has product titles, prices, original prices, shipping info, and timestamps. My goal was to understand patterns in prices, discounts, shipping options, when deals are posted, and what products are common.

2. Cleaning the Data

Before analyzing, I cleaned the data:

Removed symbols like $ and US from the price and original_price columns and converted them to numbers.

Filled missing original_price with the current price when it was empty.

For shipping info, I replaced empty or "N/A" values with "Shipping info unavailable".

Removed duplicate rows based on item_url to avoid repeated products.

Calculated the discount percentage and absolute discount for each product.

3. Analysis Steps
3.1 Time Analysis

Converted timestamp to datetime and extracted the hour.

Grouped the data by hour and plotted the number of deals per hour.

Observation: Most deals were posted in the afternoon and early evening.

3.2 Prices and Discounts

I plotted histograms and boxplots to see the distribution of prices.

Compared original_price versus price using a scatter plot.

Checked how discounts vary using a histogram of discount_percentage.

Observation: Most products are in lower price ranges, but some expensive products exist. Discounts vary a lot; some deals had big discounts, over 50%.

3.3 Shipping

Counted the different shipping options and plotted a bar chart.

Observation: Most products have normal shipping, but some don’t show shipping info.

3.4 Product Titles

Chose keywords like "Apple", "Samsung", "Laptop", "iPhone", "Tablet", "Gimbal".

Counted how often these keywords appeared in titles, ignoring case.

Plotted a bar chart of keyword frequencies.

Observation: Apple and Samsung products are very common. Laptops and iPhones are the most frequent items.

3.5 Price Difference

Created a column for absolute discount (original_price - price).

Plotted a histogram.

Observation: Most discounts are small, but a few items had very high discounts.

3.6 Top Discounts

Sorted the data by discount_percentage to see the top 5 deals.

Observation: Some deals gave huge discounts, even more than 70%.

4. Problems I Faced

Many duplicates made the dataset bigger than it should be.

Prices were messy with $, US, and commas.

Missing shipping info needed fixing.

Product titles had different ways of writing brands and models.

5. Ideas for Improvement

Use NLP to detect brands and product types automatically.

Check trends over days or weeks, not just hours.

Compare discounts with brands and categories.

Make interactive charts with hover info using Plotly.

6. Conclusion

This project helped me understand eBay tech deals better. I now know when deals are posted, what products are most common, how discounts work, and how shipping is handled. This cleaned dataset can be useful for finding deals, predicting prices, or building a recommendation system.