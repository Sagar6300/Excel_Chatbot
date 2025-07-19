# 📊 Excel-Based Insights Chatbot

This project is a Streamlit-based chatbot that helps you interact with Excel files using natural language.
Users can upload Excel files and ask questions in plain English to receive clear responses in the form of text, tables, or visual charts.

---

## 🌐 Access the Web Application  
Use the link below to interact with the deployed chatbot:  

🔗 [Launch the Web App](https://excelchatbot-etuafuzrjcco2xzqdhjfti.streamlit.app/)

---

## Features

- Upload Excel files and preview the data.
- Ask natural language questions about the dataset.
- Automatic visualization using matplotlib/seaborn based on LLM responses.
- Visual Insights: Automatically generates bar charts, line graphs, or histograms based on your query.
- Smart Column Detection: Automatically infers numeric, categorical, or binary types.
- Google Gemini API integration for intelligent responses.
---

## Input Requirements

- Format: `.xlsx`
- Structure: Single sheet, one header row, tabular data
- Size: Up to 500 rows and less than 50 columns
- Columns: May contain numeric, categorical, binary values, or nulls
- Column names can include spaces, special characters, or inconsistent casing

---

## Example Queries

- "What is the average salary?"
- "How many customers are under 30?"
- "Compare loan defaults by gender"
- "Show a bar chart of transaction count by job"
- Show a line chart of External Intervention across the top 15 countries.
- Visualize the correlation between Group Grievance and Factionalized Elites.

---

## Screenshots

### Interface:  

##### Before Uploading the Excel File

<img width="1920" height="1017" alt="Screenshot (5414)" src="https://github.com/user-attachments/assets/0003ea98-bd59-4acc-a148-c7d9257bb00f" />

##### After Uploading the Excel File

<img width="1920" height="1014" alt="Screenshot (5415)" src="https://github.com/user-attachments/assets/a7563784-214b-4661-8ef6-b81efde84862" />

<img width="1920" height="1021" alt="Screenshot (5416)" src="https://github.com/user-attachments/assets/4ff20637-1813-408b-b034-73e0357b0b3c" />


 ### Chatbot Responses:

 ##### Chatbot Response 1
 <img width="1920" height="1017" alt="Screenshot (5417)" src="https://github.com/user-attachments/assets/4783418f-b3d3-414c-99d2-46865f8fe07f" />
 
 ##### Chatbot Response 2
 <img width="1920" height="1021" alt="Screenshot (5418)" src="https://github.com/user-attachments/assets/1af9f3ea-229c-46a8-a0fd-8a91fe4899a5" />
 
 ##### Chatbot Response 3
 <img width="1920" height="1017" alt="Screenshot (5419)" src="https://github.com/user-attachments/assets/959a7844-26b8-4abb-a068-6be6575215f4" />
 
 ##### Chatbot Response 4
 <img width="1920" height="1021" alt="Screenshot (5420)" src="https://github.com/user-attachments/assets/3e3d7b9f-9269-4e8b-b70f-213aa72b26b3" />
 
 ##### Chatbot Response 5
 <img width="1920" height="1024" alt="Screenshot (5436)" src="https://github.com/user-attachments/assets/9bcd078e-d496-483c-9b9b-393d4a14e842" />
 
 ##### Chatbot Response 6
 <img width="1920" height="1021" alt="Screenshot (5423)" src="https://github.com/user-attachments/assets/05a3902c-3687-4313-ab34-d37d632aae6c" />

 <img width="1920" height="1017" alt="Screenshot (5424)" src="https://github.com/user-attachments/assets/2607435c-f10b-4a35-b03f-0a46005a4005" />
 ##### Chatbot Response 7
 <img width="1920" height="1024" alt="Screenshot (5428)" src="https://github.com/user-attachments/assets/2557c940-07ec-4310-b0be-2f5debd666c6" />

 <img width="1920" height="1017" alt="Screenshot (5429)" src="https://github.com/user-attachments/assets/6ef425dd-07d8-41a8-a3d1-2206b117b6ab" />
 
 ##### Chatbot Response 8
 <img width="1920" height="1021" alt="Screenshot (5430)" src="https://github.com/user-attachments/assets/7eb4cc48-ec35-486c-a83a-e8859356c4a9" />
 
 ##### Chatbot Response 9
 <img width="1920" height="1017" alt="Screenshot (5433)" src="https://github.com/user-attachments/assets/69e2aa1c-9fba-4e79-95ab-c90c52ccf837" />

 <img width="1920" height="1017" alt="Screenshot (5434)" src="https://github.com/user-attachments/assets/b4386eba-7e49-42bd-9f94-e6de9937e8a9" />

---

## Technologies Used

- **Frontend**: Streamlit
- **Backend**: Python
- **LLM Integration**: Google Gemini API via `google-generativeai`
- **Data Handling**: pandas, matplotlib, seaborn
- **Environment Config**: dotenv

---

## Deployment

This application is deployed on Streamlit Cloud and is accessible through a public URL for easy access and testing.
