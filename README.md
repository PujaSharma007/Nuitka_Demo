

## 1. What is Nuitka? 

Normally, Python programs are like a person reading a recipe book aloud line by line:
* The computer reads the plain-text script (`.py`) every single time it runs.
* Because the code is just plain text, anyone can open it, read private business secrets, or steal it.
* To run it, the user must install Python and download a bunch of extra files on their computer.

**Nuitka is a translator.** 
Instead of reading the code line by line every time, Nuitka takes the Python code and translates it directly into computer language (the same language used to build Windows). It then turns that into a normal Windows application (`.exe`).

### Benefits:
1. **Hidden Code:** The original Python code is converted into computer gibberish. Nobody can open the files and read the code.
2. **No Setup Needed:** The customer does not need to install Python or any extra tools. They just double-click the `.exe`.
3. **Faster:** The application runs smoothly and directly on the computer's processor.

> **Note:** The final executable format depends on the target operating system and architecture. The `.exe` extension applies to Windows builds; other operating systems use their respective executable formats/extensions. Therefore, the final output should not be assumed to always be a `.exe` file.

---

## 2. Licensing: Can It Be Used Commercially to Sell Software?-GNU Affero General Public License version 3 (AGPLv3).Link-https://github.com/Nuitka/Nuitka/blob/develop/LICENSE.txt

* **The Rule:** Nuitka includes an **explicit, official exception for all created applications**.
  * This means that **any application (`.exe`) created belongs 100% to the creator**.
  * The software does **NOT** have to be open-source.
  * Creators are legally allowed to sell the application to clients without sharing a single line of their secret code.

---

## 3. Two Ways to Build: Why `--standalone` Was Chosen

When building an application, there are two main ways to package it:

| Feature | The `--onefile` Way | The `--standalone` Way (What Was Used) |
|---|---|---|
| **What it does** | Squashes everything into a single `.exe` file. | Puts the `.exe` inside a neat folder alongside its required background files. |
| **How it starts up** | Every time it is double-clicked, Windows secretly unzips all files into a temporary hidden folder before it can start. | Starts running immediately with zero delay because files are already unzipped in the folder. |
| **Startup speed** | Very slow for apps that use heavy AI features. | Instant (starts in under 1 second). |

### Why was `--standalone` chosen?
This AI app relies on heavy internal tools (like reading PDFs and running math for the AI). 

If a single file was used:
* Every time a client launched the program, their computer would freeze just unzipping megabytes of heavy AI tools before anything appeared on the screen.
* By using **`--standalone`**, the application boots up instantly, runs smoothly, and allows the user to easily swap out their PDF documents without breaking the app.

---

## 4. How the AI App Works

1. **Read:** It reads a PDF document from a folder.
2. **Cut:** It cuts the text into smaller pieces.
3. **Remember:** It converts those pieces into a special format the AI can understand and saves them in a local memory folder.
4. **Answer:** It accepts user questions, finds the most relevant text from its memory, and asks a local AI to generate a natural, human-like answer.

### Overview of Files & Folders

Here is what every file and folder in the project does:

| Folder / File | What it is | Purpose in Simple English |
|---|---|---|
| `main.py` | Main Menu | The front door of the program. It asks if you want to read a document or ask questions. |
| `ingest.py` | PDF Reader | Pulls all the text out of the PDF files. |
| `chunker.py` | Text Cutter | Cuts large blocks of text into smaller, bite-sized pieces for the AI. |
| `store.py` | Memory Manager | Saves the bite-sized pieces of text into a smart folder on the computer. |
| `rag.py` | Chat Engine | The interactive chat screen. It fetches the right text from memory and asks the AI for answers. |
| `requirements.txt` | Shopping List | A list of extra tools the developer needed to build the app. |
| `data/` | Document Drop-box | The folder where users drop their raw PDFs before the app reads them. |
| `chroma_db/` | The Brain | The folder where the app saves everything it has memorized. |

---

## 5. Why Keep `data/` and `chroma_db/` Outside the App?

