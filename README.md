# 🧠 Mini Compiler - PBL Project

> A full-stack web-based **compiler simulator** built from scratch using **React** and **Flask**, capable of performing **lexical analysis**, **parsing**, **semantic analysis**, **intermediate code generation**, and **target code generation** (MIPS). It also supports **custom grammar input** and **visualizes the parse tree** beautifully.

---

## 🚀 Features

- 🧾 Lexical Analysis using PLY (Lex)
- 🌲 Syntax Parsing with user-defined grammar using PLY (Yacc)
- ✅ Semantic Analysis with error reporting
- 🧠 Abstract Syntax Tree (AST) and Parse Tree visualization
- ⚙️ Intermediate Code Generation (Three-Address Code)
- 🧮 Target Code Generation in MIPS format
- 💻 Monaco Editor for source code and grammar input
- 🎯 Full-stack integration with clean API flow
- 📥 Downloadable Output Report and Parse Tree (SVG)

---

## 🛠️ Tech Stack

### 🔹 Frontend (React)
- React.js
- Monaco Editor
- Tailwind CSS (if used)
- react-d3-tree (for Parse Tree)
- jsPDF + FileSaver (for downloads)

### 🔹 Backend (Python)
- Flask
- Flask-CORS
- PLY (Python Lex-Yacc)


---

## 🧪 How It Works

1. User types source code and grammar into Monaco editors
2. Frontend sends both to backend via `/compile` endpoint
3. Backend performs:
   - Lexical analysis → tokens
   - Syntax parsing → parse tree & AST
   - Semantic analysis → error checks
   - IR generation → 3-address code
   - Target code → MIPS instructions
4. Result is returned and visualized

---

## 🔧 Setup Instructions

### 1. Clone the Repo
```bash
git clone https://github.com/VinodPandey14/Mini-Compiler.git
cd mini-compiler
``` 

### 2. Backend (Flask)
```
cd backend
pip install -r requirements.txt
python app.py
By default, runs at: http://localhost:5000
```
### 3. Frontend (React)
```
cd frontend
npm install
npm start
Runs at: http://localhost:3000
```

# 📥 Downloads

### ✅ Output report (compiler_output.txt)

### 🌳 Parse tree image (parse_tree.svg)

---

# 👨‍💻 Built By
### Vinod Pandey
#### B.Tech CSE | Graphic Era Hill University
