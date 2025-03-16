# Netflix Release Date Optimization

## Description

The Netflix Release Date Optimization project focuses on analyzing the release patterns of Netflix titles to optimize the release timing for maximizing viewership. By leveraging a dataset of Netflix titles (`netflix_titles.csv`), this project provides insights into trends such as seasonal content distribution, top genres, and directors. Additionally, it predicts the optimal season for releasing a title based on historical data using a Random Forest classifier.

### App Screenshot
![App Screenshot](https://github.com/Adityalolla04/Netflix-Release-Date-Optimization-for-Maximum-Viewership/blob/main/Images/app_screenshot.png)


## Key Steps in the Project

### 1. Data Cleaning and Preprocessing
- **Dataset Overview**: The dataset contains 8,807 entries with features like title, type (movie or TV show), director, cast, country, date added, release year, rating, and description.
- **Data Issues Addressed**:
  - Missing values in columns like `country`, `director`, and `cast` were replaced with `"Unknown"`.
  - A new feature, `season`, was created by mapping release months to their corresponding seasons (e.g., `January-March → Winter`).
  - Missing values in the `date_added` column were imputed using the most frequent values in the dataset.

### 2. Exploratory Data Analysis (EDA)
- **General Statistics**:
  - The dataset spans titles from 1925 to 2021.
  - Movies and TV shows are nearly evenly distributed.
- **Visualizations**:
  - **Bar Chart**: The number of titles added by release type (movies and TV shows).
  - **Pie Chart**: Distribution of titles across different countries.
  - **Trend Analysis**: Year-wise addition of titles shows a steady increase, with a sharp rise after 2015.
  - **Top Genres and Directors**: The most frequent genres and directors contributing to the Netflix library.

### 3. Predictive Modeling
- **Model**: A Random Forest classifier was trained to predict the optimal release season for a Netflix title.
- **Features**:
  - Type (Movie/TV Show)
  - Genres (e.g., Action, Comedy)
  - Release Year
- **Performance**:
  - Achieved **95.94% accuracy** on the testing data.
  - The model is capable of predicting seasons like Winter, Spring, Summer, and Fall based on title attributes.

### 4. Insights and Trends
- **Seasonal Distribution**:
  - A large proportion of titles are added in Fall and Summer.
  - Winter sees the least number of new releases, possibly due to reduced audience engagement.
- **Top Genres and Countries**:
  - Popular genres include Drama, Comedy, and Documentaries.
  - The U.S., India, and the U.K. dominate in terms of content production.

## Visualizations

### 1. Seasonal Distribution of Titles
- A bar chart showing the number of titles released across Winter, Spring, Summer, and Fall.

### Seasonal Distribution of Titles
![Seasonal Distribution of Titles](https://github.com/Adityalolla04/Netflix-Release-Date-Optimization-for-Maximum-Viewership/blob/main/Images/Seasonal%20Distribution%20of%20titles.png)


### 2. Genre and Country Analysis
- Pie and bar charts illustrate the distribution of titles by genre and country.

### Countries Distribution
![Countries Distribution](https://github.com/Adityalolla04/Netflix-Release-Date-Optimization-for-Maximum-Viewership/blob/main/Images/Contries.png)

### 3. Predicted Release Season Distribution
- A bar plot visualizing the predicted release seasons for different genres.

### Predicted Release Season Distribution
![Predicted Release Season Distribution](https://github.com/Adityalolla04/Netflix-Release-Date-Optimization-for-Maximum-Viewership/blob/main/Images/Predicted%20Release%20Season%20Distribution.png)


## Project Highlights

1. **Data Cleaning**:
   - Addressed missing values and created new features like `season` for analysis.
   - Ensured the dataset was suitable for predictive modeling.

2. **Exploratory Insights**:
   - Visualized key trends in Netflix content addition over time.
   - Identified seasonal patterns and genre distributions.

3. **Machine Learning**:
   - Developed a robust Random Forest model to predict the optimal release season for new titles.
   - The model achieved an exceptionally high accuracy of **96.94%**.

4. **User Interaction**:
   - The project is integrated into a **Streamlit app**, providing an interactive interface for filtering titles and visualizing insights.



## Technical Summary

### Data Sources
- **Dataset**: `netflix_titles.csv`
  - Contains 8,807 entries and 12 features.

### Tools and Technologies
- **Data Manipulation**: Pandas and NumPy
- **Visualization**: Matplotlib and Seaborn
- **Machine Learning**: Scikit-learn (Random Forest Classifier)
- **App Development**: Streamlit for an interactive web application.

### Model Details
- **Model**: Random Forest Classifier
- **Target**: Optimal release season (Winter, Spring, Summer, Fall)
- **Accuracy**: **95.94%**


## Key Insights

- **Seasonal Trends**: Fall and Summer are the most popular seasons for releasing new titles, while Winter sees fewer releases.
- **Content Trends**: Drama, Comedy, and Documentaries are the dominant genres, with most content coming from the U.S., India, and the U.K.
- **Predictive Capabilities**: The project provides a data-driven approach to optimize Netflix release dates for maximum viewership.

## Conclusion

The Netflix Release Date Optimization project demonstrates how data analytics and machine learning can help optimize the timing of content releases for maximum audience engagement. By identifying seasonal trends, popular genres, and predictive insights, this project provides a robust framework for decision-making in the media industry.
