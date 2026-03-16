1. Age-wise Analysis (Identifying high-risk groups)
Question: Kaunse age groups mein vision issues ka total value sabse zyada hai?
Query:
SELECT Age, SUM(Data_Value) AS Total_Value
FROM vision_data
GROUP BY Age
ORDER BY Total_Value DESC;

Insight: Data se pata chala ki 18-39 aur 65+ groups mein vision health focus ki sabse zyada zarurat hai.

2. Risk Factor Impact
Question: Diabetes, Smoking aur Hypertension ka vision health par kya asar hai?
Query:
SELECT RiskFactor, SUM(Data_Value) AS Total
FROM vision_data
GROUP BY RiskFactor;

Insight: Smoking aur Diabetes sabse bade risk factors nikal kar aaye.

3. Gender-based Comparison
Question: Kya vision issues gender ke basis par differ karte hain?
Query:
SELECT Gender, SUM(Data_Value) AS Total
FROM vision_data
GROUP BY Gender;

4. Data Quality Check
Question: Kya dataset mein koi missing (NULL) values hain?
Query:
SELECT * FROM vision_data WHERE Data_Value IS NULL;

5. Top Functional Challenges
Question: Logo ko sabse zyada kis tarah ki dekhne ki dikkat (functional difficulty) ho rahi hai?
Query:
SELECT Question, SUM(Data_Value) AS Total
FROM vision_data
GROUP BY Question
ORDER BY Total DESC
LIMIT 5;
Insight: "Reading Difficulty" aur "Seeing up close" sabse bade challenges hain.
