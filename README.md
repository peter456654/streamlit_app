# Physics Equations Streamlit App

A simple web application built using **Python** and **Streamlit** to display important physics equations.

This project demonstrates how to build a basic frontend interface using Streamlit and render physics formulas using LaTeX.

---

## Features

* Interactive web interface
* Displays common physics equations
* Uses LaTeX for mathematical formatting
* Beginner-friendly Python project

---

## Physics Equations Included

* Newton's Second Law
* Einstein Mass-Energy Equation
* Kinematic Equation
* Gravitational Force
* Ohm's Law

Examples:

F = ma
E = mc²
v = u + at

---

## Project Structure

```
streamlit-physics-app
│
├── app.py
├── requirements.txt
└── README.md
```

---

## Installation

1. Clone the repository

```
git clone https://github.com/your-username/streamlit-physics-app.git
```

2. Navigate to the project folder

```
cd streamlit-physics-app
```

3. Install dependencies

```
pip install -r requirements.txt
```

---

## Running the Application

Run the following command:

```
streamlit run app.py
```

The application will open in your browser at:

```
http://localhost:8501
```

---

## Example Code (app.py)

```python
import streamlit as st

st.title("Physics Equation App")

st.header("Newton's Second Law")
st.latex(r"F = ma")

st.header("Einstein Equation")
st.latex(r"E = mc^2")
```

---

## Technologies Used

* Python
* Streamlit
* LaTeX

---

## Future Improvements

* Add more physics formulas
* Build interactive physics calculators
* Add UI styling
* Deploy online using Streamlit Cloud

---

## Author

Created as a beginner project to learn Streamlit and GitHub workflow.
