# Content-Based-Document-Search-Engine
This project is a content-based document search engine developed using machine learning and text vectorization techniques. Built for the DSA469 course on Big Data Systems, it demonstrates a scalable system to search and rank HTML documents by content relevance.
## 🧠 Project Summary

- 🔎 Extracts text from HTML documents
- 🧹 Cleans and preprocesses the text (removes tags, stopwords, etc.)
- 🧮 Converts documents to vectors using **TF-IDF**
- 📐 Uses **cosine similarity** to rank results based on query relevance
- 🌐 Built with **Flask** (backend) and **HTML/CSS** (frontend)

---

## 🚀 How It Works

1. **Upload HTML documents**
2. **Enter a search query**
3. System ranks documents using cosine similarity to the query
4. Top results are returned in descending order of relevance

---

## ⚙️ Tech Stack

- Python
- Flask
- Scikit-learn (`TfidfVectorizer`)
- BeautifulSoup
- HTML / CSS

---

## 📊 Results

- Search engine successfully retrieved and ranked relevant documents
- Optimized for performance by caching vectors unless new files are uploaded

---

## 🧪 Example

You can try it using example HTML documents in the `searchbar.html` folder.

---

## 📈 Future Improvements

- Add real-time web scraping support
- Implement deep learning-based embeddings (e.g., BERT)
- Deploy on the web with Docker or Heroku


---

## 👤 Author

**Hardik Polamarasetti**  
[LinkedIn](www.linkedin.com/in/hardik-polamarasetti-baa344343)  
[GitHub](https://github.com/hpolam)
