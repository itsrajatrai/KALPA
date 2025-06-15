# 🌸 KALPA

> **KALPA** — *"A Language of Precision, Expression & Thoughtfulness"*

---

### 🔤 What is KALPA?

**KALPA** stands for:

> **K**nowledgeable  
> **A**rticulate  
> **L**anguage for  
> **P**rogrammable  
> **A**ctions

**KALPA** is a **human-first programming language** that emphasizes *structured thought*, *natural readability*, and *semantic clarity*.

It is **transpiled to Python**, so that developers and non-programmers alike can write expressive KALPA code — while Python remains fully hidden underneath.

---

### 🌿 Core Philosophy

> *"What if programming languages felt like structured thought, not machine code?"*

KALPA is influenced by:
- 🕉️ The **precision of Sanskrit** — every word matters, every rule has structure.
- 🧠 Human-first design — readable by non-coders, explainable by AI.
- 💡 A desire for new paradigms — with **natural syntax**, **data semantics**, and **declarative modeling**.

---

### 🔀 Modes of Expression

KALPA supports **two parallel modes**, both powered by the same core engine:

#### 🗣️ VAKYA Mode (Conversational)
Designed for beginners, non-coders, and AI agents.
```kalpa
mode: VAKYA
begin: greet user
  know name as TEXT "Arjun"
  do message as "Hello, " and name
  say message
  check message is not SHUNYA
💻 SANKHYA Mode (Symbolic)
Designed for developers who prefer concise syntax.

kalpa
Copy
Edit
mode: SANKHYA
intent: greet_user {
  know: TEXT name = "Arjun"
  do: message = "Hello, " + name
  do: print message
  check: message != SHUNYA
}
🧬 Sanskrit-Inspired Data Types
Type	Meaning	Use Case
NUMBER	Integer/float	Calculations, stats
TEXT	String data	Names, messages
TRUTH	Boolean logic	Conditions
SHUNYA	Null/empty	Safe null handling
ANANTA	Infinity	Unbounded values
LIST	Ordered items	Sequences
DICT	Key-value pairs	Metadata
SET	Unique values	Fast lookup
SAMYOGA	Immutable tuple	Config or fixed structures
BHAVA	Custom entities	Declarative structures with fields, constraints, and intents
SANDHI	Union type	Polymorphic inputs
KSHANA	Time durations	Scheduling, delays
SAMSARA	Live streams	IoT, sensor data, real-time flows

⚙️ How It Works
KALPA is a transpiler, not an interpreter.

txt
Copy
Edit
Your KALPA Code  -->  Transpiler  -->  Python Code  -->  Execution
The user never writes Python directly.

You write in VAKYA or SANKHYA — the transpiler handles the rest.

Ideal for beginner-friendly coding, AI co-pilots, and new forms of expression.

🤖 Prompt-to-Code Engine
KALPA supports basic prompt-based programming:

kalpa
Copy
Edit
prompt: "Greet a user named Arjun"
The engine will convert this into VAKYA or SANKHYA mode code. It enables:

Natural language → code generation

Rule-based prompt expansion

Future: LLM integration with structured type-checking

🧘 Why KALPA is Unique
✍️ Readable syntax — designed for humans first, machines second.

🕉️ Sanskrit-structured types — rich semantics, not just keywords.

⚡ Dual modes — VAKYA for simplicity, SANKHYA for precision.

💫 BHAVA — a declarative, intent-driven alternative to classes.

🔄 SAMSARA — native support for real-time data streams.

🧠 Prompt-friendly — AI-powered without the hallucination risks.

💡 Sample Use Case
Monitor a Sensor (VAKYA)
kalpa
Copy
Edit
mode: VAKYA
begin: monitor temperature
  know data as SAMSARA of NUMBER from "sensor"
  know interval as KSHANA duration 5 seconds
  do watch data every interval
    do filter values greater than 25
    do compute average and save in result
    say result
  check result is positive
📦 Current Status
✅ VAKYA Mode Parser

✅ SANKHYA Mode Parser

✅ Core transpiler to Python

🧪 Unique data types (BHAVA, SHUNYA, etc.)

🚧 Prompt-to-KALPA engine (WIP)

📄 Documentation + Playground coming soon

🔮 Roadmap
 Web playground (React + Flask)

 Prompt-to-code LLM fine-tuning

 VS Code Extension for KALPA

 Community-driven modules (bhava, samsara, mantra, etc.)

"A good program is not just correct. It is understandable, explainable, and beautiful."
