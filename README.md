# 🎬 ScriptSentinel: AI-Based Scene Feasibility & Risk Predictor


> **"Don't just predict risks. Predict costs, liabilities, and physics."**

**ScriptSentinel** is an advanced AI-powered "Line Producer" that analyzes film scripts for logistical feasibility, safety risks, and legal liabilities. Unlike standard tools that simply look for keywords (e.g., "Fire" = Danger), ScriptSentinel uses **Interpretive Reasoning** to understand context, local laws, and physical constraints.

---

## 🚀 The Problem
Many scenes look great on paper but are high-risk, expensive, or legally impossible to execute.
* **The "Context" Blindspot:** Standard AI sees "Rain" and suggests an umbrella. It fails to realize that *Rain + Night Shoot + 300 Extras* = A logistical nightmare.
* **The "Locale" Blindspot:** A snow scene is cheap in Kashmir but logistically impossible (and dangerous) in tropical Kerala.
* **The "Liability" Blindspot:** Most tools ignore local labor laws (e.g., Child Labour Acts) and historical safety precedents.

---

## 💡 The Solution: ScriptSentinel
ScriptSentinel acts as a **War Room** of three expert AI agents—a Stunt Coordinator, a Lawyer, and a Physicist—debating the script in real-time.

### ✨ Key Features (The 4 Novelty Pillars)

#### 1. 🌍 Locale-Adaptive Engine
* **What it does:** Adjusts risk assessments based on the physical realities of the location.
* **Example:** Flags "Heavy Snow" in **Kerala (Tropical)** as a **Critical Logistics Failure** (Heatstroke risk + massive chemical foam cost), whereas in **Kashmir**, it is marked as Low Risk.

#### 2. 🛡️ Context-Aware Mitigation
* **What it does:** Identifies **Combinatorial Risks** (when two safe things become dangerous together).
* **Example:** "Rain" is fine. "Night" is fine. "Rain + Night" is a **Visibility Hazard** requiring specific "Wet-Down" techniques instead of active rain towers.

#### 3. ⚖️ Liability & Precedent Oracle
* **What it does:** Checks script actions against **Local Laws** and cites **Historical Accidents**.
* **Example:** Detects a "Child Actor" in a "Night Scene" and flags it as a violation of the *Child Labour (Prohibition and Regulation) Rules, 2017*. Cites the *Twilight Zone Movie* accident for helicopter risks.

#### 4. ⏳ Time & Physics Validator
* **What it does:** Detects "Invisible Risks" like impossible lighting windows.
* **Example:** A 5-page dialogue scene set at "Sunset" (which lasts only 20 mins) is flagged as a **Physics Failure** because you will run out of light before shooting is complete.

---

## 🛠️ Technology Stack

| Component | Technology Used | Why We Chose It |
| :--- | :--- | :--- |
| **Inference Engine** | **Google Gemini 1.5 Flash** | Chosen for its 1M+ token context window (can read full scripts) and superior multilingual reasoning. |
| **Frontend / UI** | **Streamlit** | Provides a rapid, reactive "Glassmorphism" interface for zero-latency feedback. |
| **Backend Logic** | **Python 3.10+** | Utilizes strict JSON parsing to force the AI into a deterministic output structure. |
| **Deployment** | **Streamlit Cloud** | Serverless architecture for instant scalability and GitHub integration. |

---

## 📸 Demo & Screenshots

| **The "War Room" Dashboard** | **Multilingual Support (Hindi)** |
|:---:|:---:|
| <img width="1558" height="583" alt="image" src="https://github.com/user-attachments/assets/a0eb725d-93d0-4378-9531-078181ce4621" />| <img width="968" height="329" alt="image" src="https://github.com/user-attachments/assets/73c5b805-6181-4d6f-b02a-234fb6e1094b" />
| *Real-time risk badges & mitigation plans* | *Input Hindi -> Output Hindi analysis* |

---

## ⚡ Installation & Local Run

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/YourUsername/script-sentinel.git](https://github.com/YourUsername/script-sentinel.git)
    cd script-sentinel
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set Up API Key**
    * Get your FREE API Key from [Google AI Studio](https://aistudio.google.com/).
    * Open `app.py` and paste your key in the `api_key` variable (or set via `st.secrets` for cloud deployment).

4.  **Run the App**
    ```bash
    streamlit run app.py
    ```

---

## 🧠 How It Works (Architecture)

1.  **Input:** User pastes a script scene (in English, Hindi, Malayalam, etc.).
2.  **Context Injection:** The user selects a "Shooting Location" (e.g., Hyderabad, Kerala).
3.  **The "War Room" Simulation:**
    * The **Gemini 1.5 Flash** model receives a complex System Prompt acting as a Line Producer.
    * It cross-references the script against:
        * *Local Weather/Terrain Physics*
        * *Labor Laws & Safety Guidelines*
        * *Historical Accident Databases*
4.  **Structured Output:** The AI forces a strict JSON output containing Risk Levels, Mitigation Strategies, and Novelty Scores.
5.  **Rendering:** Streamlit parses the JSON and renders the "Glassmorphism" UI with dynamic risk badges.

---

## 📜 License
This project is licensed under the MIT License.

---

*Built with ❤️ by RaknaTech*