### 1. Why skip the `data/` folder?
* The `data/` folder is a drop-box for user PDFs. It needs to be easily accessible by end-users so they can add or remove documents at any time.
* If it were locked inside the `.exe`, users would never be able to add new documents!

### 2. Why skip the `chroma_db/` (The Brain) folder?
* This folder is a living memory. As users read new PDFs, this folder grows and changes.
* Applications (`.exe` files) are locked and cannot change. Therefore, the memory must sit outside the `.exe` so the application can read and write new memories to it.

---

## 6. Step-by-Step Build Instructions

Here is the exact process used to build and test the application from scratch:

### Step 1: Set Up the Tools
Ensure the environment is ready:
```cmd
pip install -r requirements.txt
```

### Step 2: Install the Builder
Install Nuitka (the tool that turns Python into an `.exe`):
```cmd
pip install nuitka
```

### Step 3: Run the Build Command
Run the following command to build the app:
```cmd
python -m nuitka --standalone --plugin-enable=pkg-resources --include-package=chromadb --include-package=fitz --include-package=onnxruntime --include-package=tokenizers main.py
```

#### What this command means in simple terms:
* `--standalone`: Put the app in its own neat folder (`main.dist`).
* `--plugin-enable=pkg-resources`: Help the app find its internal version numbers so it doesn't get confused and crash.
* `--include-package=...`: Sometimes the builder forgets to grab hidden, heavy AI files. These commands force it to grab every single required file so the app doesn't break later.

---

### Step 4: Add the Missing Folders
Once the builder finishes, it creates a new folder called `main.dist`. 
To ensure the app can read user documents, an empty data folder must be created inside it:

```cmd
cd main.dist
mkdir data
```
*(Place a test PDF document inside this newly created `data/` directory).*

---

### Step 5: Run and Test
To test the app:

```cmd
./main.exe
```

### Expected Output


```text
warning: The `fitz` API is deprecated and will be removed in future. Use `import pymupdf` instead.
=== Main RAG Application ===
1. Ingest Data (Reads PDFs from data/ and stores in chroma_db/)
2. Run RAG Q&A (Queries existing chroma_db/)
3. Exit

Select an option (1, 2, or 3): 1

--- Starting Ingestion ---
Reading data\wellhead.pdf...
Extracted 8703 characters.
Created 10 chunks.
Stored 10 chunks in ChromaDB.
--- Ingestion Complete ---


Select an option (1, 2, or 3): 2

--- Starting Q&A ---
Welcome to Simple Local RAG Q&A
Type 'quit' or 'exit' to stop.
--------------------------------------------------

Question: What is a wellhead?

Searching for context...

Retrieved context:
[1] Wellhead A wellhead is the component at the surface of an oil or gas well that provides the structural and  pressure containing interface for the dril...
[2] t is  referred to as a subsea wellhead or mudline wellhead. Primary Function of a Wellhead The primary function of a wellhead is pressure control to c...
[3] stallation Operation and Maintenance During installation, the wellhead is attached to the top of the surface casing and cemented in place.  Blowout pr...
[4] trol, sealing integrity, and long term reliability across oil,  gas, thermal, geothermal, and hydrogen applications. The Importance of Wellhead Innova...
[5] ll  through wellhead systems designed to support efficient drilling operations and pressure control. Its  wellhead systems are designed for applicatio...
[6] ature of  each well.Common working pressure ratings include 2000 psi, 5000 psi, 10000 psi, 15000 psi, and  up to 20000 psi for high pressure and high ...
[7] quipment is designed  for demanding drilling and production environments where pressure control, sealing integrity, and  operational reliability are i...

Answer:
A wellhead is the component at the surface of an oil or gas well that provides the structural and pressure containing interface for the drilling and production equipment.
--------------------------------------------------

Question: exit

Select an option (1, 2, or 3): exit
Exiting application...
```


> **Note:**:Nuitka cannot reliably resolve imports whose module names are determined dynamically at runtime, because the compiler does not know the final target module name during the build process. In such cases, the required module may not be included in the compiled application. If that module is missing from the final package, the program can fail at runtime with an ImportError or ModuleNotFoundError.